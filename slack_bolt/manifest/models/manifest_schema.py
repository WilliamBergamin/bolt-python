class Schema:
    def keys(self):
        return self.__dict__.keys()

    def get(self, key: str):
        return self.__getattribute__(key)


from typing import Optional, List, Dict, Any, Union
from enum import Enum


class ManifestAppDirectorySchema(Schema):
    app_directory_categories: Optional[List[str]] = None
    direct_install_url: Optional[str] = None
    installation_landing_page: Optional[str] = None
    pricing: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    support_email: Optional[str] = None
    support_url: Optional[str] = None
    supported_languages: Optional[List[str]] = None
    use_direct_install: Optional[bool] = None

    def __init__(
        self,
        app_directory_categories: Optional[List[str]] = None,
        direct_install_url: Optional[str] = None,
        installation_landing_page: Optional[str] = None,
        pricing: Optional[str] = None,
        privacy_policy_url: Optional[str] = None,
        support_email: Optional[str] = None,
        support_url: Optional[str] = None,
        supported_languages: Optional[List[str]] = None,
        use_direct_install: Optional[bool] = None,
    ) -> None:
        self.app_directory_categories = app_directory_categories
        self.direct_install_url = direct_install_url
        self.installation_landing_page = installation_landing_page
        self.pricing = pricing
        self.privacy_policy_url = privacy_policy_url
        self.support_email = support_email
        self.support_url = support_url
        self.supported_languages = supported_languages
        self.use_direct_install = use_direct_install


class Attribute(Schema):
    items: Optional[str] = None
    properties: Optional[Dict[str, str]] = None
    type: str

    def __init__(self, type: str, items: Optional[str] = None, properties: Optional[Dict[str, str]] = None) -> None:
        self.items = items
        self.properties = properties
        self.type = type


class ManifestDatastoreSchema(Schema):
    attributes: Dict[str, Dict[str, Attribute]]
    primary_key: str

    def __init__(self, attributes: Dict[str, Dict[str, Attribute]], primary_key: str) -> None:
        self.attributes = attributes
        self.primary_key = primary_key


class ManifestDisplayInformationSchema(Schema):
    """A group of settings that describe parts of an app's appearance within Slack. If you're
    distributing the app via the App Directory, read our listing guidelines to pick the best
    values for these settings.
    """

    """A string containing a hex color value (including the hex sign) that specifies the
    background color used on hovercards that display information about your app. Can be
    3-digit (#000) or 6-digit (#000000) hex values. Once an app has set a background color
    value, it cannot be removed, only updated.
    """
    background_color: Optional[str] = None
    """A string with a short description of the app for display to users. Maximum length is 140
    characters.
    """
    description: Optional[str] = None
    """A string with a longer version of the description of the app. Maximum length is 4000
    characters
    """
    long_description: Optional[str] = None
    """A string of the name of the app. Maximum length is 35 characters."""
    name: str

    def __init__(
        self,
        name: str,
        background_color: Optional[str] = None,
        description: Optional[str] = None,
        long_description: Optional[str] = None,
    ) -> None:
        self.background_color = background_color
        self.description = description
        self.long_description = long_description
        self.name = name


class ManifestAppHomeSchema(Schema):
    """A subgroup of settings that describe App Home configuration."""

    """A boolean that specifies whether or not the Home tab is enabled."""
    home_tab_enabled: Optional[bool] = None
    """A boolean that specifies whether or not the Messages tab in your App Home is enabled."""
    messages_tab_enabled: Optional[bool] = None
    """A boolean that specifies whether or not the users can send messages to your app in the
    Messages tab of your App Home.
    """
    messages_tab_read_only_enabled: Optional[bool] = None

    def __init__(
        self,
        home_tab_enabled: Optional[bool] = None,
        messages_tab_enabled: Optional[bool] = None,
        messages_tab_read_only_enabled: Optional[bool] = None,
    ) -> None:
        self.home_tab_enabled = home_tab_enabled
        self.messages_tab_enabled = messages_tab_enabled
        self.messages_tab_read_only_enabled = messages_tab_read_only_enabled


class ManifestBotUserSchema(Schema):
    """A subgroup of settings that describe bot user configuration."""

    """A boolean that specifies whether or not the bot user will always appear to be online."""
    always_online: Optional[bool] = None
    """A string containing the display name of the bot user. Maximum length is 80 characters."""
    display_name: str

    def __init__(self, display_name: str, always_online: Optional[bool] = None) -> None:
        self.always_online = always_online
        self.display_name = display_name


