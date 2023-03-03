Bind9
=========

Install and manage bind9 master, slave server and zone.

compatible with multiple zone

Requirements
------------

No requirements, apart from ansible.

Role Variables
--------------

All var is in example playbook below

> Note the variables `bind9_hostname` need to be set to the hostname of the machine. This is used to generate the `named.conf.local` file. If you don't set this variable, the role will use the actual hostname of the machine.

Dependencies
------------

No dependencies

Example Playbook
----------------

```yaml
- name: "Install and configure bind9"
  hosts: localhost
  roles:
    - role: bind9m
      vars:
        # new hostname
        bind9_hostname: "ns"

        # ansible inventory host name 
        bind9_master_inv_name: "master" 

        # list of forwarders
        bind9_forwarders:
          - 8.8.8.8
          - 1.1.1.1

        bind9_zones:
          # create db file for example.com
          - name: "example.com"
            serial: "{{ ansible_date_time.epoch }}"
            refresh: 3600
            retry: 600
            expire: 604800
            ttl: 86400
            # address of master for slave
            master:
              - "127.0.0.1"
            # address of slaves allowed to transfer zone
            allow_transfer:
              - "127.0.0.1"
            # list of records (order is applied in db file)
            records:
              - name: "@"
                type: "A"
                value: "127.0.0.1"
```

License
-------

BSD

Author Information
------------------

MsterHuj <gabin.lanore@gmail.com>