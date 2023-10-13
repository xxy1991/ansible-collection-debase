Ansible Role: HashiCorp
=========

![.github/workflows/roles.yml](https://github.com/xxy1991/ansible-collection-debase/actions/workflows/roles.yml/badge.svg)

An Ansible Role that installs [HashiCorp Products](https://www.hashicorp.com) on Debian-based Linux.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# HashiCorp options
hashicorp_install_packer: true
hashicorp_install_vagrant: true
hashicorp_install_terraform: true
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    hashicorp_install_packer: true
    hashicorp_install_vagrant: true
    hashicorp_install_terraform: true
  roles:
    - xxy1991.hashicorp
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
