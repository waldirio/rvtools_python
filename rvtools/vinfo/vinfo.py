from pyVmomi import vim


def vinfo_collect(si):
    print("here here here")
    print("the SI content: {}". format(si))

    content = si.RetrieveContent()
    container = content.rootFolder

    viewType = [vim.VirtualMachine]
    containerView = content.viewManager.CreateContainerView(container,viewType,True)

    children = containerView.view
    for child in children:
        vm = child.name
        print("Machine Name: {}".format(vm))
        print("here")
        pass
#        powerstate = child.PowerState
#        print("Powerstate: {}".format(powerstate))

        template = "xx"
        print("Template: {}".format(template))

        config_status = child.configStatus
        print("Config status: {}".format(config_status))

        dns_name = "xx"
        print("DNS Name: {}".format(dns_name))

        connection_state = "xx"
        print("Connection state: {}".format(connection_state))

        guest_state = child.guest.guestState
        print("Guest state: {}".format(guest_state))

        heartbeat = child.guestHeartbeatStatus
        print("Heartbeat: {}".format(heartbeat))

        consolidation_needed = "xx"
        print("Consolidation needed: {}".format(consolidation_needed))

        poweron = "xx"
        print("Power On: {}".format(poweron))

        suspend_time = "xx"
        print("Suspend time: {}".format(suspend_time))

        change_version = child.config.changeVersion
        print("Change version: {}".format(change_version))

        cpus = child.config.hardware.numCPU
        print("CPUs: {}".format(cpus))

        latency_sensitivy = "xx"
        print("Latency sensitivy: {}".format(latency_sensitivy))

        memory = child.config.hardware.memoryMB
        print("Memory: {}".format(memory))

        nics = "xx"
        print("Nics: {}".format(nics))

        disks = "xx"
        print("Disks: {}".format(disks))

        enable_uuid = "xx"
        print("Enable UUID: {}".format(enable_uuid))

        cbt = "xx"
        print("CBT: {}".format(cbt))

        network_01 = "xx"
        print("Network #1: {}".format(network_01))

        network_02 = "xx"
        print("Network #2: {}".format(network_02))

        network_03 = "xx"
        print("Network #3: {}".format(network_03))

        network_04 = "xx"
        print("Network #4: {}".format(network_04))

        num_monitors = "xx"
        print("Num monitors: {}".format(num_monitors))

        video_ram_kb = "xx"
        print("Video ram KB: {}".format(video_ram_kb))

        resource_pool = "xx"
        print("Resource pool: {}".format(resource_pool))

        folder = "xx"
        print("Folder: {}".format(folder))

        vapp = "xx"
        print("vApp: {}".format(vapp))

        das_protection = "xx"
        print("DAS protection: {}".format(das_protection))

        ft_state = "xx"
        print("FT state: {}".format(ft_state))

        ft_latency = "xx"
        print("FT latency: {}".format(ft_latency))

        ft_bandwidth = "xx"
        print("FT bandwidth: {}".format(ft_bandwidth))

        ft_sec_latency = "xx"
        print("FT sec latency: {}".format(ft_sec_latency))

        provisioned_mb = "xx"
        print("Provisioned MB: {}".format(provisioned_mb))

        in_use_mb = "xx"
        print("In use MB: {}".format(in_use_mb))

        unshared_mb = "xx"
        print("Unshared MB: {}".format(unshared_mb))

        ha_restart_priority = "xx"
        print("HA restart priority: {}".format(ha_restart_priority))

        ha_isolation_response = "xx"
        print("HA isolation response: {}".format(ha_isolation_response))

        ha_vm_monitoring = "xx"
        print("HA VM monitoring: {}".format(ha_vm_monitoring))

        cluster_rule = "xx"
        print("Cluster rule: {}".format(cluster_rule))

        cluster_rule_name = "xx"
        print("Cluster rule name: {}".format(cluster_rule_name))

        boot_required = "xx"
        print("Boot required: {}".format(boot_required))

        boot_delay = child.config.bootOptions.bootDelay
        print("Boot delay: {}".format(boot_delay))

        boot_retry_delay = child.config.bootOptions.bootRetryDelay
        print("Boot retry delay: {}".format(boot_retry_delay))

        boot_retry_enabled = child.config.bootOptions.bootRetryEnabled
        print("Boot retry enabled: {}".format(boot_retry_enabled))

        boot_bios_setup = "xx"
        print("Boot bios setup: {}".format(boot_bios_setup))

        firmware = child.config.firmware
        print("Firmware: {}".format(firmware))

        hw_version = "xx"
        print("HW Version: {}".format(hw_version))

        hw_upgrade_status = "xx"
        print("HW Upgrade Status: {}".format(hw_upgrade_status))

        hw_upgrade_policy = "xx"
        print("HW Upgrade Policy: {}".format(hw_upgrade_policy))

        hw_target = "xx"
        print("HW Target: {}".format(hw_target))

        path = child.config.files.vmPathName
        print("Path: {}".format(path))

        annotation = "xx"
        print("Annotation: {}".format(annotation))

        datacenter = "xx"
        print("Datacenter: {}".format(datacenter))

        cluster = "xx"
        print("Cluster: {}".format(cluster))

        host = "xx"
        print("Host: {}".format(host))

        os_according_to_the_configuration_file = "xx"
        print("OS According to the configuration file: {}".format(os_according_to_the_configuration_file))

        os_according_to_the_vmware_tools = child.config.guestFullName
        print("OS According to the vmware tools: {}".format(os_according_to_the_vmware_tools))

        vm_id = "xx"
        print("VM ID: {}".format(vm_id))

        vm_uuid = "xx"
        print("VM UUID: {}".format(vm_uuid))

        vi_sdk_server_type = "xx"
        print("VI SDK SERVER TYPE: {}".format(vi_sdk_server_type))

        vi_sdk_api_version = "xx"
        print("VI SDK API VERSION: {}".format(vi_sdk_api_version))

        vi_sdk_server = "xx"
        print("VI SDK SERVER: {}".format(vi_sdk_server))

        vi_sdk_uuid = "xx"
        print("VI SDK UUID: {}".format(vi_sdk_uuid))

        print("=====================")