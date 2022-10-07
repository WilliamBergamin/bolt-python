import json

from slack_bolt.manifest.manifest import FunctionDefinition, Manifest, WorkflowDefinition
from slack_bolt.manifest.models.manifest_schema import (
    ManifestAppHomeSchema,
    ManifestBotUserSchema,
    ManifestDisplayInformationSchema,
    ManifestEventSubscriptionsSchema,
    ManifestFeaturesSchema,
    ManifestInteractivitySchema,
    ManifestMetadataSchema,
    ManifestOauthConfigSchema,
    ManifestParameters,
    ManifestSettingsSchema,
    ManifestShortcutSchema,
    ManifestSlashCommandSchema,
    ManifestWorkflowSchema,
    ManifestWorkflowStepSchema,
    ParameterDefinition,
    Scopes,
    ShortcutType,
)


class TestManifest:
    def test_manifest(self):
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
        assert manifest.to_dict() == sample_base_manifest

    def test_manifest_with_workflow(self):
        func = FunctionDefinition(
            callback_id="sample_function",
            description="A sample function",
            input_parameters=ManifestParameters(
                properties={"message": ParameterDefinition(type="string", description="Message to be posted")},
                required=["message"],
            ),
            output_parameters=ManifestParameters(
                properties={"updatedMsg": ParameterDefinition(type="string", description="Updated message to be posted")},
                required=["updatedMsg"],
            ),
            title="Sample function",
        )
        workflow = WorkflowDefinition(
            callback_id="sample_workflow",
            description="A sample workflow",
            input_parameters=ManifestParameters(
                {
                    "interactivity": ParameterDefinition(type="slack#/types/interactivity"),
                    "channel": ParameterDefinition(type="slack#/types/channel_id"),
                },
                required=["interactivity"],
            ),
            title="Sample workflow",
        )

        workflow.append_step(
            ManifestWorkflowStepSchema(
                function_id="slack#/functions/open_form",
                id="0",
                inputs={
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
            )
        )

        workflow.append_step(func, inputs={"message": "{{steps.0.fields.message}}"})

        workflow.append_step(
            ManifestWorkflowStepSchema(
                function_id="slack#/functions/send_message",
                id="0",
                inputs={"channel_id": "{{steps.0.fields.channel}}", "message": "{{steps.1.updatedMsg}}"},
            )
        )
        
        manifest = Manifest(
            display_information=ManifestDisplayInformationSchema(name="Bolt Template App"),
            metadata=ManifestMetadataSchema(major_version=2, minor_version=2),
            features=ManifestFeaturesSchema(
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
            ),
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
            workflows=[workflow],
        )
        assert manifest.to_dict() == {**sample_base_manifest, **sample_functions, **sample_workflows}


sample_base_manifest = {
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

sample_functions = {
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
        }
    },
}

sample_workflows = {
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
                    "type": "function",
                },
                {
                    "id": "2",
                    "function_id": "slack#/functions/send_message",
                    "inputs": {"channel_id": "{{steps.0.fields.channel}}", "message": "{{steps.1.updatedMsg}}"},
                },
            ],
        }
    },
}
