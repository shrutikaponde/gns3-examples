## Install Nornir and other plugins

1. Create virtual environment and activate it.

```
python -m venv .nornir-venv
source .nornir-venv/bin/activate
```

2. Install Nornir

```
pip install nornir nornir_utils
```

3. Install Napalm and Netmiko plugin

```
pip install nornir_netmiko nornir_napalm
```