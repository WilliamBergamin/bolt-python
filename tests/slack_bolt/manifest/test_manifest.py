import os
import json

from slack_bolt.manifest.manifest import Manifest
from slack_bolt.manifest.models.manifest_schema import (
    ManifestAppHomeSchema,
    ManifestBotUserSchema,
    ManifestDisplayInformationSchema,
    ManifestEventSubscriptionsSchema,
    ManifestFeaturesSchema,
    ManifestInteractivitySchema,
    ManifestMetadataSchema,
    ManifestOauthConfigSchema,
    ManifestSettingsSchema,
    ManifestShortcutSchema,
    ManifestSlashCommandSchema,
    Scopes,
    ShortcutType,
)


class TestManifest:

    working_directory = "tests/slack_bolt/cli/test_app"

    def setup_method(self, method):
        os.environ["SLACK_CLI_XOXB"] = "xoxb-xxx"
        os.environ["SLACK_CLI_XAPP"] = "xapp-xxx"

    def teardown_method(self, method):
        os.environ.pop("SLACK_CLI_XOXB", None)
        os.environ.pop("SLACK_CLI_XAPP", None)
        os.environ.pop("SLACK_CLI_CUSTOM_FILE_PATH", None)

    def test_manifest(self, capsys):
        features = ManifestFeaturesSchema(
            app_home=ManifestAppHomeSchema(
                home_tab_enabled=True, messages_tab_enabled=True, messages_tab_read_only_enabled=True
            ),
            bot_user=ManifestBotUserSchema(always_online=False, display_name="Bolt Template App"),
            shortcuts=[
                ManifestShortcutSchema(
                    callback_id="sample_shortcut_id",
                    name="Run sample shortcut",
                    description="Runs a sample shortcut",
                    type=ShortcutType.GLOBAL,
                )
            ],
            slash_commands=[
                ManifestSlashCommandSchema(
                    command="/sample-command", description="Runs a sample command", should_escape=False
                )
            ],
        )
        manifest = Manifest(
            display_information=ManifestDisplayInformationSchema(name="Bolt Template App"),
            metadata=ManifestMetadataSchema(major_version=2, minor_version=2),
            features=features,
            oauth_config=ManifestOauthConfigSchema(
                scopes=Scopes(bot=["channels:history", "chat:write", "commands", "chat:write.public"]),
            ),
            settings=ManifestSettingsSchema(
                event_subscriptions=ManifestEventSubscriptionsSchema(bot_events=["app_home_opened", "message.channels"]),
                interactivity=ManifestInteractivitySchema(is_enabled=True),
                org_deploy_enabled=True,
                socket_mode_enabled=True,
                token_rotation_enabled=False,
            ),
            outgoing_domains=[],
        )
        assert manifest.to_dict() == sample


sample = {
    "metadata": {"major_version": 2, "minor_version": 2},
    "display_information": {"name": "Bolt Template App"},
    "features": {
        "app_home": {"home_tab_enabled": True, "messages_tab_enabled": True, "messages_tab_read_only_enabled": True},
        "bot_user": {"display_name": "Bolt Template App", "always_online": False},
        "shortcuts": [
            {
                "name": "Run sample shortcut",
                "type": "global",
                "callback_id": "sample_shortcut_id",
                "description": "Runs a sample shortcut",
            }
        ],
        "slash_commands": [{"command": "/sample-command", "description": "Runs a sample command", "should_escape": False}],
    },
    "oauth_config": {"scopes": {"bot": ["channels:history", "chat:write", "commands", "chat:write.public"]}},
    "settings": {
        "event_subscriptions": {"bot_events": ["app_home_opened", "message.channels"]},
        "interactivity": {"is_enabled": True},
        "org_deploy_enabled": True,
        "socket_mode_enabled": True,
        "token_rotation_enabled": False,
    },
    "outgoing_domains": [],
}

functions_workflows = {
    "functions": {
        "sample_function": {
            "title": "Sample function",
            "description": "A sample function",
            "input_parameters": {
                "properties": {"message": {"type": "string", "description": "Message to be posted"}},
                "required": ["message"],
            },
            "output_parameters": {
                "properties": {"updatedMsg": {"type": "string", "description": "Updated message to be posted"}},
                "required": ["updatedMsg"],
            },
        },
        "sample_view_function": {
            "title": "Sample view function",
            "description": "A sample function thats uses views",
            "input_parameters": {"properties": {"interactivity": {"type": "slack#/types/interactivity"}}},
            "output_parameters": {
                "properties": {"markdown": {"type": "string", "description": "message to be send to slack"}},
                "required": ["markdown"],
            },
        },
    },
    "types": {},
    "workflows": {
        "sample_workflow": {
            "title": "Sample workflow",
            "description": "A sample workflow",
            "input_parameters": {
                "properties": {
                    "interactivity": {"type": "slack#/types/interactivity"},
                    "channel": {"type": "slack#/types/channel_id"},
                },
                "required": ["interactivity"],
            },
            "steps": [
                {
                    "id": "0",
                    "function_id": "slack#/functions/open_form",
                    "inputs": {
                        "title": "Send message to channel",
                        "submit_label": "Send message",
                        "description": "Send a message to a channel",
                        "interactivity": "{{inputs.interactivity}}",
                        "fields": {
                            "elements": [
                                {"name": "message", "title": "Message", "type": "string", "long": True},
                                {
                                    "name": "channel",
                                    "title": "Channel to send message to",
                                    "type": "slack#/types/channel_id",
                                    "default": "{{inputs.channel}}",
                                },
                            ],
                            "required": ["channel", "message"],
                        },
                    },
                },
                {
                    "id": "1",
                    "function_id": "#/functions/sample_function",
                    "inputs": {"message": "{{steps.0.fields.message}}"},
                },
                {
                    "id": "2",
                    "function_id": "slack#/functions/send_message",
                    "inputs": {"channel_id": "{{steps.0.fields.channel}}", "message": "{{steps.1.updatedMsg}}"},
                },
            ],
        },
        "sample_view_workflow": {
            "title": "Sample view workflow",
            "description": "A sample view workflow",
            "input_parameters": {
                "properties": {
                    "interactivity": {"type": "slack#/types/interactivity"},
                    "channel": {"type": "slack#/types/channel_id"},
                },
                "required": ["interactivity", "channel"],
            },
            "steps": [
                {
                    "id": "0",
                    "function_id": "#/functions/sample_view_function",
                    "inputs": {"interactivity": "{{inputs.interactivity}}"},
                },
                {
                    "id": "1",
                    "function_id": "slack#/functions/send_message",
                    "inputs": {"channel_id": "{{inputs.channel}}", "message": "{{steps.0.markdown}}"},
                },
            ],
        },
    },
}
