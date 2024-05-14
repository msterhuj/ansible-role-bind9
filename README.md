Bind9
=========

Install and manage bind9 master, slave server and zone.

compatible with multiple zone

[![Lint and Test Ansible Role](https://github.com/msterhuj/ansible-role-bind9/actions/workflows/ansible-test.yml/badge.svg?branch=master)](https://github.com/msterhuj/ansible-role-bind9/actions/workflows/ansible-test.yml)

Requirements
------------

You need to enable the gathering of facts in your playbook.

Role Variables
--------------

Variable can be found in `defaults/main.yml` and are as follows: [Click here](defaults/main.yml)

Dependencies
------------

No dependencies

Example Playbook
----------------

```yaml
- name: "Install and configure bind9"
  roles:
    - role: msterhuj.bind9m
```

License
-------

GNU GPLv3

Author Information
------------------

MsterHuj <gabin.lanore@gmail.com>