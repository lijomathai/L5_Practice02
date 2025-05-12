from cvprac.cvp_client import CvpClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Create connection to CloudVision
clnt = CvpClient()
clnt.connect(nodes=['192.168.0.5'], username="arista",password="aristacnyc")

configletName = "cvprac_example"

configlet = """!
interface Ethernet10
   description test
   ip address 10.144.144.1/24
!
"""

clnt.api.add_configlet(configletName,configlet)