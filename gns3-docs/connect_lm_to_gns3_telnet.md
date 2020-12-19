## Connect local machine to GNS3

1. Create GNS3 Topology
    Add Cloud and Cisco Router to GNS3 and configure them.
    

    1. Configure Cloud

        Run `ifconfig` check available interfaces. Configure the cloud with an interface `virbr0`.

        ![IF_CONFIG](https://github.com/shrutikaponde/gns3-examples/blob/main/imgs/ifconfig.png)

        Add link from `virbr0` to `fa0/0`.

        ![CISCO_TOPOLOGY](https://github.com/shrutikaponde/gns3-examples/blob/main/imgs/cloud_cisco.png)

    2. Configure router

        Open router console and type following commands
        ```
        R1>en
        R1#conf t
        R1(config)#int fa0/0
        R1(config-if)#ip add dhcp
        R1(config-if)#no shut
        R1(config-if)#exit

        # If password and secret not configured, configure it 
        R1(config)#line vty 0 4
        R1(config-line)#password cisco 
        R1(config-line)#exit
        R1(config)#enable secret cisco 
        R1(config)#exit
        R1#wr
        ```

2. Check ip assigned to the router for interface fa0/0
    ```
    R1#show ip int br    
    Interface                  IP-Address      OK? Method Status                Protocol
    FastEthernet0/0            192.168.122.146 YES DHCP   up                    up   
    Serial0/0                  unassigned      YES unset  administratively down down  
    ```

3. Check if you ping the router from th local machine `ping 192.168.122.146`
4. Connect to router with `telnet`
    ```
    shrutika@shrutika:~$ telnet 192.168.122.146
    Trying 192.168.122.146...
    Connected to 192.168.122.146.
    Escape character is '^]'.


    User Access Verification

    Password: 

    ```

Yeah !!! We can successfully access the router from local machine.