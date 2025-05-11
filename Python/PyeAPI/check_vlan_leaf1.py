import yaml
import pyeapi

pyeapi.load_config('eapi.conf')

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

connect = pyeapi.connect_to('leaf1')
raw_cmd_result = connect.enable('show vlan')
cmd_vlan_dict = raw_cmd_result[0]['result']['vlans']

#--- Script to check if VLAN 10 exist on leaf1, if not proceed to add on leaf1

if str("10") not in cmd_vlan_dict:
    print("vlan-10 donot exist on leaf1!")
    connect = pyeapi.connect_to('leaf1')
    print(f"Connecting to leaf1")
    vlan_api = connect.api('vlans')
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        # print(f"Adding VLAN {vlan_id} to leaf1")
        if vlan_id == 10:
            print(f"Adding {vlan_id} to leaf1")
            vlan_api.create(vlan_id)
            vlan_api.set_name(vlan_id, vlan_name)
        else:
            print("No Action needed!")
        # vlan_api.create(vlan_id)
        # vlan_api.set_name(vlan_id, vlan_name)
else:
    print("vlan-10 exist on leaf1")

#-- End of script !!