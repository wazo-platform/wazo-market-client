#!/usr/bin/env python3
# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages, setup

setup(
    name='wazo_market_client',
    version='0.1',
    description='a simple client library for the wazo-market',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_market_client.commands': [
            'plugins = wazo_market_client.commands:PluginCommand',
        ],
    },
)
