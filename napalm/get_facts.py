#!/usr/bin/python3.6

# 
# Connecting to cisco router configured in GNS3
# 

from napalm import get_network_driver
from pprint import pprint

driver = get_network_driver('ios')
conn_method = {'transport': 'telnet', 'secret': 'cisco'}
host = '192.168.122.200'  # your ip address
user = ''
passwd = 'cisco'

# With context manager
with driver(hostname=host, username=user, password=passwd, optional_args=conn_method ) as device:
    print('Getting facts')
    pprint(device.get_facts())
