# # Execute Napalm's get_* methods
# 
# napalm_get - Call napalm’s get_* method


from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

import pprint



nr = InitNornir(config_file="config.yaml")
result = nr.run(
    task=napalm_get,
    getters=["facts", "config", "interfaces", "bgp_neighbors"]
    )

# print_result(result)
print('==========================================')
print('===================FACTS==================')
print('==========================================')
# ### Get Facts:
pprint.pprint(result['r1'][0].result['facts'])

input()
print('==========================================')
print('==================CONFIG==================')
print('==========================================')
# ### Get Config:
pprint.pprint(result['r1'][0].result['config'])

input()
print('==========================================')
print('===============INTERFACES=================')
print('==========================================')
# ### Get Interfaces:
pprint.pprint(result['r1'][0].result['interfaces'])

input()
print('==========================================')
print('===============BGP_NEI====================')
print('==========================================')
# ### Get BGP neighbors:
pprint.pprint(result['r1'][0].result['bgp_neighbors'])


# #### Find other getter methods in napalm [here](https://napalm.readthedocs.io/en/latest/support/#getters-support-matrix)

