from __future__ import print_function
import pyeapi

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')
raw_cmd_result = connect.enable('show version')
cmd_sys_info = raw_cmd_result[0]['result']['systemMacAddress']

print(f'My system MAC address is {cmd_sys_info}')