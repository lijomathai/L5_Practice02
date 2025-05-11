import yaml
import pyeapi

pyeapi.load_config('eapi.conf')

#-- to print the vlan name & vlan id on leaf1 !!

connect = pyeapi.connect_to('leaf1')
raw_cmd_result = connect.enable('show vlan')
cmd_vlan_dict = raw_cmd_result[0]['result']['vlans']
# print(cmd_vlan_dict[vlan])

for vlan in cmd_vlan_dict:
    vlan_id = vlan
    vlan_name = cmd_vlan_dict[vlan]['name']
    print(vlan) #to print vlan ID
    # print(cmd_vlan_dict[vlan]['name']) #to print vlan name
    # print(f"VLAN ID of {vlan_id} with name {vlan_name}") #to print vlan ID with name

#-- End of script !!

#-- to print a report of all the vlan name & vlan id on all the switches in the list!!

file = open('vlans.yml', 'r')
file_vlan_dict = yaml.safe_load(file)

# for switch in file_vlan_dict['switches']:
#     connect = pyeapi.connect_to(switch)
#     # print(f"Connecting to {switch}")
#     raw_cmd_result = connect.enable('show vlan')
#     cmd_vlan_dict = raw_cmd_result[0]['result']['vlans']
#     print(f"For switch {switch}")
#     for vlan in cmd_vlan_dict:
#         vlan_id = vlan
#         vlan_name = cmd_vlan_dict[vlan]['name']
#         # print(cmd_vlan_dict[vlan]['name'])
#         print(f"VLAN ID of {vlan_id} with name {vlan_name}")

#-- End of script !!