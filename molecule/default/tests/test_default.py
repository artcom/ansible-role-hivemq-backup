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
    assert (
        hivemq_backup_script.sha256sum ==
        'a512edfdffbf0626a0a5c466de73e0c8a1f97e7e9c48ea771c5b0ce2b4e7c60a'
    )


def test_spool_cron(host):
    spool_cron = host.file('/var/spool/cron')

    assert spool_cron.exists
    assert spool_cron.is_directory


def test_backup_crontab(host):
    backup_crontab = host.file('/var/spool/cron/crontabs/root')

    assert backup_crontab.exists
    assert backup_crontab.is_file
    assert backup_crontab.contains(
        r'^0 1 \* \* \* /bin/bash /var/local/hivemq/backup\.sh$'
    )
