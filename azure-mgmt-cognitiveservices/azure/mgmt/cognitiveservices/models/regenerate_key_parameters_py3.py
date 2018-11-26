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


class RegenerateKeyParameters(Model):
    """Regenerate key parameters.

    :param key_name: key name to generate (Key1|Key2). Possible values
     include: 'Key1', 'Key2'
    :type key_name: str or ~azure.mgmt.cognitiveservices.models.KeyName
    """

    _attribute_map = {
        'key_name': {'key': 'keyName', 'type': 'KeyName'},
    }

    def __init__(self, *, key_name=None, **kwargs) -> None:
        super(RegenerateKeyParameters, self).__init__(**kwargs)
        self.key_name = key_name
