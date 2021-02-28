
from MainInterface import it_hmi_location
from MainInterface import it_iso_location
from MainInterface import it_vm_location
from MainInterface import it_template_location
from MainInterface import it_vm_switch_name
from MainInterface import it_template_login_user_name
from MainInterface import it_template_login_user_password
from MainInterface import it_vm_netsh_default_connect_port
from MainInterface import it_bare_metal_mode
from MainInterface import it_vm_netsh_extra_mirrored_port_started
from MainInterface import it_vm_netsh_extra_connect_port_number
from Interface import config_writer
from Interface.Actuator import PowershellActuator
from Interface.UT import get_now_time
from Interface.UT import get_random_port

def VMCreateWheel(vm_name,vm_ram,vm_cpu,vhd_size,iso_name):
    try:
        # Create a VM
        stdout_1 = PowershellActuator.vm_newVM(vm_name,vm_ram,vm_cpu,it_vm_switch_name)
        print(stdout_1)

        # Create a VHD Drive
        vhd_location_has_name = it_vm_location+vm_name
        vhd_name = vm_name+'-'+vhd_size
        PowershellActuator.disk_newVHD_dynamic(vhd_size,vhd_location_has_name,vhd_name)

        # Load VHD Drive into VM
        PowershellActuator.disk_loadVHD(vm_name,vhd_name)

        # Get vm_id
        vm_id = PowershellActuator.catch_vm_getVMID(vm_name).replace(' ','').replace('\n','').replace('\r','')
        print('VM '+vm_name+' ID: '+vm_id)

        # # Catch vm_vhd_path
        while True:

            
            vm_disks_vhd_path = PowershellActuator.catch_disk_getVHD(vm_name,'Path').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_path:
                # print('未获取到硬盘路径, 重复获取')
                continue
            else:
                # print('获取成功硬盘路径')
                break

        # 已修复该漏洞（Issue-201）

        while True:
            vm_disks_vhd_controller_type = PowershellActuator.catch_disk_getVHD(vm_name,'ControllerType').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_controller_type:
                # print('未获取到硬盘控制器类型')
                continue
            else:
                # print('获取成功硬盘控制器类型')
                break

        # Catch vm_vhd_ControllerNumber
        while True:
            vm_disks_vhd_controller_number = PowershellActuator.catch_disk_getVHD(vm_name,'ControllerNumber').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_controller_number:
                # print('未获取到控制器number')
                continue
            else:
                # print('获取成功控制器number')
                break

        # Catch vm_vhd_ControllerLocation
        while True:
            vm_disks_vhd_controller_location = PowershellActuator.catch_disk_getVHD(vm_name,'ControllerLocation').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_controller_location:
                # print('未获取到控制器地址')
                continue
            else:
                # print('获取成功控制器地址')
                break

        # Load ISO Drive
        PowershellActuator.disk_loadDVD(vm_name,iso_name)

        # Start VM
        a_5=PowershellActuator.vm_startVM(vm_name)
        print(a_5)

        # Print Output
        print('')
        print('Please install the OS like in physical computer.')
        print('The Create-VM Task will be continued.')
        print('')
        # Catch vm_address_ipv4
        while True:
            vm_address_ipv4 = PowershellActuator.catch_vm_getAddress_ipv4(vm_name).replace(' ','').replace('\n','').replace('\r','')
            if 'null' in vm_address_ipv4:

                # print('未获取到ipv4地址')
                continue
            else:
                print('IPv4 Address: '+vm_address_ipv4)
                break
        
        # Catch vm_address_ipv6
        while True:
            vm_address_ipv6 = PowershellActuator.catch_vm_getAddress_ipv6(vm_name).replace(' ','').replace('\n','').replace('\r','')
            if 'null' in vm_address_ipv6:
                # print('未获取到ipv6地址')
                continue
            else:
                print('IPv6 Address: '+vm_address_ipv6)
                break

        # Create NetSH Mirror Port 3389 to random
        random_port = str(get_random_port.getRandomPort()).replace(' ','').replace('\n','')
        mirrored_port = it_vm_netsh_default_connect_port
        print('Create Port Mirrored: '+mirrored_port+'->'+random_port)
        PowershellActuator.netsh_createMirrorPort(random_port,vm_address_ipv4,mirrored_port)

        # Get Now Time
        maturity_start_date = str(get_now_time.getNowTime()).replace(' ','').replace('\n','').replace('\r','')
        
        api_dict = {
            "function.type": "Create-VM",
            "vm.name": vm_name,
            "vm.address.ipv4": vm_address_ipv4,
            "vm.address.ipv6": vm_address_ipv6,
            "vm.location": it_vm_location+vm_name+'\\',
            "function.time": maturity_start_date
        }
        return api_dict
    except Exception as e:
        return e
    

def VMExportWheel(vm_name):
    try:
        # Get VM-Status
        while True:
            switch = PowershellActuator.catch_vm_getPowerStatus(vm_name)
            if 'Running' in switch:
                break
            else:
                continue

        # Stop VM
        stdout_1 = PowershellActuator.vm_stop_conventional(vm_name)
        print(stdout_1)

        # Export VM
        stdout_2 = PowershellActuator.vm_exportVM(vm_name)
        print(stdout_2)

        # Get Now Time
        maturity_start_date = str(get_now_time.getNowTime())

        api_dict = {
            "function.type": "Export-VM",
            "vm.name": vm_name,
            "vm.location": it_template_location+vm_name+'\\',
            "function.time": maturity_start_date
        }

        return api_dict
    except Exception as e:
        return e


