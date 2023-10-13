Ansible Role: Node.js
=========

![.github/workflows/roles.yml](https://github.com/xxy1991/ansible-collection-debase/actions/workflows/roles.yml/badge.svg)

An Ansible Role that installs [Node.js](https://nodejs.org) on Debian-based Linux.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# Node.js options:
# version options:
# 12 for 12.x
# 14 for 14.x (LTS)
# 16 for 16.x (current)
# lts for 14.x
# current for 16.x
nodejs_version: lts
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    nodejs_version: lts
  roles:
    - xxy1991.nodejs
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
