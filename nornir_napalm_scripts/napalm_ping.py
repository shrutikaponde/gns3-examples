# # Execute Napalm's ping method
# 
# napalm_ping - Call napalm’s ping method


from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

import pprint



nr = InitNornir(config_file="config.yaml")
result = nr.run(task=napalm_ping, dest='192.168.122.146')
print_result(result["r1"])

# TODO: Add source and destination example in topology 