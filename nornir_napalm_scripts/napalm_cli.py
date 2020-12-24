# # Execute Napalm's cli methods
# 
# napalm_cli - Call napalm’s cli method


from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result

import pprint

nr = InitNornir(config_file="config.yaml")
result = nr.run(napalm_cli, commands=["show version", "show ip int br", "show ip route"])
print_result(result["r1"])


# Command output can also be accessed as follows:
# pprint.pprint(result["r1"][0].result["show version"])
