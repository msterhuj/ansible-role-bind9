from retry import retry

def test_account_present(host):
    group = host.group("bind")
    user = host.user("bind")
    assert group.exists
    assert user.exists

def test_config_file(host):
    files: list[str] =  [
        "/etc/bind/named.conf",
        "/etc/bind/named.conf.options",
    ]

    hostname = host.ansible.get_variables().get('inventory_hostname')
    if hostname == "master":
        files.append("/etc/bind/db.example.com")
    else:
        files.append("/var/lib/bind/db.example.com")

    @retry(AssertionError, tries=5, delay=5.0)
    def _check_file():
        for file in files:
            assert host.file(file).exists

    _check_file()
