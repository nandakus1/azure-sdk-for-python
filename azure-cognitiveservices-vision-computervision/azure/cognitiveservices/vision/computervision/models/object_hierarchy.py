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


class ObjectHierarchy(Model):
    """An object detected inside an image.

    :param object_property: Label for the object.
    :type object_property: str
    :param confidence: Confidence score of having observed the object in the
     image, as a value ranging from 0 to 1.
    :type confidence: float
    :param parent: The parent object, from a taxonomy perspective.
     The parent object is a more generic form of this object.  For example, a
     'bulldog' would have a parent of 'dog'.
    :type parent:
     ~azure.cognitiveservices.vision.computervision.models.ObjectHierarchy
    """

    _attribute_map = {
        'object_property': {'key': 'object', 'type': 'str'},
        'confidence': {'key': 'confidence', 'type': 'float'},
        'parent': {'key': 'parent', 'type': 'ObjectHierarchy'},
    }

    def __init__(self, **kwargs):
        super(ObjectHierarchy, self).__init__(**kwargs)
        self.object_property = kwargs.get('object_property', None)
        self.confidence = kwargs.get('confidence', None)
        self.parent = kwargs.get('parent', None)