class ShortcutType(Enum):
    GLOBAL = "global"
    MESSAGE = "message"


class ManifestShortcutSchema(Schema):
    callback_id: str
    description: str
    name: str
    type: ShortcutType

    def __init__(self, callback_id: str, description: str, name: str, type: ShortcutType) -> None:
        self.callback_id = callback_id
        self.description = description
        self.name = name
        self.type = type


class ManifestSlashCommandSchema(Schema):
    command: str
    description: str
    should_escape: Optional[bool] = None
    url: Optional[str] = None
    usage_hint: Optional[str] = None

    def __init__(
        self,
        command: str,
        description: str,
        should_escape: Optional[bool] = None,
        url: Optional[str] = None,
        usage_hint: Optional[str] = None,
    ) -> None:
        self.command = command
        self.description = description
        self.should_escape = should_escape
        self.url = url
        self.usage_hint = usage_hint


class ManifestWorkflowStepLegacy(Schema):
    callback_id: str
    name: str

    def __init__(self, callback_id: str, name: str) -> None:
        self.callback_id = callback_id
        self.name = name


class ManifestFeaturesSchema(Schema):
    """A group of settings corresponding to the Features section of the app config pages."""

    """A subgroup of settings that describe App Home configuration."""
    app_home: Optional[ManifestAppHomeSchema] = None
    """A subgroup of settings that describe bot user configuration."""
    bot_user: Optional[ManifestBotUserSchema] = None
    shortcuts: Optional[List[ManifestShortcutSchema]] = None
    slash_commands: Optional[List[ManifestSlashCommandSchema]] = None
    unfurl_domains: Optional[List[str]] = None
    workflow_steps: Optional[List[ManifestWorkflowStepLegacy]] = None

    def __init__(
        self,
        app_home: Optional[ManifestAppHomeSchema] = None,
        bot_user: Optional[ManifestBotUserSchema] = None,
        shortcuts: Optional[List[ManifestShortcutSchema]] = None,
        slash_commands: Optional[List[ManifestSlashCommandSchema]] = None,
        unfurl_domains: Optional[List[str]] = None,
        workflow_steps: Optional[List[ManifestWorkflowStepLegacy]] = None,
    ) -> None:
        self.app_home = app_home
        self.bot_user = bot_user
        self.shortcuts = shortcuts
        self.slash_commands = slash_commands
        self.unfurl_domains = unfurl_domains
        self.workflow_steps = workflow_steps


class ParameterDefinition(Schema):
    description: Optional[str] = None
    is_required: Optional[bool] = None
    title: Optional[str] = None
    type: str

    def __init__(
        self, type: str, description: Optional[str] = None, is_required: Optional[bool] = None, title: Optional[str] = None
    ) -> None:
        self.description = description
        self.is_required = is_required
        self.title = title
        self.type = type


class ManifestParameters(Schema):
    properties: Dict[str, ParameterDefinition]
    required: Optional[List[str]] = None

    def __init__(self, properties: Dict[str, ParameterDefinition], required: Optional[List[str]] = None) -> None:
        self.properties = properties
        self.required = required


class ManifestFunctionSchema(Schema):
    description: str
    input_parameters: ManifestParameters
    output_parameters: ManifestParameters
    title: str

    def __init__(
        self, description: str, input_parameters: ManifestParameters, output_parameters: ManifestParameters, title: str
    ) -> None:
        self.description = description
        self.input_parameters = input_parameters
        self.output_parameters = output_parameters
        self.title = title


class ManifestMetadataSchema(Schema):
    """A group of settings that describe the manifest"""

    """An integer that specifies the major version of the manifest schema to target."""
    major_version: Optional[float] = None
    """An integer that specifies the minor version of the manifest schema to target."""
    minor_version: Optional[float] = None

    def __init__(self, major_version: Optional[float] = None, minor_version: Optional[float] = None) -> None:
        self.major_version = major_version
        self.minor_version = minor_version


class Scopes(Schema):
    """A subgroup of settings that describe permission scopes configuration."""

    """An array of strings containing bot scopes to request upon app installation. A maximum of
    255 scopes can included in this array.
    """
    bot: Optional[List[str]] = None
    """An array of strings containing user scopes to request upon app installation. A maximum of
    255 scopes can included in this array.
    """
    user: Optional[List[str]] = None

    def __init__(self, bot: Optional[List[str]] = None, user: Optional[List[str]] = None) -> None:
        self.bot = bot
        self.user = user


