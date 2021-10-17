from pyVmomi import vim
import pyVmomi
from rvtools.printrv.csv_print import *


def get_obj(content, vimtype):
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    obj = container.view[0].name
    # for c in container.view:
    #     if name:
    #         if c.name == name:
    #             obj = c
    #             break
    #     else:
    #         obj = c
    #         break
    return obj


def vinfo_collect(service_instance, directory):
    """ Def responsible to connect on the vCenter and retrieve VM information """

    print("## Processing vInfo module")

    content = service_instance.RetrieveContent()
    container = content.rootFolder

    view_type = [vim.VirtualMachine]
    container_view = content.viewManager.CreateContainerView(container, view_type, True)

    server_list = []

    children = container_view.view
    for child in children:
        # if 'sat62' in child.name:
        # if 'akavir-sat63' in child.name:
        # if 'waldirio' in child.name:
        if True:

            # get_obj(content, [vim.Datacenter], name)

            vinfo_data = {}

            # OK
            vm = child.name
            if vm is None:
                vm = ""
            print("Machine Name: {}".format(vm))
            vinfo_data['vm'] = vm

            # OK
            powerstate = child.runtime.powerState
            if powerstate is None:
                powerstate = ""
            # print("Powerstate: {}".format(powerstate))
            vinfo_data['powerstate'] = str(powerstate)

            # OK
            template = child.config.template
            if template is None:
                template = ""
            # print("Template: {}".format(template))
            vinfo_data['template'] = str(template)

            # OK
            config_status = child.configStatus
            if config_status is None:
                config_status = ""
            # print("Config status: {}".format(config_status))
            vinfo_data['config_status'] = str(config_status)

            # OK
            dns_name = child.guest.hostName
            if dns_name is None:
                dns_name = ""
            # print("DNS Name: {}".format(dns_name))
            vinfo_data['dns_name'] = str(dns_name)

            # OK
            connection_state = child.runtime.connectionState
            if connection_state is None:
                connection_state = ""
            # print("Connection state: {}".format(connection_state))
            vinfo_data['connection_state'] = str(connection_state)

            # OK
            guest_state = child.guest.guestState
            if guest_state is None:
                guest_state = ""
            # print("Guest state: {}".format(guest_state))
            vinfo_data['guest_state'] = str(guest_state)

            # OK
            heartbeat = child.guestHeartbeatStatus
            if heartbeat is None:
                heartbeat = ""
            # print("Heartbeat: {}".format(heartbeat))
            vinfo_data['heartbeat'] = str(heartbeat)

            # OK
            consolidation_needed = child.runtime.consolidationNeeded
            if consolidation_needed is None:
                consolidation_needed = ""
            # print("Consolidation needed: {}".format(consolidation_needed))
            vinfo_data['consolidation_needed'] = str(consolidation_needed)

            # poweron = "xx"
            # print("Power On: {}".format(poweron))
            # vinfo_data['xx'] = str(xx)

            # OK
            suspend_time = child.runtime.suspendTime
            if suspend_time is None:
                suspend_time = ""
            # print("Suspend time: {}".format(suspend_time))
            vinfo_data['suspend_time'] = str(suspend_time)

            # OK
            change_version = child.config.changeVersion
            if change_version is None:
                change_version = ""
            # print("Change version: {}".format(change_version))
            vinfo_data['change_version'] = str(change_version)

            # OK
            cpus = child.config.hardware.numCPU
            if cpus is None:
                cpus = ""
            # print("CPUs: {}".format(cpus))
            vinfo_data['cpus'] = str(cpus)

            # OK
            try:
                latency_sensitivity = child.config.latencySensitivity.level
            except AttributeError:
                latency_sensitivity = ""

            # print("Latency sensitivy: {}".format(latency_sensitivity))
            vinfo_data['latency_sensitivity'] = str(latency_sensitivity)

            # OK
            memory = child.config.hardware.memoryMB
            if memory is None:
                memory = ""
            # print("Memory: {}".format(memory))
            vinfo_data['memory'] = str(memory)

            # OK
            nics = child.network.__len__()
            # print("Nics: {}".format(nics))
            vinfo_data['nics'] = str(nics)

            # OK
            disks = child.layout.disk.__len__()
            if disks is None:
                disks = ""
            # print("Disks: {}".format(disks))
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
            except IndexError:
                network_01 = ""

            # print("Network #1: {}".format(network_01))
            vinfo_data['network_01'] = str(network_01)

            # OK
            try:
                if child.network[1].name:
                    network_02 = child.network[1].name
            except IndexError:
                network_02 = ""

            # print("Network #2: {}".format(network_02))
            vinfo_data['network_02'] = str(network_02)

            # OK
            try:
                if child.network[2].name:
                    network_03 = child.network[2].name
            except IndexError:
                network_03 = ""

            # print("Network #3: {}".format(network_03))
            vinfo_data['network_03'] = str(network_03)

            # OK
            try:
                if child.network[3].name:
                    network_04 = child.network[3].name
            except IndexError:
                network_04 = ""

            # print("Network #4: {}".format(network_04))
            vinfo_data['network_04'] = str(network_04)

            # OK
            for device in child.config.hardware.device:
                if device._wsdlName == 'VirtualMachineVideoCard':
                    num_monitors = device.numDisplays
                    # print("Num monitors: {}".format(num_monitors))
                    vinfo_data['num_monitors'] = str(num_monitors)
                    break

            # OK
            for device in child.config.hardware.device:
                if device._wsdlName == 'VirtualMachineVideoCard':
                    video_ram_kb = device.videoRamSizeInKB
                    # print("Video ram KB: {}".format(video_ram_kb))
                    vinfo_data['video_ram_kb'] = str(video_ram_kb)
                    break

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
            if ft_state is None:
                ft_state = ""
            # print("FT state: {}".format(ft_state))
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
            if boot_delay is None:
                boot_delay = ""
            # print("Boot delay: {}".format(boot_delay))
            vinfo_data['boot_delay'] = str(boot_delay)

            # OK
            boot_retry_delay = child.config.bootOptions.bootRetryDelay
            if boot_retry_delay is None:
                boot_retry_delay = ""
            # print("Boot retry delay: {}".format(boot_retry_delay))
            vinfo_data['boot_retry_delay'] = str(boot_retry_delay)

            # OK
            boot_retry_enabled = child.config.bootOptions.bootRetryEnabled
            if boot_retry_enabled is None:
                boot_retry_enabled = ""
            # print("Boot retry enabled: {}".format(boot_retry_enabled))
            vinfo_data['boot_retry_enabled'] = str(boot_retry_enabled)

            # boot_bios_setup = "xx"
            # print("Boot bios setup: {}".format(boot_bios_setup))
            # vinfo_data['xx'] = str(xx)

            # OK
            firmware = child.config.firmware
            if firmware is None:
                firmware = ""
            # print("Firmware: {}".format(firmware))
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
            if path is None:
                path = ""
            # print("Path: {}".format(path))
            vinfo_data['path'] = str(path)

            # annotation = "xx"
            # print("Annotation: {}".format(annotation))
            # vinfo_data['xx'] = str(xx)

            # OK
            datacenter = get_obj(content, [vim.Datacenter])
            # datacenter = get_obj(child, [vim.Datacenter])
            print("Datacenter: {}".format(datacenter))
            vinfo_data['datacenter'] = str(datacenter)

            # OK
            cluster = get_obj(content, [vim.ClusterComputeResource])
            print("Cluster: {}".format(cluster))
            vinfo_data['cluster'] = str(cluster)

            # try:
            #     host = child.runtime.host.name
            # except pyVmomi.VmomiSupport.NoPermission:
            # # except vim.fault.noPermission:
            #     host = None

            # if host is None:
            #     host = ""
            # # print("Host: {}".format(host))
            # vinfo_data['host'] = str(host)

            # os_according_to_the_configuration_file = "xx"
            # print("OS According to the configuration file: {}".format(os_according_to_the_configuration_file))
            # vinfo_data['xx'] = str(xx)

            # OK
            os_according_to_the_vmware_tools = child.config.guestFullName
            if os_according_to_the_vmware_tools is None:
                os_according_to_the_vmware_tools = ""
            # print("OS According to the vmware tools: {}".format(os_according_to_the_vmware_tools))
            vinfo_data['os_according_to_the_vmware_tools'] = str(os_according_to_the_vmware_tools)

            # OK
            vm_id = child._moId
            if vm_id is None:
                vm_id = ""
            # print("VM ID: {}".format(vm_id))
            vinfo_data['vm_id'] = str(vm_id)

            # OK
            vm_uuid = child.config.uuid
            if vm_uuid is None:
                vm_uuid = ""
            # print("VM UUID: {}".format(vm_uuid))
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

            print("=====================")

            server_list.append(vinfo_data)

    csv_print("vinfo.csv", server_list, directory)
