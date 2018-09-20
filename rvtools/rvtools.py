#!/usr/bin/env python 

from corerv import *
from vinfo.vinfo import *
import requests

from pyVim import connect
from pyVmomi import vmodl
#from pyVmomi import vim
import ssl

requests.packages.urllib3.disable_warnings()

def main():
    print("Reading the conf file")

    obj = coreCode()
    conn = obj.read_conf_file()

    sslContext = ssl._create_unverified_context()

    # sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # sslContext.verify_mode = ssl.CERT_NONE

    print("vcenter: {}\nuser: {}\npassword: {}\n ".format(conn._vcenter, conn._username, conn._password))
    
    si = connect.SmartConnect(host=conn._vcenter,user=conn._username,pwd=conn._password, port=443, sslContext=sslContext)

#    content = si.RetrieveContent()
#    container = content.rootFolder

#    viewType = [vim.VirtualMachine]
#    containerView = content.viewManager.CreateContainerView(container,viewType,True)

    #vm_data = pchelper.collect_properties()


    vinfo_collect(si)
#    children = containerView.view
#    for child in children:
#        machine_name = child.name
#        print("Machine Name: {}".format(machine_name))
        #aux = child.config.bootOptions.networkBootProtocol
#        aux = child.config.hardware.numCPU
#        print("Aux: {}".format(aux))
#        pass
        #print("{}".format(child.config.cpuAllocation))
        #print("{}".format(child.hardware.numCPU))
        

#        print("{},{},{}".format(child.name,child.runtime.powerState,child.config.cpuAllocation.hardware.numCPU))
        #print(child.runtime.powerState)
##        print(child.guest)
##        print("")

#    viewType = [vim.Datacenter]
#    containerView = content.viewManager.CreateContainerView(container,viewType,True)

#    aux = containerView.view

#    print ("test")
#    pass


    # si1 = vim.GuestOsDescriptor.GuestOsIdentifier
    # si1 = vim.SmartConnect(host=conn._vcenter,user=conn._username,pwd=conn._password, port=443, sslContext=sslContext)
    
    # dir(si)
    # dc = si.content.rootFolder.childEntity[0]
    # vm = dc.vmFolder.childEntity

    # for i in vm:
    #     print(i.name)
    # print(si.CurrentTime())

    #xpto = si.vim.vm.GuestOsDescriptor.GuestOsIdentifier

    pass
    
# https://code.vmware.com/apis/358/vsphere

if __name__ == "__main__":
    main()
