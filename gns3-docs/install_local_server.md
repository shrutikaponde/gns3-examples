## Install GNS3 on Local Linux Machine (Ubuntu 16.04)

### Steps:

1. Install Dynamips and Ubridge
    ```
    sudo apt install dynamips ubridge
    ```
    * Verify installation
    ```
    dynamips
    ubridge -v
    ```
    
2. Install Virtual PC Simulator(VPCS)
    * Download [vpcs](https://github.com/GNS3/vpcs/archive/v0.6.2.zip) and extract the zip.
    ```
    cd vpcs-0.6.2/src
    ./mk.sh 64 # i386 | amd64 | 32 | 64 ---> mention any of the option
    sudo mv vpcs /usr/local/bin
    ```
    * Verify the location and version for VPCS
    ```
    which vpcs
    vpcs -v
    ```
    
3. Install QEMU
4. Install Docker
5. Install Wireshark
6. Install GNS3
    Create a python virtual environment and install `gns3-server`, `gns3-gui` and other dependencies inside virutal environment:
    ```
    python -m venv ~/.gns3-venv
    source /home/user/.gns-vnev/bin/activate
    pip install -U gns3-gui gns3-server PyQt5-sip pyqt5==5.14.0
    ```
    The steps to install other dependiences ar not mentioned here. Please check [official documentation](https://docs.gns3.com/docs/getting-started/installation/linux) to install all dependencies.

7. Launch GNS3 gui with command:
    ```
    gns3
    ```
    If installation was successful, it will launch the application.
 
## Errors:
   ### Error 1
   ```
   2020-12-17 19:48:15 CRITICAL topology.py:258 uBridge is not available, path doesn't exist, or you just installed GNS3 and need to restart your user session to refresh user permissions.
   ```
   Restart your machine or change `ubridge` permissions using following command:
   ```
   sudo chmod 777 /usr/bin/ubridge
   ```
    
   ### Error 2
   ```
   No path to a VPCS executable has been set
   ```
   Download [vpcs](https://github.com/GNS3/vpcs/releases). Go to Edit > Preferences > VPCS Preferences > Set Path to a VPCS executable. You may need to restart GNS3.