class ManifestOauthConfigSchema(Schema):
    """A group of settings describing OAuth configuration for the app."""

    """An array of strings containing OAuth redirect URLs. A maximum of 1000 redirect URLs can
    be included in this array.
    """
    redirect_urls: Optional[List[str]] = None
    """A subgroup of settings that describe permission scopes configuration."""
    scopes: Scopes
    token_management_enabled: Optional[bool] = None

    def __init__(
        self, scopes: Scopes, redirect_urls: Optional[List[str]] = None, token_management_enabled: Optional[bool] = None
    ) -> None:
        self.redirect_urls = redirect_urls
        self.scopes = scopes
        self.token_management_enabled = token_management_enabled


class MetadataSubscription(Schema):
    app_id: Optional[str] = None
    event_type: Optional[str] = None

    def __init__(self, app_id: Optional[str] = None, event_type: Optional[str] = None) -> None:
        self.app_id = app_id
        self.event_type = event_type


class ManifestEventSubscriptionsSchema(Schema):
    """A subgroup of settings that describe Events API configuration for the app."""

    """An array of strings matching the event types you want to the app to subscribe to. A
    maximum of 100 event types can be used.
    """
    bot_events: Optional[List[str]] = None
    metadata_subscriptions: Optional[List[MetadataSubscription]] = None
    """A string containing the full https URL that acts as the Events API request URL. If set,
    you'll need to manually verify the Request URL in the App Manifest section of App
    Management.
    """
    request_url: Optional[str] = None
    """An array of strings matching the event types you want to the app to subscribe to on
    behalf of authorized users. A maximum of 100 event types can be used.
    """
    user_events: Optional[List[str]] = None

    def __init__(
        self,
        bot_events: Optional[List[str]] = None,
        metadata_subscriptions: Optional[List[MetadataSubscription]] = None,
        request_url: Optional[str] = None,
        user_events: Optional[List[str]] = None,
    ) -> None:
        self.bot_events = bot_events
        self.metadata_subscriptions = metadata_subscriptions
        self.request_url = request_url
        self.user_events = user_events


class ManifestFunctionRuntime(Enum):
    LOCAL = "local"
    REMOTE = "remote"
    SLACK = "slack"


class ManifestIncomingWebhooks(Schema):
    incoming_webhooks_enabled: Optional[bool] = None

    def __init__(self, incoming_webhooks_enabled: Optional[bool] = None) -> None:
        self.incoming_webhooks_enabled = incoming_webhooks_enabled


class ManifestInteractivitySchema(Schema):
    """A subgroup of settings that describe interactivity configuration for the app."""

    """A boolean that specifies whether or not interactivity features are enabled."""
    is_enabled: bool
    """A string containing the full https URL that acts as the interactive Options Load URL."""
    message_menu_options_url: Optional[str] = None
    """A string containing the full https URL that acts as the interactive Request URL."""
    request_url: Optional[str] = None

    def __init__(
        self, is_enabled: bool, message_menu_options_url: Optional[str] = None, request_url: Optional[str] = None
    ) -> None:
        self.is_enabled = is_enabled
        self.message_menu_options_url = message_menu_options_url
        self.request_url = request_url


class ManifestSiwsLinksSchema(Schema):
    initiate_uri: Optional[str] = None

    def __init__(self, initiate_uri: Optional[str] = None) -> None:
        self.initiate_uri = initiate_uri


