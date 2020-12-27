cd gns3-examples/
git checkout ubuntu-gns3-topology
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9 -y
sudo apt install python3.9-dev python3.9-venv -y
python3.9 -m venv .nornir-venv
. .nornir-venv/bin/activate
pip install nornir nornir_utils nornir_napalm nornir_jinja2
