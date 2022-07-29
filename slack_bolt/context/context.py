# pytype: skip-file
from typing import Optional

from slack_sdk import WebClient

from slack_bolt.context.ack import Ack
from slack_bolt.context.base_context import BaseContext
from slack_bolt.context.respond import Respond
from slack_bolt.context.say import Say
from slack_bolt.context.complete_success import CompleteSuccess
from slack_bolt.context.complete_error import CompleteError
from slack_bolt.util.utils import create_copy

CLIENT: str = "client"
ACK: str = "ack"
SAY: str = "say"
RESPOND: str = "respond"
COMPLETE_ERROR: str = "complete_error"
COMPLETE_SUCCESS: str = "complete_success"


class BoltContext(BaseContext):
    """Context object associated with a request from Slack."""

    def to_copyable(self) -> "BoltContext":
        new_dict = {}
        for prop_name, prop_value in self.items():
            if prop_name in self.standard_property_names:
                # all the standard properties are copiable
                new_dict[prop_name] = prop_value
            else:
                try:
                    copied_value = create_copy(prop_value)
                    new_dict[prop_name] = copied_value
                except TypeError as te:
                    self.logger.warning(
                        f"Skipped setting '{prop_name}' to a copied request for lazy listeners "
                        "due to a deep-copy creation error. Consider passing the value not as part of context object "
                        f"(error: {te})"
                    )
        return BoltContext(new_dict)

    @property
    def client(self) -> Optional[WebClient]:
        f"""The `WebClient` instance available for this request.

            @app.{CLIENT}("app_mention")
            def handle_events(context):
                context.{CLIENT}.chat_postMessage(
                    channel=context.channel_id,
                    text="Thanks!",
                )

            # You can access "{CLIENT}" this way too.
            @app.event("app_mention")
            def handle_events({CLIENT}, context):
                {CLIENT}.chat_postMessage(
                    channel=context.channel_id,
                    text="Thanks!",
                )

        Returns:
            `WebClient` instance
        """
        if CLIENT not in self:
            self[CLIENT] = WebClient(token=None)
        return self[CLIENT]

    @property
    def ack(self) -> Ack:
        f"""`{ACK}()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.{ACK}()

            # You can access "{ACK}" this way too.
            @app.action("button")
            def handle_button_clicks({ACK}):
                {ACK}()

        Returns:
            Callable `{ACK}()` function
        """
        if ACK not in self:
            self[ACK] = Ack()
        return self[ACK]

    @property
    def say(self) -> Say:
        f"""`{SAY}()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()
                context.{SAY}("Hi!")

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack, {SAY}):
                ack()
                {SAY}("Hi!")

        Returns:
            Callable `{SAY}()` function
        """
        if SAY not in self:
            self[SAY] = Say(client=self.client, channel=self.channel_id)
        return self[SAY]

    @property
    def respond(self) -> Optional[Respond]:
        f"""`{RESPOND}()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()
                context.{RESPOND}("Hi!")

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack, {RESPOND}):
                ack()
                {RESPOND}("Hi!")

        Returns:
            Callable `{RESPOND}()` function
        """
        if RESPOND not in self:
            self[RESPOND] = Respond(
                response_url=self.response_url,
                proxy=self.client.proxy,
                ssl=self.client.ssl,
            )
        return self[RESPOND]

    @property
    def complete_success(self) -> CompleteSuccess:
        f"""`{COMPLETE_SUCCESS}()` function for this request.

            @app.function("reverse")
            def handle_button_clicks(context):
                context.{COMPLETE_SUCCESS}({{"stringReverse":"olleh"}})

            @app.function("reverse")
            def handle_button_clicks({COMPLETE_SUCCESS}):
                {COMPLETE_SUCCESS}({{"stringReverse":"olleh"}})

        Returns:
            Callable `{COMPLETE_SUCCESS}()` function
        """
        if COMPLETE_SUCCESS not in self:
            self[COMPLETE_SUCCESS] = CompleteSuccess(client=self.client, function_execution_id=self.function_execution_id)
        return self[COMPLETE_SUCCESS]

    @property
    def complete_error(self) -> CompleteError:
        f"""`{COMPLETE_ERROR}()` function for this request.

            @app.function("reverse")
            def handle_button_clicks(context):
                context.{COMPLETE_ERROR}("an error spawned")

            @app.function("reverse")
            def handle_button_clicks({COMPLETE_ERROR}):
                {COMPLETE_ERROR}("an error spawned")

        Returns:
            Callable `{COMPLETE_ERROR}()` function
        """
        if COMPLETE_ERROR not in self:
            self[COMPLETE_ERROR] = CompleteError(client=self.client, function_execution_id=self.function_execution_id)
        return self[COMPLETE_ERROR]
