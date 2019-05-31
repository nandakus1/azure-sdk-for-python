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


class ApplicationGetEndpoint(Model):
    """Gets the application SSH endpoint.

    :param location: The location of the endpoint.
    :type location: str
    :param destination_port: The destination port to connect to.
    :type destination_port: int
    :param public_port: The public port to connect to.
    :type public_port: int
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'destination_port': {'key': 'destinationPort', 'type': 'int'},
        'public_port': {'key': 'publicPort', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGetEndpoint, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.destination_port = kwargs.get('destination_port', None)
        self.public_port = kwargs.get('public_port', None)