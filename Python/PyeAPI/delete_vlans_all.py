import yaml
import pyeapi


file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    for vlan in vlan_dict['vlans']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Deleting VLAN {vlan_id} from {switch}")
        vlan_api.delete(vlan_id)