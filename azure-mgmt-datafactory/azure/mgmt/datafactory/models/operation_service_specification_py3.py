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


class OperationServiceSpecification(Model):
    """Details about a service operation.

    :param log_specifications: Details about operations related to logs.
    :type log_specifications:
     list[~azure.mgmt.datafactory.models.OperationLogSpecification]
    :param metric_specifications: Details about operations related to metrics.
    :type metric_specifications:
     list[~azure.mgmt.datafactory.models.OperationMetricSpecification]
    """

    _attribute_map = {
        'log_specifications': {'key': 'logSpecifications', 'type': '[OperationLogSpecification]'},
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[OperationMetricSpecification]'},
    }

    def __init__(self, *, log_specifications=None, metric_specifications=None, **kwargs) -> None:
        super(OperationServiceSpecification, self).__init__(**kwargs)
        self.log_specifications = log_specifications
        self.metric_specifications = metric_specifications
