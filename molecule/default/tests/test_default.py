import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hivemq_directory(host):
    hivemq_directory = host.file('/var/local/hivemq')

    assert hivemq_directory.exists
    assert hivemq_directory.is_directory
    assert hivemq_directory.user == 'root'
    assert hivemq_directory.group == 'root'
    assert oct(hivemq_directory.mode) == '0o755'


def test_hivemq_backup_script(host):
    hivemq_backup_script = host.file('/var/local/hivemq/backup.sh')

    assert hivemq_backup_script.exists
    assert hivemq_backup_script.is_file
    assert hivemq_backup_script.user == 'root'
    assert hivemq_backup_script.group == 'root'
    assert oct(hivemq_backup_script.mode) == '0o744'
    assert hivemq_backup_script.sha256sum == '8492fa455080dbfb105ab5eb5a60dd54aa8e4e8d7ad2115491bfb4d4d49a0222'


def test_spool_cron(host):
    spool_cron = host.file('/var/spool/cron')

    assert spool_cron.exists
    assert spool_cron.is_directory
