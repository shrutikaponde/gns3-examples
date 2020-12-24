# # Execute Napalm's validate method
# 
# napalm_validate - Call napalm’s validate method


from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_validate
from nornir_utils.plugins.functions import print_result

import pprint



nr = InitNornir(config_file="config.yaml")
result = nr.run(task=napalm_validate, src='validation_files/validate_ios_R1.yaml')
print_result(result["r1"])


