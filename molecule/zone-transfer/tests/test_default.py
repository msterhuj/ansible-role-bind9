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
    if host.run("hostname") == "master":
        files.append("/etc/bind/db.example.com")
    else:
        files.append("/var/lib/bind/db.example.com")

    for file in files:
        config = host.file(file)
        assert config.exists

# todo add test for zone transfer
