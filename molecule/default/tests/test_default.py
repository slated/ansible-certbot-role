import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_certbot_is_existed(host):
    cerbot = host.file("/opt/certbot-auto")
    assert cerbot.exists
