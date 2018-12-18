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


class ImageTagRegion(Model):
    """Defines an image region relevant to the ImageTag.

    All required parameters must be populated in order to send to Azure.

    :param query_rectangle: Required. A rectangle that outlines the area of
     interest for this tag.
    :type query_rectangle:
     ~azure.cognitiveservices.search.visualsearch.models.NormalizedQuadrilateral
    :param display_rectangle: Required. A recommended rectangle to show to the
     user.
    :type display_rectangle:
     ~azure.cognitiveservices.search.visualsearch.models.NormalizedQuadrilateral
    """

    _validation = {
        'query_rectangle': {'required': True},
        'display_rectangle': {'required': True},
    }

    _attribute_map = {
        'query_rectangle': {'key': 'queryRectangle', 'type': 'NormalizedQuadrilateral'},
        'display_rectangle': {'key': 'displayRectangle', 'type': 'NormalizedQuadrilateral'},
    }

    def __init__(self, **kwargs):
        super(ImageTagRegion, self).__init__(**kwargs)
        self.query_rectangle = kwargs.get('query_rectangle', None)
        self.display_rectangle = kwargs.get('display_rectangle', None)
