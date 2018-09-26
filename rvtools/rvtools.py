""" Main rvtools module """
#!/usr/bin/env python 

import ssl
import requests
from pyVim import connect

from corerv import *
from vinfo.vinfo import *

#from pyVmomi import vmodl


requests.packages.urllib3.disable_warnings()

def main():
    """ Def responsible to start the vCenter connection and call all report modules """
    print("Reading the conf file")

    obj = CoreCode()
    conn = obj.read_conf_file()

    ssl_context = ssl._create_unverified_context()

    print("vcenter: {}\nuser: {}\npassword: {}\n ".format( \
         conn._vcenter, conn._username, conn._password))

    service_instance = connect.SmartConnect(host=conn._vcenter, user=conn._username, \
         pwd=conn._password, port=443, sslContext=ssl_context)


    # VM Information
    vinfo_collect(service_instance)



# https://code.vmware.com/apis/358/vsphere

if __name__ == "__main__":
    main()