def VMImportWheel(template_name,vm_name,vm_ram,vm_cpu,maturity_end_date):
    try:
        # Import VM from template
        print('')
        print('Loading vm in template. Do not close this window or shutdown computer.')
        stdout_1 = PowershellActuator.vm_importVM(template_name,vm_name)
        print(stdout_1)

        # Get VM-ID
        vm_id = PowershellActuator.catch_vm_getVMID(vm_name).replace(' ','').replace('\n','').replace('\r','')
        print('VM '+vm_name+' ID: '+vm_id)

        '''
        # Get it_bare_metal_mode switch
        if it_bare_metal_mode == True:
            # Set Static RAM
            stdout_2 = PowershellActuator.vm_setRAM_static(vm_name,vm_ram)
            print(stdout_2)
        else:
            # Set Dynamic RAM
            stdout_2 = PowershellActuator.vm_setRAM_dynamic(vm_name,vm_ram)
        '''
        stdout_2 = PowershellActuator.vm_setRAM_static(vm_name,vm_ram)
        print(stdout_2)

        stdout_3 = PowershellActuator.vm_setCPU(vm_name,vm_cpu)
        print(stdout_3)

        # Catch vm_vhd_path
        while True:
            vm_disks_vhd_path = PowershellActuator.catch_disk_getVHD(vm_name,'Path').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_path:
                # print('未获取到硬盘路径, 重复获取')
                continue
            else:
                # print('获取成功硬盘路径')
                break

        # 已修复该漏洞（Issue-201）

        while True:
            vm_disks_vhd_controller_type = PowershellActuator.catch_disk_getVHD(vm_name,'ControllerType').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_controller_type:
                # print('未获取到硬盘控制器类型')
                continue
            else:
                # print('获取成功硬盘控制器类型')
                break

        # Catch vm_vhd_ControllerNumber
        while True:
            vm_disks_vhd_controller_number = PowershellActuator.catch_disk_getVHD(vm_name,'ControllerNumber').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_controller_number:
                # print('未获取到控制器number')
                continue
            else:
                # print('获取成功控制器number')
                break

        # Catch vm_vhd_ControllerLocation
        while True:
            vm_disks_vhd_controller_location = PowershellActuator.catch_disk_getVHD(vm_name,'ControllerLocation').replace(' ','').replace('\n','').replace('\r','').replace("'","")
            if 'null' in vm_disks_vhd_controller_location:
                # print('未获取到控制器地址')
                continue
            else:
                # print('获取成功控制器地址')
                break

        # Start VM
        stdout_4 = PowershellActuator.vm_startVM(vm_name)
        print(stdout_4)

        # Catch vm_address_ipv4
        while True:
            vm_address_ipv4 = PowershellActuator.catch_vm_getAddress_ipv4(vm_name).replace(' ','').replace('\n','').replace('\r','')
            if 'null' in vm_address_ipv4:

                # print('未获取到ipv4地址')
                continue
            else:
                # print('成功获取ipv4地址')
                break
        
        # Catch vm_address_ipv6
        while True:
            vm_address_ipv6 = PowershellActuator.catch_vm_getAddress_ipv6(vm_name).replace(' ','').replace('\n','').replace('\r','')
            if 'null' in vm_address_ipv6:
                # print('未获取到ipv6地址')
                continue
            else:
                # print('成功获取ipv6地址')
                break
        
        # Create NetSH Mirror Port 3389 to random
        random_port = str(get_random_port.getRandomPort()).replace(' ','').replace('\n','')
        mirrored_port = it_vm_netsh_default_connect_port
        print('Create Port Mirrored: '+mirrored_port+'->'+random_port)
        PowershellActuator.netsh_createMirrorPort(random_port,vm_address_ipv4,mirrored_port)

        # Create NetSH Mirror Port automatic
        for i in range(it_vm_netsh_extra_mirrored_port_started, it_vm_netsh_extra_mirrored_port_started + it_vm_netsh_extra_connect_port_number):
            random_port_extra = str(get_random_port.getRandomPort()).replace(' ','').replace('\n','')
            print('Create Extra Port Mirrored: '+i+'->'+random_port)
            PowershellActuator.netsh_createMirrorPort(random_port_extra,vm_address_ipv4,i)
            

        # Get Now Time
        maturity_start_date = str(get_now_time.getNowTime())
        
        # Write Config Second
        config_writer.VMConfWriter(vm_name,vm_id,vm_cpu,vm_ram,vm_address_ipv4,vm_address_ipv6,mirrored_port,random_port,vm_disks_vhd_controller_type,vm_disks_vhd_controller_number,vm_disks_vhd_controller_location,'VHDX',vm_disks_vhd_path,maturity_start_date,maturity_end_date)
        
        # Log-In VM and change Computer-Name to VM-ID
        vm_login_user = it_template_login_user_name
        vm_login_password = it_template_login_user_password
        PowershellActuator.vm_setComputerNameToVMID(vm_name,vm_login_user,vm_login_password)

        api_dict = {
            "function.type": "Create-VM",
            "template.name": template_name,
            "vm.name": vm_name,
            "vm.address.ipv4": vm_address_ipv4,
            "vm.address.ipv6": vm_address_ipv6,
            "vm.location": it_vm_location+vm_name+'\\',
            "vm.location.config": it_hmi_location+'Config\\'+vm_name+'.json',
            "function.time": maturity_start_date
        }
        return api_dict
    except Exception as e:
        return e




