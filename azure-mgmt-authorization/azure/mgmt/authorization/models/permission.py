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


class Permission(Model):
    """Role definition permissions.

    :param actions: Allowed actions.
    :type actions: list of str
    :param not_actions: Denied actions.
    :type not_actions: list of str
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'not_actions': {'key': 'notActions', 'type': '[str]'},
    }

    def __init__(self, actions=None, not_actions=None):
        self.actions = actions
        self.not_actions = not_actions