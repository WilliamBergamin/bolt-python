from readline import insert_text
from typing import Optional, List, Dict, Union
from enum import Enum

from .models.manifest_schema import (
    ManifestMetadataSchema,
    ManifestAppDirectorySchema,
    ManifestDatastoreSchema,
    ManifestDisplayInformationSchema,
    ManifestFeaturesSchema,
    ManifestOauthConfigSchema,
    ManifestSettingsSchema,
    ManifestParameters,
    ManifestWorkflowStepSchema,
    ManifestFunctionSchema,
    ManifestWorkflowSchema,
    ManifestSchema,
    StepType,
    Schema,
)


class FunctionDefinition:
    def __init__(
        self,
        callback_id: str,
        description: str,
        input_parameters: ManifestParameters,
        output_parameters: ManifestParameters,
        title: str,
    ) -> None:
        self.callback_id = callback_id
        self.description = description
        self.input_parameters = input_parameters
        self.output_parameters = output_parameters
        self.title = title

    def to_manifest_function_schema(self) -> ManifestFunctionSchema:
        return ManifestFunctionSchema(
            description=self.description,
            input_parameters=self.input_parameters,
            output_parameters=self.output_parameters,
            title=self.title,
        )


class WorkflowStepDefinition:
    function_id: str
    type: Optional[StepType] = None

    def __init__(
        self,
        function_id: str,
        type: Optional[StepType] = None,
    ) -> None:
        self.function_id = function_id
        self.type = type


class WorkflowDefinition:

    _steps: List[ManifestWorkflowStepSchema] = []
    _functions: List[FunctionDefinition] = []

    def __init__(
        self,
        callback_id: str,
        description: Optional[str] = None,
        input_parameters: Optional[ManifestParameters] = None,
        title: Optional[str] = None,
    ) -> None:
        self.callback_id = callback_id
        self.description = description
        self.input_parameters = input_parameters
        self.title = title

    def _append_function_definition_step(self, function: FunctionDefinition, inputs: Optional[Dict] = {}):
        self._steps.append(
            ManifestWorkflowStepSchema(
                function_id=f"#/functions/{function.callback_id}", id=None, inputs=inputs, type=StepType.FUNCTION
            )
        )
        self._functions.append(function)

    def append_step(self, function: Union[WorkflowStepDefinition, FunctionDefinition], inputs: Optional[Dict]):
        if isinstance(function, WorkflowStepDefinition):
            self._steps.append(
                ManifestWorkflowStepSchema(function_id=function.function_id, id=None, inputs=inputs, type=function.type)
            )
        elif isinstance(function, FunctionDefinition):
            self._append_function_definition_step(function, inputs)

    def _set_step_ids(self) -> None:
        for index, step in enumerate(self._steps):
            step.id = str(index)

    def to_manifest_workflow_schema(self) -> ManifestWorkflowSchema:
        self._set_step_ids()
        return ManifestWorkflowSchema(
            description=self.description, input_parameters=self.input_parameters, steps=self._steps, title=self.title
        )


class Manifest:
    def __init__(
        self,
        display_information: ManifestDisplayInformationSchema,
        metadata: Optional[ManifestMetadataSchema] = None,
        app_directory: Optional[ManifestAppDirectorySchema] = None,
        datastores: Optional[Dict[str, ManifestDatastoreSchema]] = None,
        features: Optional[ManifestFeaturesSchema] = None,
        oauth_config: Optional[ManifestOauthConfigSchema] = None,
        outgoing_domains: Optional[List[str]] = [],
        settings: Optional[ManifestSettingsSchema] = None,
        types: Optional[List[ManifestParameters]] = None,
        workflows: List[WorkflowDefinition] = [],
    ) -> None:
        self.metadata = metadata
        self.app_directory = app_directory
        self.datastores = datastores
        self.display_information = display_information
        self.features = features
        self.oauth_config = oauth_config
        self.outgoing_domains = outgoing_domains
        self.settings = settings
        self.types = types
        self.workflows = workflows

    def to_dict(self) -> Dict:
        defined_functions = [func for workflow in self.workflows for func in workflow._functions]
        functions = (
            {func.callback_id: func.to_manifest_function_schema() for func in defined_functions}
            if defined_functions
            else None
        )
        workflows = (
            {workflow.callback_id: workflow.to_manifest_workflow_schema() for workflow in self.workflows}
            if self.workflows
            else None
        )

        manifest = ManifestSchema(
            display_information=self.display_information,
            metadata=self.metadata,
            app_directory=self.app_directory,
            datastores=self.datastores,
            features=self.features,
            oauth_config=self.oauth_config,
            outgoing_domains=self.outgoing_domains,
            settings=self.settings,
            types=self.types,
            workflows=workflows,
            functions=functions,
        )
        return _to_dict(manifest)


def _to_dict(obj: Union[Schema, Dict, List, Enum, int, float, str, bool]) -> Dict:

    if isinstance(obj, (int, float, str, bool)):
        return obj
    elif isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, list):
        return [_to_dict(item) for item in obj]

    return {key: _to_dict(obj.get(key)) for key in obj.keys() if obj.get(key) is not None}
