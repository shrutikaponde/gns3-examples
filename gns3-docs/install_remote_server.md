## Install GNS3 on Cloud (Azure VM, EC2, etc)

### Steps:

1. Create the remote server

* To create a Linux virtual machine in the Azure portal follow these [steps](https://docs.microsoft.com/en-gb/azure/virtual-machines/linux/quick-create-portal?WT.mc_id=UI_empg).

* To create Amazon EC2 Linux instance follow these [steps](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html).

2. Open port `1194` for the remote server.

3. Install GNS3 on a remote server
    Commands:
    ```
    cd /tmp
    curl https://raw.githubusercontent.com/GNS3/gns3-server/master/scripts/remote-install.sh > gns3-remote-install.sh
    bash gns3-remote-install.sh --with-openvpn --with-iou --with-i386-repository
    ```
    Explaination for commands is provided [here](https://docs.gns3.com/docs/getting-started/installation/remote-server).

4. Download the certificate. You can also find the certificate in `/root/client.ovpn`. You can also use `scp` command. First copy `/root/client.ovpn` to `/home/<remote_user>`, then you can use scp to copy it locally.
    ```
    scp <remote_user>@<remote_ip>:/home/<remote_user>/client.ovpn client.ovpn
    ```

5. VPN connection on local Linux
    ```
    sudo apt-get install openvpn
    sudo openvpn --config client.ovpn --auth-retry interact
    ```
    
6. VPN connection on Windows
      Download and install OpenVPN for [Windows](https://openvpn.net/index.php/open-source/downloads.html).

      * Click on “Show Hidden Items” in the Taskbar
      * Right-click on “OpenVPN-GUI”, and select “Import file”
      * Select the .ovpn file you downloaded, and click “Import”
      * Right-click on “OpenVPN-GUI” again, and select “Connect”
      
7. If the VPN works, this page should work: http://172.16.253.1:3080/
