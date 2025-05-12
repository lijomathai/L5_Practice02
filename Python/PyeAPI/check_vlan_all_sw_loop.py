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

#--- Script to check if VLAN str("x") exist on all switches, if not proceed to add VLAN str("x")

    if str("20") not in cmd_vlan_dict:
        print(f"vlan-20 donot exist on {switch}!")
        for vlan in vlan_dict['vlans']:
            vlan_api = connect.api('vlans')
            vlan_id = vlan['id']
            vlan_name = vlan['name']
            while vlan_id == 20:
                print(f"Adding VLAN {vlan_id} to {switch}")
                vlan_api.create(vlan_id)
                vlan_api.set_name(vlan_id, vlan_name)
                break
    else:
        print(f"vlan-20 exist on {switch}")

#-- End of script !!