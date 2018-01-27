#! /usr/bin/env python
#
# Mixpanel, Inc. -- http://mixpanel.com/
#
# Python API client library to consume mixpanel.com analytics data.
#
# Copyright 2010-2013 Mixpanel, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import json
import requests


class Mixpanel(object):

    VERSION = '2.0'
    ENDPOINT = 'https://mixpanel.com/api'

    def __init__(self, api_secret):
        self.api_secret = api_secret

    def request(self, methods, params, format='json'):
        """
            methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
                      will give us http://mixpanel.com/api/2.0/events/properties/values/
            params - Extra parameters associated with method
        """
        params['format'] = format

        request_url = '/'.join([self.ENDPOINT, self.VERSION] + methods)
        encoded_params = self.encode_params(params)

        request = requests.get(
            request_url,
            params=encoded_params,
            auth=requests.auth.HTTPBasicAuth(self.api_secret, ''),
        )
        return request.json()

    def encode_params(self, params):
        if isinstance(params, dict):
            params = list(params.items())

        for i, param in enumerate(params):
            if isinstance(param[1], list):
                params[i] = (param[0], json.dumps(param[1]),)

        return params
