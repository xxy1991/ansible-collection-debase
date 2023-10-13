Ansible Role: Visual Studio Code
=========

![.github/workflows/roles.yml](https://github.com/xxy1991/ansible-collection-debase/actions/workflows/roles.yml/badge.svg)

An Ansible Role that installs [Visual Studio Code](https://code.visualstudio.com) on Debian-based Linux.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# Visual Studio Code options
vscode_install_stable: true
vscode_install_insiders: false
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    vscode_install_stable: true
    vscode_install_insiders: false
  roles:
    - xxy1991.vscode
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
