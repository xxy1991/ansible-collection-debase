Ansible Role: Docker
=========

![.github/workflows/roles.yml](https://github.com/xxy1991/ansible-collection-debase/actions/workflows/roles.yml/badge.svg)

An Ansible Role that installs [Docker](https://www.docker.com) on Debian-based Linux.

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
# Docker options
docker_install_compose: false
docker_use_buildx: true
```

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all
  vars:
    docker_install_compose: false
    docker_use_buildx: true
    docker_users: [ xxy ]
  roles:
    - xxy1991.docker
```

Molecule test
-------------

```shell
molecule test
```

License
-------

AGPL-3.0-or-later

## Reference

- [geerlingguy/ansible-role-docker](https://github.com/`geerlingguy/ansible-role-docker`)

xxy1991(xxy1991@gmail.com)
------------------
