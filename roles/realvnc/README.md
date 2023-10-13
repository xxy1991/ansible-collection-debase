Ansible Role: RealVNC
=========

![.github/workflows/roles.yml](https://github.com/xxy1991/ansible-collection-debase/actions/workflows/roles.yml/badge.svg)

An Ansible Role that installs [RealVNC](https://www.realvnc.com) on Debian-based Linux.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# RealVNC options:
realvnc_version: 6.7.4
realvnc_license: ""
realvnc_x11_enabled: false
realvnc_virtual_enabled: false
realvnc_virtual_use_system_xorg: true
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    realvnc_version: 6.7.4
    realvnc_license: ""
    realvnc_x11_enabled: true
    realvnc_virtual_enabled: true
    realvnc_virtual_use_system_xorg: true
  roles:
    - xxy1991.realvnc
```

Molecule test
-------------

```shell
molecule test
```

License
-------

AGPL-3.0-or-later

xxy1991(xxy1991@gmail.com)
------------------
