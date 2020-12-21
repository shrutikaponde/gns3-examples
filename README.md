# GNS3 Guide

1. [Install GNS3 on Remote server (Azure, AWS)](gns3-docs/install_remote_server.md)
2. [Install GNS3 on Local machine (Linux)](gns3-docs/install_local_server.md)
3. [Create GNS3 Topology](gns3-docs/create_gns3_topology.md)
4. [Create GNS3 Cisco Topology](gns3-docs/create_cisco_topology.md)
5. [Connect local machine to GNS3(Telnet)](gns3-docs/connect_lm_to_gns3_telnet.md)
6. [Connect local machine to GNS3(SSH)](gns3-docs/connect_lm_to_gns3_ssh.md)

# Nornir 

## Install 

1. Install nornir into virtual environment.

    ```
    python -m venv .nornir-venv
    source .nornir-venv/bin/activate
    pip install nornir nornir_utils
    ```

## Nornir With Napalm

1. Install nornir_napalm plugin
    ```
    pip install nornir_napalm
    ```

2. Access GNS3 devices using Nornir and Napalm
    * [napalm_cli](nornir/napalm_cli.ipynb) - Call napalm's cli method
    * napalm_configure - Call napalm's configure method. It also allows committing/discarding configurations. (In progress)
    * [napalm_get](nornir/napalm_get.ipynb) - Call napalm's get_* methods
    * [napalm_ping](nornir/napalm_ping.ipynb) - Call napalm's ping method`
    * [napalm_validate](nornir/napalm_validate.ipynb) - Call napalm's validate method


## Nornir With Napalm

1. Install nornir_netmiko plugin
    ```
    pip install nornir_netmiko
    ```
2. Access GNS3 devices using Nornir and Netmiko (Coming Soon)


# Useful References

* https://www.freeccnaworkbook.com/workbooks/ccna/interface-ip-address-configuration
* http://journey2ccie.blogspot.com/2010/02/gns3-install-and-configure-vpcs-to-use.html
* https://binarynature.blogspot.com/2015/11/install-configure-gns3-arch-linux.html
* https://protechgurus.com/how-to-use-vpcs-in-gns3/
* https://www.learncisco.net/courses/icnd-1/lan-connections/configuring-a-router.html
* https://imtiazrahman.com/2016/11/17/how-to-login-cisco-router-with-ssh-key/ (####)
* https://gns3.com/community/featured/error-while-setting-up-node-virb
* https://developer.cisco.com/codeexchange/github/repo/shahkh-eng/Project-Code-Nornir/
* https://codingnetworks.blog/napalm-network-automation-python-working-with-cisco-ios-and-ios-xr/
* https://dteslya.engineer/network_automaiton_101/