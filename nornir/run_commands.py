#!/usr/bin/python3.6
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

commands = ['show ip int br', 'show ip route']

for cmd in commands:
    nr = InitNornir(
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": "hosts.yaml"
            },
        },
    )

    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd
    )

    print_result(result)
