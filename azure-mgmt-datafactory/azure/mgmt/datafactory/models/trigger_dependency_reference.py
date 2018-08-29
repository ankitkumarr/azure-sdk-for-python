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

from .dependency_reference import DependencyReference


class TriggerDependencyReference(DependencyReference):
    """Trigger referenced dependency.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: TumblingWindowTriggerDependencyReference

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param reference_trigger: Required. Referenced trigger.
    :type reference_trigger: ~azure.mgmt.datafactory.models.TriggerReference
    """

    _validation = {
        'type': {'required': True},
        'reference_trigger': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'reference_trigger': {'key': 'referenceTrigger', 'type': 'TriggerReference'},
    }

    _subtype_map = {
        'type': {'TumblingWindowTriggerDependencyReference': 'TumblingWindowTriggerDependencyReference'}
    }

    def __init__(self, **kwargs):
        super(TriggerDependencyReference, self).__init__(**kwargs)
        self.reference_trigger = kwargs.get('reference_trigger', None)
        self.type = 'TriggerDependencyReference'
