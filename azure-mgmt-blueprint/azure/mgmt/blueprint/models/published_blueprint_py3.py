# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .azure_resource_base_py3 import AzureResourceBase


class PublishedBlueprint(AzureResourceBase):
    """Represents a published blueprint.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: String Id used to locate any resource on Azure.
    :vartype id: str
    :ivar type: Type of this resource.
    :vartype type: str
    :ivar name: Name of this resource.
    :vartype name: str
    :param display_name: One-liner string explain this resource.
    :type display_name: str
    :param description: Multi-line explain this resource.
    :type description: str
    :ivar status: Status of the blueprint. This field is readonly.
    :vartype status: ~azure.mgmt.blueprint.models.BlueprintStatus
    :param target_scope: The scope where this blueprint definition can be
     assigned. Possible values include: 'subscription', 'managementGroup'
    :type target_scope: str or
     ~azure.mgmt.blueprint.models.BlueprintTargetScope
    :param parameters: Parameters required by this blueprint definition.
    :type parameters: dict[str,
     ~azure.mgmt.blueprint.models.ParameterDefinition]
    :param resource_groups: Resource group placeholders defined by this
     blueprint definition.
    :type resource_groups: dict[str,
     ~azure.mgmt.blueprint.models.ResourceGroupDefinition]
    :param blueprint_name: Name of the published blueprint definition.
    :type blueprint_name: str
    :param change_notes: Version-specific change notes.
    :type change_notes: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'max_length': 256},
        'description': {'max_length': 500},
        'status': {'readonly': True},
        'change_notes': {'max_length': 500},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'BlueprintStatus'},
        'target_scope': {'key': 'properties.targetScope', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': '{ParameterDefinition}'},
        'resource_groups': {'key': 'properties.resourceGroups', 'type': '{ResourceGroupDefinition}'},
        'blueprint_name': {'key': 'properties.blueprintName', 'type': 'str'},
        'change_notes': {'key': 'properties.changeNotes', 'type': 'str'},
    }

    def __init__(self, *, display_name: str=None, description: str=None, target_scope=None, parameters=None, resource_groups=None, blueprint_name: str=None, change_notes: str=None, **kwargs) -> None:
        super(PublishedBlueprint, self).__init__(**kwargs)
        self.display_name = display_name
        self.description = description
        self.status = None
        self.target_scope = target_scope
        self.parameters = parameters
        self.resource_groups = resource_groups
        self.blueprint_name = blueprint_name
        self.change_notes = change_notes
