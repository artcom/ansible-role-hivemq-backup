# HiveMQ Backup
Ansible role to make periodic backups of HiveMQ broker data.

## Requirements
None.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
hivemq_backup_data_path: /var/local/hivemq
hivemq_backup_destination_path: "{{ hivemq_backup_data_path }}/backup"
```

## Dependencies
None.

# Example Playbook
```yaml
- name: Backup HiveMQ data
  hosts: all
  become: true
  roles:
    - role: hivemq-backup
```

## Test
### Requirements
- python >= 3.7
- docker

### Run
```bash
pip install -r requirements.txt
molecule test
```

## License
MIT
