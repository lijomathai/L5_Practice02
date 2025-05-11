import yaml
import pyeapi

pyeapi.load_config('eapi.conf')

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    raw_cmd_result = connect.enable('show vlan')
    cmd_vlan_dict = raw_cmd_result[0]['result']['vlans']

#--- Script to check if VLAN 10 exist on leaf1, if not proceed to add on leaf1

    if str("10") not in cmd_vlan_dict:
        print(f"vlan-10 donot exist on {switch}!")
        connect = pyeapi.connect_to(switch)
        print(f"Connecting to {switch}")
        # vlan_api = connect.api('vlans')
        # vlan_id = vlan['id']
        # vlan_name = vlan['name']
        for vlan in vlan_dict['vlans']:
            vlan_api = connect.api('vlans')
            vlan_id = vlan['id']
            vlan_name = vlan['name']
            print(f"Adding VLAN {vlan_id} to {switch}")
            if vlan_id == 10:
                print(f"Connecting to {switch}")
                # vlan_api = connect.api('vlans')
                # vlan_id = vlan['id']
                # vlan_name = vlan['name']
                print(f"Adding {vlan_id} to {switch}")
                vlan_api.create(vlan_id)
                vlan_api.set_name(vlan_id, vlan_name)
            else:
                print("No Action needed!")
            # vlan_api.create(vlan_id)
            # vlan_api.set_name(vlan_id, vlan_name)
    else:
        print(f"vlan-10 exist on {switch}")

#-- End of script !!