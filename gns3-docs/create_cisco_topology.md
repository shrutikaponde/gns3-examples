## Create Cisco Topology

To configure a Cisco topology, you must first add IOS images to GNS3.
Watch this [video](https://www.youtube.com/watch?v=YQcWuWGjppY) to understand how to add images and setup Cisco topology.

### Example 1: GNS3 topology consisting of two Cisco routers
The [official document](https://docs.gns3.com/docs/getting-started/your-first-cisco-topology) explains to configure a simple GNS3 topology consisting of two Cisco routers.

### Example 2: Set-up Cisco router configuration to receive/forward data packets between computer networks

#### Final topology snapshot:
![CISCO_TOPTLOGY](https://user-images.githubusercontent.com/26830541/102511871-4ff76580-40af-11eb-8a1d-850433ee5d2e.jpeg)

Open console for respective node and copy following commands.

##### PC1 configuration:
```
ip 192.168.10.1 255.255.255.0 192.168.10.2
```

##### PC2 configuration:
```
ip 192.168.20.1 255.255.255.0 192.168.20.2
```

##### Router(R1) configuration:
ip address of interface fa0/0 will be same as default Gateway(`192.168.10.2`) of PC1.
```
Router>enable
Router#conf t
Router(config)#int fa0/0
Router(config-if)#ip address 192.168.10.2 255.255.255.0
Router(config-if)#no shut
Router(config-if)#exit
Router(config)#int serial0/0
Router(config-if)#clock rate 128000
Router(config-if)#ip address 192.168.30.1 255.255.255.0
Router(config-if)#no shut
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 192.168.30.3
Router(config)#exit
Router#wr
```

##### Router(R2) configuration:
ip address of interface fa0/0 will be same as default Gateway(`192.168.20.2`) of PC2. 
```
Router>enable
Router#conf t
Router(config)#int fa0/0
Router(config-if)#ip address 192.168.20.2 255.255.255.0
Router(config-if)#no shut
Router(config-if)#exit
Router(config)#int serial0/0
Router(config-if)#clock rate 128000
Router(config-if)#ip address 192.168.30.2 255.255.255.0
Router(config-if)#no shut
Router(config-if)#exit
Router(config)#ip route 0.0.0.0 0.0.0.0 192.168.30.3
Router(config)#exit
Router#wr
```
#### Test the topology :
* From PC1 `ping 192.168.20.1`(PC2)
* From PC2 `ping 192.168.10.1`(PC1)

Both should be able to ping sucessfully


### References:
* https://www.youtube.com/watch?v=52tbNuHX2G8