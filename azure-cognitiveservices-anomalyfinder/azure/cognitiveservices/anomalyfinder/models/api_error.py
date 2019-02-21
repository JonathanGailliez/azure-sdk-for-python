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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class APIError(Model):
    """Error information returned by the API.

    :param code: The error code.
    :type code: object
    :param message: A message explaining the error reported by the service.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'object'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(APIError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class APIErrorException(HttpOperationError):
    """Server responsed with exception of type: 'APIError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(APIErrorException, self).__init__(deserialize, response, 'APIError', *args)
