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

from .sub_resource import SubResource


class ServiceEndpointPolicyDefinition(SubResource):
    """Service Endpoint policy definitions.

    :param id: Resource ID.
    :type id: str
    :param description: A description for this rule. Restricted to 140 chars.
    :type description: str
    :param service: service endpoint name.
    :type service: str
    :param service_resources: A list of service resources.
    :type service_resources: list[str]
    :param provisioning_state: The provisioning state of the service end point
     policy definition. Possible values are: 'Updating', 'Deleting', and
     'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'service': {'key': 'properties.service', 'type': 'str'},
        'service_resources': {'key': 'properties.serviceResources', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceEndpointPolicyDefinition, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.service = kwargs.get('service', None)
        self.service_resources = kwargs.get('service_resources', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.name = kwargs.get('name', None)
        self.etag = kwargs.get('etag', None)