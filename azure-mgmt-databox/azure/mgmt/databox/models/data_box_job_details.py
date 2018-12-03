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

from .job_details import JobDetails


class DataBoxJobDetails(JobDetails):
    """DataBox Job Details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param expected_data_size_in_tera_bytes: The expected size of the data,
     which needs to be transferred in this job, in terabytes.
    :type expected_data_size_in_tera_bytes: int
    :ivar job_stages: List of stages that run in the job.
    :vartype job_stages: list[~azure.mgmt.databox.models.JobStages]
    :param contact_details: Required. Contact details for notification and
     shipping.
    :type contact_details: ~azure.mgmt.databox.models.ContactDetails
    :param shipping_address: Required. Shipping address of the customer.
    :type shipping_address: ~azure.mgmt.databox.models.ShippingAddress
    :ivar delivery_package: Delivery package shipping details.
    :vartype delivery_package:
     ~azure.mgmt.databox.models.PackageShippingDetails
    :ivar return_package: Return package shipping details.
    :vartype return_package: ~azure.mgmt.databox.models.PackageShippingDetails
    :param destination_account_details: Required. Destination account details.
    :type destination_account_details:
     list[~azure.mgmt.databox.models.DestinationAccountDetails]
    :ivar error_details: Error details for failure. This is optional.
    :vartype error_details: list[~azure.mgmt.databox.models.JobErrorDetails]
    :param preferences: Preferences for the order.
    :type preferences: ~azure.mgmt.databox.models.Preferences
    :ivar copy_log_details: List of copy log details.
    :vartype copy_log_details: list[~azure.mgmt.databox.models.CopyLogDetails]
    :ivar reverse_shipment_label_sas_key: Shared access key to download the
     return shipment label
    :vartype reverse_shipment_label_sas_key: str
    :ivar chain_of_custody_sas_key: Shared access key to download the chain of
     custody logs
    :vartype chain_of_custody_sas_key: str
    :param job_details_type: Required. Constant filled by server.
    :type job_details_type: str
    :ivar copy_progress: Copy progress per storage account.
    :vartype copy_progress: list[~azure.mgmt.databox.models.CopyProgress]
    """

    _validation = {
        'job_stages': {'readonly': True},
        'contact_details': {'required': True},
        'shipping_address': {'required': True},
        'delivery_package': {'readonly': True},
        'return_package': {'readonly': True},
        'destination_account_details': {'required': True},
        'error_details': {'readonly': True},
        'copy_log_details': {'readonly': True},
        'reverse_shipment_label_sas_key': {'readonly': True},
        'chain_of_custody_sas_key': {'readonly': True},
        'job_details_type': {'required': True},
        'copy_progress': {'readonly': True},
    }

    _attribute_map = {
        'expected_data_size_in_tera_bytes': {'key': 'expectedDataSizeInTeraBytes', 'type': 'int'},
        'job_stages': {'key': 'jobStages', 'type': '[JobStages]'},
        'contact_details': {'key': 'contactDetails', 'type': 'ContactDetails'},
        'shipping_address': {'key': 'shippingAddress', 'type': 'ShippingAddress'},
        'delivery_package': {'key': 'deliveryPackage', 'type': 'PackageShippingDetails'},
        'return_package': {'key': 'returnPackage', 'type': 'PackageShippingDetails'},
        'destination_account_details': {'key': 'destinationAccountDetails', 'type': '[DestinationAccountDetails]'},
        'error_details': {'key': 'errorDetails', 'type': '[JobErrorDetails]'},
        'preferences': {'key': 'preferences', 'type': 'Preferences'},
        'copy_log_details': {'key': 'copyLogDetails', 'type': '[CopyLogDetails]'},
        'reverse_shipment_label_sas_key': {'key': 'reverseShipmentLabelSasKey', 'type': 'str'},
        'chain_of_custody_sas_key': {'key': 'chainOfCustodySasKey', 'type': 'str'},
        'job_details_type': {'key': 'jobDetailsType', 'type': 'str'},
        'copy_progress': {'key': 'copyProgress', 'type': '[CopyProgress]'},
    }

    def __init__(self, **kwargs):
        super(DataBoxJobDetails, self).__init__(**kwargs)
        self.copy_progress = None
        self.job_details_type = 'DataBox'
