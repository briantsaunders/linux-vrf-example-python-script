# Linux VRF Example Python Script

This script is an example for how to create a vrf, delete a vrf, and add / remove interfaces from a VRF in Linux via python.  Included in this repo is a Vagrant file that will spin up a vagrant environment for testing the script functionality.

## Script Prerequisites

```
>= python3.6
pip3
```

## Vagrant Environment

![environment](https://github.com/briantsaunders/linux-vrf-example-python-script/blob/master/docs/environment.PNG?raw=true)

Vagrant and virtualbox should be install prior to bringing up the vagrant environment.

The vagrant environment is simulating a single router with multiple interfaces and servers connected to those interfaces.  The router (circle in the diagram) is Ubuntu 18.04 with [FRRouting](https://frrouting.org/) installed.  The servers (squares in the diagram) are vanilla Ubuntu 18.04.

Following the below instructions the python script will place the router's interfaces into VRFs so that the servers will only be able to communicate with other servers in their respective VRF.

### Vagrant Up

```
git clone https://github.com/briantsaunders/linux-vrf-example-python-script.git
cd linux-vrf-example-python-script
vagrant up
```

Ansible is used to provision the site1router virtual box.  It will install pip3 on site1router, and will pip3 install the requirements.txt on site1router.  Check out the playbook pb.conf.all.yml for more details.

### Testing in Vagrant

Once the vagrant environment is up issue the following commands to configure VRFs on the site1router.

Create VRFs on sie1router:
```
vagrant ssh site1router
cd /vagrant
sudo python3 linux_vrf_example.py --action create --vrf_name vrf1 --vrf_table 1
sudo python3 linux_vrf_example.py --action create --vrf_name vrf2 --vrf_table 2
```

Associate interfaces with VRFs on site1router:
```
vagrant ssh site1router
cd /vagrant
sudo python3 linux_vrf_example.py --action add_interface --vrf_name vrf1 --interface eth2
sudo python3 linux_vrf_example.py --action add_interface --vrf_name vrf1 --interface eth3
sudo python3 linux_vrf_example.py --action add_interface --vrf_name vrf2 --interface eth4
sudo python3 linux_vrf_example.py --action add_interface --vrf_name vrf2 --interface eth5
```

Validate site1server1 CAN ping site1server2 and CANNOT ping site1server3 or site1server4:
```
vagrant ssh site1server1
ping 10.1.2.10
ping 10.1.3.10
ping 10.1.4.10
```

Validate site1server3 CAN ping site1server4 and CANNOT ping site1server1 or site1server2:
```
vagrant ssh site1server
ping 10.1.4.10
ping 10.1.1.10
ping 10.1.2.10
```

Disassociate interfaces with VRFs on site1router:
```
vagrant ssh site1router
cd /vagrant
sudo python3 linux_vrf_example.py --action remove_interface --vrf_name vrf1 --interface eth2
sudo python3 linux_vrf_example.py --action remove_interface --vrf_name vrf1 --interface eth3
sudo python3 linux_vrf_example.py --action remove_interface --vrf_name vrf2 --interface eth4
sudo python3 linux_vrf_example.py --action remove_interface --vrf_name vrf2 --interface eth5
```

Delete VRFs on site1router:
```
vagrant ssh site1router
cd /vagrant
sudo python3 linux_vrf_example.py --action delete --vrf_name vrf1
sudo python3 linux_vrf_example.py --action delete --vrf_name vrf2
```

## Script Operation

### Args

| Option String | Required | Type    | Default | Example  | Description    |
|---------------|----------|---------|---------|----------|----------------|
| action    | True     | string  | none    | create | create, delete, add_interface, remove_interface  |
| vrf_name   | True     | string  | none    | vrf1 | Name of vrf |
| vrf_table           | False     | integer | none    | 1      | VRF table     |
| interface | False | string | none    | eth2   | Name of interface |

### Run

#### Create VRF

```
sudo python3 linux_vrf_example.py --action create --vrf_name vrf1 --vrf_table 1
```

#### Add Interface to VRF

```
sudo python3 linux_vrf_example.py --action add_interface --vrf_name vrf1 --interface eth2
```

#### Remove Interface from VRF

```
sudo python3 linux_vrf_example.py --action remove_interface --vrf_name vrf1 --interface eth2
```

#### Delete VRF

```
sudo python3 linux_vrf_example.py --action delete --vrf_name vrf1
```