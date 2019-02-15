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


class NetworkInterfaceProperties(Model):
    """Properties of a network interface.

    :param virtual_network_id: The resource ID of the virtual network.
    :type virtual_network_id: str
    :param subnet_id: The resource ID of the sub net.
    :type subnet_id: str
    :param public_ip_address_id: The resource ID of the public IP address.
    :type public_ip_address_id: str
    :param public_ip_address: The public IP address.
    :type public_ip_address: str
    :param private_ip_address: The private IP address.
    :type private_ip_address: str
    :param dns_name: The DNS name.
    :type dns_name: str
    :param rdp_authority: The RdpAuthority property is a server DNS host name
     or IP address followed by the service port number for RDP (Remote Desktop
     Protocol).
    :type rdp_authority: str
    :param ssh_authority: The SshAuthority property is a server DNS host name
     or IP address followed by the service port number for SSH.
    :type ssh_authority: str
    :param shared_public_ip_address_configuration: The configuration for
     sharing a public IP address across multiple virtual machines.
    :type shared_public_ip_address_configuration:
     ~azure.mgmt.devtestlabs.models.SharedPublicIpAddressConfiguration
    """

    _attribute_map = {
        'virtual_network_id': {'key': 'virtualNetworkId', 'type': 'str'},
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
        'public_ip_address_id': {'key': 'publicIpAddressId', 'type': 'str'},
        'public_ip_address': {'key': 'publicIpAddress', 'type': 'str'},
        'private_ip_address': {'key': 'privateIpAddress', 'type': 'str'},
        'dns_name': {'key': 'dnsName', 'type': 'str'},
        'rdp_authority': {'key': 'rdpAuthority', 'type': 'str'},
        'ssh_authority': {'key': 'sshAuthority', 'type': 'str'},
        'shared_public_ip_address_configuration': {'key': 'sharedPublicIpAddressConfiguration', 'type': 'SharedPublicIpAddressConfiguration'},
    }

    def __init__(self, **kwargs):
        super(NetworkInterfaceProperties, self).__init__(**kwargs)
        self.virtual_network_id = kwargs.get('virtual_network_id', None)
        self.subnet_id = kwargs.get('subnet_id', None)
        self.public_ip_address_id = kwargs.get('public_ip_address_id', None)
        self.public_ip_address = kwargs.get('public_ip_address', None)
        self.private_ip_address = kwargs.get('private_ip_address', None)
        self.dns_name = kwargs.get('dns_name', None)
        self.rdp_authority = kwargs.get('rdp_authority', None)
        self.ssh_authority = kwargs.get('ssh_authority', None)
        self.shared_public_ip_address_configuration = kwargs.get('shared_public_ip_address_configuration', None)
