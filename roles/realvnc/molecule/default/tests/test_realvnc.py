#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from os import environ
from os import path

from jinja2 import Template
from testinfra import get_host
from testinfra.utils import ansible_runner

logging.basicConfig(level=logging.DEBUG)

testinfra_hosts = ansible_runner.AnsibleRunner(
    environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    pkg = host.package('xserver-xorg-video-dummy')
    assert pkg.is_installed
    pkg = host.package('realvnc-vnc-server')
    assert pkg.is_installed


def test_config(host):
    log = logging.getLogger('test_config')
    local = get_host("local://")
    res_path = path.join('templates', 'etc', 'vnc', 'config.d', 'vncserver-virtual.j2')
    example = local.file(res_path).content_string
    values = dict(
        use_system_xorg=1
    )
    example = Template(example, keep_trailing_newline=True).render(values)
    remote_file = host.file('/etc/vnc/config.d/vncserver-virtual')
    assert remote_file.exists
    content = remote_file.content_string
    assert example == content
    # log.debug(content)
