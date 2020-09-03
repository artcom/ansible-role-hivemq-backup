# HiveMQ Backup
Ansible role to make periodic backups of HiveMQ broker data.

## Requirements
None.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
backup_data_path: null
backup_destination_path: null
```
Mandatory variables (role will fail if the variables are not set):
```yaml
backup_data_path: "string"
backup_destination_path: "string"
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
      vars:
        backup_data_path: /var/local/hivemq
        backup_destination_path: "{{ backup_data_path }}/backup"
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
