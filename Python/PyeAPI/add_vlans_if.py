import yaml
import pyeapi

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')
raw_cmd_result = connect.enable('show vlan')
cmd_vlan_dict = raw_cmd_result[0]['result']['vlans']
for vlan in cmd_vlan_dict:
    vlan_id = vlan
    vlan_name = cmd_vlan_dict[vlan]['name']
    print(vlan)