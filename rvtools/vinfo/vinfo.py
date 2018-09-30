# from pprint import pprint
import time

from pyVmomi import vim
from print.csv_print import *
from obj_inspect import *

def vinfo_collect(service_instance):
    """ Def responsible to connect on the vCenter and retrieve VM information """

    content = service_instance.RetrieveContent()
    container = content.rootFolder

    view_type = [vim.VirtualMachine]
    container_view = content.viewManager.CreateContainerView(container, view_type, True)

    server_list = []

    children = container_view.view
    for child in children:
        # if 'sat62' in child.name:
        # if 'akavir-sat63' in child.name:
        if True:

            vinfo_data = {}

            # OK
            vm = child.name
            print("Machine Name: {}".format(vm))
            vinfo_data['vm'] = vm

            # OK
            powerstate = child.runtime.powerState
            print("Powerstate: {}".format(powerstate))
            vinfo_data['powerstate'] = str(powerstate)

            # OK
            template = child.config.template
            print("Template: {}".format(template))
            vinfo_data['template'] = str(template)

            # OK
            config_status = child.configStatus
            print("Config status: {}".format(config_status))
            vinfo_data['config_status'] = str(config_status)

            # OK
            dns_name = child.guest.hostName
            print("DNS Name: {}".format(dns_name))
            vinfo_data['dns_name'] = str(dns_name)

            # OK
            connection_state = child.runtime.connectionState
            print("Connection state: {}".format(connection_state))
            vinfo_data['connection_state'] = str(connection_state)

            # OK
            guest_state = child.guest.guestState
            print("Guest state: {}".format(guest_state))
            vinfo_data['guest_state'] = str(guest_state)

            # OK
            heartbeat = child.guestHeartbeatStatus
            print("Heartbeat: {}".format(heartbeat))
            vinfo_data['heartbeat'] = str(heartbeat)

            # OK
            consolidation_needed = child.runtime.consolidationNeeded
            print("Consolidation needed: {}".format(consolidation_needed))
            vinfo_data['consolidation_needed'] = str(consolidation_needed)

            # poweron = "xx"
            # print("Power On: {}".format(poweron))
            # vinfo_data['xx'] = str(xx)

            # OK
            suspend_time = child.runtime.suspendTime
            print("Suspend time: {}".format(suspend_time))
            vinfo_data['suspend_time'] = str(suspend_time)

            # OK
            change_version = child.config.changeVersion
            print("Change version: {}".format(change_version))
            vinfo_data['change_version'] = str(change_version)

            # OK
            cpus = child.config.hardware.numCPU
            print("CPUs: {}".format(cpus))
            vinfo_data['cpus'] = str(cpus)

            # OK
            latency_sensitivity = child.config.latencySensitivity.level
            print("Latency sensitivy: {}".format(latency_sensitivity))
            vinfo_data['latency_sensitivity'] = str(latency_sensitivity)

            # OK
            memory = child.config.hardware.memoryMB
            print("Memory: {}".format(memory))
            vinfo_data['memory'] = str(memory)

            # #nics = child.guest.ipStack.len()
            # nics = "xx"
            # print("Nics: {}".format(nics))
            # vinfo_data['xx'] = str(xx)

            # OK
            disks = child.layout.disk.__len__()
            print("Disks: {}".format(disks))
            vinfo_data['disks'] = str(disks)

            # enable_uuid = "xx"
            # print("Enable UUID: {}".format(enable_uuid))
            # vinfo_data['xx'] = str(xx)

            # cbt = "xx"
            # print("CBT: {}".format(cbt))
            # vinfo_data['xx'] = str(xx)

            # OK
            try:
                if child.network[0].name:
                    network_01 = child.network[0].name
            except(IndexError):
                network_01 = ""

            print("Network #1: {}".format(network_01))
            vinfo_data['network_01'] = str(network_01)

            # OK
            try:
                if child.network[1].name:
                    network_02 = child.network[1].name
            except(IndexError):
                network_02 = ""

            print("Network #2: {}".format(network_02))
            vinfo_data['network_02'] = str(network_02)

            # OK
            try:
                if child.network[2].name:
                    network_03 = child.network[2].name
            except(IndexError):
                network_03 = ""

            print("Network #3: {}".format(network_03))
            vinfo_data['network_03'] = str(network_03)

            # OK
            try:
                if child.network[3].name:
                    network_04 = child.network[3].name
            except(IndexError):
                network_04 = ""

            print("Network #4: {}".format(network_04))
            vinfo_data['network_04'] = str(network_04)


            num_monitors = "xx"
            print("Num monitors: {}".format(num_monitors))
            # vinfo_data['xx'] = str(xx)

            print("here")

            # video_ram_kb = "xx"
            # print("Video ram KB: {}".format(video_ram_kb))
            # vinfo_data['xx'] = str(xx)

            # resource_pool = "xx"
            # print("Resource pool: {}".format(resource_pool))
            # vinfo_data['xx'] = str(xx)

            # folder = "xx"
            # print("Folder: {}".format(folder))
            # vinfo_data['xx'] = str(xx)

            # vapp = "xx"
            # print("vApp: {}".format(vapp))
            # vinfo_data['xx'] = str(xx)

            # das_protection = "xx"
            # print("DAS protection: {}".format(das_protection))
            # vinfo_data['xx'] = str(xx)

            # OK
            ft_state = child.runtime.faultToleranceState
            print("FT state: {}".format(ft_state))
            vinfo_data['ft_state'] = str(ft_state)

            # ft_latency = "xx"
            # print("FT latency: {}".format(ft_latency))
            # vinfo_data['xx'] = str(xx)

            # ft_bandwidth = "xx"
            # print("FT bandwidth: {}".format(ft_bandwidth))
            # vinfo_data['xx'] = str(xx)

            # ft_sec_latency = "xx"
            # print("FT sec latency: {}".format(ft_sec_latency))
            # vinfo_data['xx'] = str(xx)

            # provisioned_mb = "xx"
            # print("Provisioned MB: {}".format(provisioned_mb))
            # vinfo_data['xx'] = str(xx)

            # in_use_mb = "xx"
            # print("In use MB: {}".format(in_use_mb))
            # vinfo_data['xx'] = str(xx)

            # unshared_mb = "xx"
            # print("Unshared MB: {}".format(unshared_mb))
            # vinfo_data['xx'] = str(xx)

            # ha_restart_priority = "xx"
            # print("HA restart priority: {}".format(ha_restart_priority))
            # vinfo_data['xx'] = str(xx)

            # ha_isolation_response = "xx"
            # print("HA isolation response: {}".format(ha_isolation_response))
            # vinfo_data['xx'] = str(xx)

            # ha_vm_monitoring = "xx"
            # print("HA VM monitoring: {}".format(ha_vm_monitoring))
            # vinfo_data['xx'] = str(xx)

            # cluster_rule = "xx"
            # print("Cluster rule: {}".format(cluster_rule))
            # vinfo_data['xx'] = str(xx)

            # cluster_rule_name = "xx"
            # print("Cluster rule name: {}".format(cluster_rule_name))
            # vinfo_data['xx'] = str(xx)

            # boot_required = "xx"
            # print("Boot required: {}".format(boot_required))
            # vinfo_data['xx'] = str(xx)

            # OK
            boot_delay = child.config.bootOptions.bootDelay
            print("Boot delay: {}".format(boot_delay))
            vinfo_data['boot_delay'] = str(boot_delay)

            # OK
            boot_retry_delay = child.config.bootOptions.bootRetryDelay
            print("Boot retry delay: {}".format(boot_retry_delay))
            vinfo_data['boot_retry_delay'] = str(boot_retry_delay)

            # OK
            boot_retry_enabled = child.config.bootOptions.bootRetryEnabled
            print("Boot retry enabled: {}".format(boot_retry_enabled))
            vinfo_data['boot_retry_enabled'] = str(boot_retry_enabled)

            # boot_bios_setup = "xx"
            # print("Boot bios setup: {}".format(boot_bios_setup))
            # vinfo_data['xx'] = str(xx)

            # OK
            firmware = child.config.firmware
            print("Firmware: {}".format(firmware))
            vinfo_data['firmware'] = str(firmware)

            # hw_version = "xx"
            # print("HW Version: {}".format(hw_version))
            # vinfo_data['xx'] = str(xx)

            # hw_upgrade_status = "xx"
            # print("HW Upgrade Status: {}".format(hw_upgrade_status))
            # vinfo_data['xx'] = str(xx)

            # hw_upgrade_policy = "xx"
            # print("HW Upgrade Policy: {}".format(hw_upgrade_policy))
            # vinfo_data['xx'] = str(xx)

            # hw_target = "xx"
            # print("HW Target: {}".format(hw_target))
            # vinfo_data['xx'] = str(xx)

            # OK
            path = child.config.files.vmPathName
            print("Path: {}".format(path))
            vinfo_data['path'] = str(path)

            # annotation = "xx"
            # print("Annotation: {}".format(annotation))
            # vinfo_data['xx'] = str(xx)

            # datacenter = "xx"
            # print("Datacenter: {}".format(datacenter))
            # vinfo_data['xx'] = str(xx)

            # cluster = "xx"
            # print("Cluster: {}".format(cluster))
            # vinfo_data['xx'] = str(xx)

            # host = "xx"
            # print("Host: {}".format(host))
            # vinfo_data['xx'] = str(xx)

            # os_according_to_the_configuration_file = "xx"
            # print("OS According to the configuration file: {}".format(os_according_to_the_configuration_file))
            # vinfo_data['xx'] = str(xx)

            # OK
            os_according_to_the_vmware_tools = child.config.guestFullName
            print("OS According to the vmware tools: {}".format(os_according_to_the_vmware_tools))
            vinfo_data['os_according_to_the_vmware_tools'] = str(os_according_to_the_vmware_tools)

            # vm_id = "xx"
            # print("VM ID: {}".format(vm_id))
            # vinfo_data['xx'] = str(xx)

            # OK
            vm_uuid = child.config.uuid
            print("VM UUID: {}".format(vm_uuid))
            vinfo_data['vm_uuid'] = str(vm_uuid)

            # vi_sdk_server_type = "xx"
            # print("VI SDK SERVER TYPE: {}".format(vi_sdk_server_type))
            # vinfo_data['xx'] = str(xx)

            # vi_sdk_api_version = "xx"
            # print("VI SDK API VERSION: {}".format(vi_sdk_api_version))
            # vinfo_data['xx'] = str(xx)

            # vi_sdk_server = "xx"
            # print("VI SDK SERVER: {}".format(vi_sdk_server))
            # vinfo_data['xx'] = str(xx)

            # vi_sdk_uuid = "xx"
            # print("VI SDK UUID: {}".format(vi_sdk_uuid))
            # vinfo_data['xx'] = str(xx)

            # print("=====================")


            server_list.append(vinfo_data)

    csv_print("vinfo.csv", server_list)
