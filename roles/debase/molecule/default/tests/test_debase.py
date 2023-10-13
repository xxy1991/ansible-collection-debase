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


def test_blacklist_floppy(host):
    log = logging.getLogger('test_blacklist_floppy')
    local = get_host("local://")
    res_path = path.join('files', 'etc', 'modprobe.d', 'blacklist-floppy.conf')
    example = local.file(res_path).content
    remote_file = host.file('/etc/modprobe.d/blacklist-floppy.conf')
    assert remote_file.exists
    content = remote_file.content
    assert example == content
    # log.debug(content)


def test_modules_load_cc(host):
    log = logging.getLogger('test_modules_load_cc')
    local = get_host("local://")
    res_path = path.join('templates', 'etc', 'modules-load.d', 'cc.conf.j2')
    example = local.file(res_path).content_string
    values = dict(
        item=dict(
            name='bbr',
            value='tcp_bbr'
        )
    )
    example = Template(example, keep_trailing_newline=True).render(values)
    remote_file = host.file('/etc/modules-load.d/cc-bbr.conf')
    assert remote_file.exists
    content = remote_file.content_string
    assert example == content
    # log.debug(content)


def test_fs_watches(host):
    log = logging.getLogger('test_fs_watches')
    local = get_host("local://")
    res_path = path.join('templates', 'etc', 'sysctl.d', '99-fs-watches.conf.j2')
    example = local.file(res_path).content_string
    values = dict(
        max_user_watches=524288
    )
    example = Template(example, keep_trailing_newline=True).render(values)
    remote_file = host.file('/etc/sysctl.d/99-fs-watches.conf')
    assert remote_file.exists
    content = remote_file.content_string
    assert example == content
    # log.debug(content)


def test_sysctl_cc(host):
    log = logging.getLogger('test_sysctl_cc')
    local = get_host("local://")
    res_path = path.join('templates', 'etc', 'sysctl.d', '99-cc.conf.j2')
    example = local.file(res_path).content_string
    values = dict(
        tcp_congestion_control="bbr"
    )
    example = Template(example, keep_trailing_newline=True).render(values)
    remote_file = host.file('/etc/sysctl.d/99-cc-bbr.conf')
    assert remote_file.exists
    content = remote_file.content_string
    assert example == content
    # log.debug(content)
