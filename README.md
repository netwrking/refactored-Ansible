# refactored-Ansible
Welcome to my first Ansible labs with Eve-ng.

# refactored-Ansible Overview
I will use this lab to write playbooks to perform basic configuration tasks on routers and switches

# Ansible-Lab1

This project contains Ansible automation for lab environments using EVE-NG.

## Structure
- `inventories/`: Static host inventory
- `playbooks/`: Playbooks to automate show commands and config tasks

## Usage
```bash
ansible-playbook -i inventories/lab_hosts.ini playbooks/show_version.yaml
