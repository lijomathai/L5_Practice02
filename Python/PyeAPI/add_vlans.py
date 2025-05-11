import yaml
import pyeapi

pyeapi.load_config('eapi.conf')

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

#-- to add vlans in the list to leaf1

# for switch in vlan_dict['switches']:
#     print(f"Connecting to {switch}")
# connect = pyeapi.connect_to('leaf1')
# vlan_api = connect.api('vlans')
# for vlan in vlan_dict['vlans']:
#     vlan_id = vlan['id']
#     vlan_name = vlan['name']
#     print(f"Adding VLAN {vlan_id} to leaf1")
#     vlan_api.create(vlan_id)
#     vlan_api.set_name(vlan_id, vlan_name)

#-- end of script !!

#-- to add all vlans in the list on all the switches in the list

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)

#-- end of script !!