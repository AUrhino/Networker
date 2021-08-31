#!/usr/bin/python
# This will use the Networker API to get a list of VM from the discovered Vsphere job.

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


''' Creds and common items'''
credU = 'administrator'
credP = 'PASSWORD'
host = 'https://fqdn.domain.name'
url = '{}:9090/nwrestapi/v2/global/vmware/vms?fl=name&q=powerState:on'.format(host)

def main():
    print_header()
    get_APMs()

def print_header():
    print('')
    print('----------------------------------------------------------------')
    print('   List of VM discovered via Networker                          ')
    print('----------------------------------------------------------------')
    print('')

def get_APMs():
    session = requests.Session()
    vms = session.request("GET", url, auth=(credU, credP), verify=False)
    print (vms.text)                                     # Displays the output

if __name__ == '__main__':
    main()