class ManifestSettingsSchema(Schema):
    """A group of settings corresponding to the Settings section of the app config pages."""

    """An array of strings that contain IP addresses that conform to the Allowed IP Ranges
    feature
    """
    allowed_ip_address_ranges: Optional[List[str]] = None
    """A subgroup of settings that describe Events API configuration for the app."""
    event_subscriptions: Optional[ManifestEventSubscriptionsSchema] = None
    function_runtime: Optional[ManifestFunctionRuntime] = None
    incoming_webhooks: Optional[ManifestIncomingWebhooks] = None
    interactivity: Optional[ManifestInteractivitySchema] = None
    """A boolean that specifies whether or not org-wide deploy is enabled."""
    org_deploy_enabled: Optional[bool] = None
    siws_links: Optional[ManifestSiwsLinksSchema] = None
    """A boolean that specifies whether or not Socket Mode is enabled."""
    socket_mode_enabled: Optional[bool] = None
    token_rotation_enabled: Optional[bool] = None

    def __init__(
        self,
        allowed_ip_address_ranges: Optional[List[str]] = None,
        event_subscriptions: Optional[ManifestEventSubscriptionsSchema] = None,
        function_runtime: Optional[ManifestFunctionRuntime] = None,
        incoming_webhooks: Optional[ManifestIncomingWebhooks] = None,
        interactivity: Optional[ManifestInteractivitySchema] = None,
        org_deploy_enabled: Optional[bool] = None,
        siws_links: Optional[ManifestSiwsLinksSchema] = None,
        socket_mode_enabled: Optional[bool] = None,
        token_rotation_enabled: Optional[bool] = None,
    ) -> None:
        self.allowed_ip_address_ranges = allowed_ip_address_ranges
        self.event_subscriptions = event_subscriptions
        self.function_runtime = function_runtime
        self.incoming_webhooks = incoming_webhooks
        self.interactivity = interactivity
        self.org_deploy_enabled = org_deploy_enabled
        self.siws_links = siws_links
        self.socket_mode_enabled = socket_mode_enabled
        self.token_rotation_enabled = token_rotation_enabled


class StepType(Enum):
    CONDITIONAL = "conditional"
    FUNCTION = "function"
    SWITCH = "switch"


class ManifestWorkflowStepSchema(Schema):
    function_id: str
    id: str
    inputs: Dict[str, Union[List[Any], bool, float, Dict[str, Any], str]]
    type: Optional[StepType] = None

    def __init__(
        self,
        function_id: str,
        id: str,
        inputs: Dict[str, Union[List[Any], bool, float, Dict[str, Any], str]],
        type: Optional[StepType] = None,
    ) -> None:
        self.function_id = function_id
        self.id = id
        self.inputs = inputs
        self.type = type


class ManifestWorkflowSchema(Schema):
    description: Optional[str] = None
    input_parameters: Optional[ManifestParameters] = None
    steps: List[ManifestWorkflowStepSchema]
    title: Optional[str] = None

    def __init__(
        self,
        steps: List[ManifestWorkflowStepSchema],
        description: Optional[str] = None,
        input_parameters: Optional[ManifestParameters] = None,
        title: Optional[str] = None,
    ) -> None:
        self.description = description
        self.input_parameters = input_parameters
        self.steps = steps
        self.title = title


class ManifestSchema(Schema):
    """A group of settings that describe the manifest"""

    metadata: Optional[ManifestMetadataSchema] = None
    app_directory: Optional[ManifestAppDirectorySchema] = None
    datastores: Optional[Dict[str, ManifestDatastoreSchema]] = None
    """A group of settings that describe parts of an app's appearance within Slack. If you're
    distributing the app via the App Directory, read our listing guidelines to pick the best
    values for these settings.
    """
    display_information: ManifestDisplayInformationSchema
    """A group of settings corresponding to the Features section of the app config pages."""
    features: Optional[ManifestFeaturesSchema] = None
    functions: Optional[Dict[str, ManifestFunctionSchema]] = None
    """A group of settings describing OAuth configuration for the app."""
    oauth_config: Optional[ManifestOauthConfigSchema] = None
    outgoing_domains: Optional[List[str]] = None
    """A group of settings corresponding to the Settings section of the app config pages."""
    settings: Optional[ManifestSettingsSchema] = None
    types: Optional[List[ManifestParameters]] = None
    workflows: Optional[Dict[str, ManifestWorkflowSchema]] = None

    def __init__(
        self,
        display_information: ManifestDisplayInformationSchema,
        metadata: Optional[ManifestMetadataSchema] = None,
        app_directory: Optional[ManifestAppDirectorySchema] = None,
        datastores: Optional[Dict[str, ManifestDatastoreSchema]] = None,
        features: Optional[ManifestFeaturesSchema] = None,
        functions: Optional[Dict[str, ManifestFunctionSchema]] = None,
        oauth_config: Optional[ManifestOauthConfigSchema] = None,
        outgoing_domains: Optional[List[str]] = None,
        settings: Optional[ManifestSettingsSchema] = None,
        types: Optional[List[ManifestParameters]] = None,
        workflows: Optional[Dict[str, ManifestWorkflowSchema]] = None,
    ) -> None:
        self.metadata = metadata
        self.app_directory = app_directory
        self.datastores = datastores
        self.display_information = display_information
        self.features = features
        self.functions = functions
        self.oauth_config = oauth_config
        self.outgoing_domains = outgoing_domains
        self.settings = settings
        self.types = types
        self.workflows = workflows
