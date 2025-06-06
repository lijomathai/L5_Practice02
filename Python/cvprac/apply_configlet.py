# Copyright (c) 2021 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from cvprac.cvp_client import CvpClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

# Create connection to CloudVision
clnt = CvpClient()
clnt.connect(nodes=['192.168.0.5'], username="arista",password="aristacnyc")

configletName = 'cvprac_example'

device_name = "leaf1"
device = clnt.api.get_device_by_name(device_name)

configlet = clnt.api.get_configlet_by_name(configletName)

clnt.api.apply_configlets_to_device("", device, [configlet])