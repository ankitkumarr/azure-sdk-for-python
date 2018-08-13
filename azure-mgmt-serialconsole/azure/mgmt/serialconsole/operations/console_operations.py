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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ConsoleOperations(object):
    """ConsoleOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2018-05-01".
    :ivar default: Default string modeled as parameter for URL to work correctly. Constant value: "default".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-05-01"
        self.default = "default"

        self.config = config

    def enable_console(
            self, custom_headers=None, raw=False, **operation_config):
        """Enables Serial Console for a VM.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SetDisabledResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.serialconsole.models.SetDisabledResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`DeploymentValidateResultException<azure.mgmt.serialconsole.models.DeploymentValidateResultException>`
        """
        # Construct URL
        url = self.enable_console.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'default': self._serialize.url("self.default", self.default, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.DeploymentValidateResultException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SetDisabledResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    enable_console.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/providers/consoleServices/{default}/enableConsole'}

    def disable_console(
            self, custom_headers=None, raw=False, **operation_config):
        """Disables Serial Console for a VM.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SetDisabledResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.serialconsole.models.SetDisabledResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`DeploymentValidateResultException<azure.mgmt.serialconsole.models.DeploymentValidateResultException>`
        """
        # Construct URL
        url = self.disable_console.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'default': self._serialize.url("self.default", self.default, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.DeploymentValidateResultException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SetDisabledResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    disable_console.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/providers/consoleServices/{default}/disableConsole'}
