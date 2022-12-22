# Copyright 2017-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_lib_rest_client.client import BaseClient


class Client(BaseClient):

    namespace = 'wazo_market_client.commands'

    def __init__(
        self, host='apps.wazo.community', port=None, version='v1', https=False, **kwargs
    ):
        super().__init__(host=host, port=port, version=version, https=https, **kwargs)
