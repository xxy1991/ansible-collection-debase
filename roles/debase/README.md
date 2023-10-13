Ansible Role: Common configurations for Debian-Based Linux
=========

![.github/workflows/roles.yml](https://github.com/xxy1991/ansible-collection-debase/actions/workflows/roles.yml/badge.svg)

An Ansible Role that configure on Debian-based Linux.

Requirements
------------

None.

Role Variables
--------------

see `vars/main.yml` and `defaults/main.yml`

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    software_google_chrome: true
    software_scooter_bcompare: true
  roles:
    - xxy1991.debase
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
