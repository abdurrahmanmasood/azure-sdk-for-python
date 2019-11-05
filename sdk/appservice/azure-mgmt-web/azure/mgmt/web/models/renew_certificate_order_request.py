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

from .proxy_only_resource import ProxyOnlyResource


class RenewCertificateOrderRequest(ProxyOnlyResource):
    """Class representing certificate renew request.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param key_size: Certificate Key Size.
    :type key_size: int
    :param csr: Csr to be used for re-key operation.
    :type csr: str
    :param is_private_key_external: Should we change the ASC type (from
     managed private key to external private key and vice versa).
    :type is_private_key_external: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'key_size': {'key': 'properties.keySize', 'type': 'int'},
        'csr': {'key': 'properties.csr', 'type': 'str'},
        'is_private_key_external': {'key': 'properties.isPrivateKeyExternal', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(RenewCertificateOrderRequest, self).__init__(**kwargs)
        self.key_size = kwargs.get('key_size', None)
        self.csr = kwargs.get('csr', None)
        self.is_private_key_external = kwargs.get('is_private_key_external', None)