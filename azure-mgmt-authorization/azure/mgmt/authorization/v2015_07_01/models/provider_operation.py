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


class ProviderOperation(Model):
    """Operation.

    :param name: The operation name.
    :type name: str
    :param display_name: The operation display name.
    :type display_name: str
    :param description: The operation description.
    :type description: str
    :param origin: The operation origin.
    :type origin: str
    :param properties: The operation properties.
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.origin = kwargs.get('origin', None)
        self.properties = kwargs.get('properties', None)