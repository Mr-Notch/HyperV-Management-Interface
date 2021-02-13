# -- coding: utf-8 --
import func.vm_create.create_commander
import func.vm_setter.set_commander
import func.vm_control.control_commander
<<<<<<< HEAD
import func.netsh.netsh_commander
=======
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
import utilities.getStatus
import utilities.getVMID
import utilities.getAddress
import utilities.RandomDice
import config.ConfigWriter
import Injector

vmloc=Injector.getVMLocation()


def guiwriter():
    print('-------------')
    print('| Create-VM |')
    print('-------------')
    print('')
    vm_name = input('VM Name (String) : ')
    vm_cpunum = input('CPU Number (Int64) : ')
    vm_ramsize = input('RAM Size (Int64) : ')+'GB'
    vm_switch_name = input('VM Switch Name (String) : ')
<<<<<<< HEAD
    port_num = input('Port Mirrored Number (Int64) : ')
=======
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
    vm_location = vmloc
    vhd_size = input('VHD Size (Int64) : ')+'GB'
    vhd_location = vm_location+'\\'+vm_name
    vhd_name = vm_name+'-'+vhd_size
    vhd_controller_type = 'IDE'
    vhd_controller_num = '0'
    vhd_controller_loc = '0'
    iso_location = input('ISO Location (Locate) : ')
    maturity_start_year = input('Maturity Start year (Int Date) : ')
    maturity_start_month = input('Maturity Start month (Int Date) : ')
    maturity_start_day = input('Maturity Start day (Int Date) : ')
    maturity_end_year = input('Maturity End year (Int Date) : ')
    maturity_end_month = input('Maturity End month (Int Date) : ')
    maturity_end_day = input('Maturity End day (Int Date) : ')

    sys_path=Injector.getSysLocation()


    output = func.vm_create.create_commander.vm_create_vm(vm_name, vm_ramsize, vm_cpunum, vm_switch_name, vm_location)

    if output == True:
        print('成功1')
    else:
        print('失败1')

    output2 = func.vm_create.create_commander.vm_create_vhd_dynamic(vhd_size, vhd_location, vhd_name)

    if output2 == True:
        print('成功2')
    else:
        print('失败2')

    output3 = func.vm_setter.set_commander.vm_set_vhd(vm_name, vhd_location, vhd_name, vhd_controller_type, vhd_controller_num,
                                                      vhd_controller_loc)
    if output3 == True:
        print('成功3')
    else:
        print('失败3')

    output4 = func.vm_setter.set_commander.vm_set_dvd(vm_name, iso_location)
    if output4 == True:
        print('成功4')
    else:
        print('失败4')

    output5 = func.vm_control.control_commander.vm_start(vm_name)
    if output5 == True:
        print('成功4')
    else:
        print('失败4')

    while True:
        if utilities.getStatus.getStatus(vm_name) == 'Running':
            break
        else:
            continue

    vmid=utilities.getVMID.getVMID(vm_name,vm_location)
    while True:
<<<<<<< HEAD
        vmaddress=utilities.getAddress.getAddressIfVMStarted(vm_name)
        if vmaddress != "null":
            mirrored_port = '3389'
            outside_port = str(utilities.RandomDice.randomDice())  # 随机的外网端口
            vm_ipv4addr = str(utilities.getAddress.getAddress(vm_name))  # 获取真正的IPV4

            config.ConfigWriter.VMConfWriter(vm_name, vmid, vm_cpunum, vm_ramsize, vm_ipv4addr, "null", "null",
                                             "null", vm_location, maturity_start_year, maturity_start_month,
                                             maturity_start_day, maturity_end_year, maturity_end_month,
                                             maturity_end_day)

            output5 = func.netsh.netsh_commander.netsh_createMirrorPort(outside_port, vm_ipv4addr, mirrored_port)

            if output5 == True:
                print('成功创建远程端口: '+mirrored_port+'->'+outside_port)
                config.ConfigWriter.PortConfigWriter(vm_name, mirrored_port, outside_port, vm_ipv4addr, 'localhost')
                for i in range(int(port_num)):
                    port_mirrored_extra = '1000' + str(i)
                    port_outside_extra = str(utilities.RandomDice.randomDice())
                    output6 = func.netsh.netsh_commander.netsh_createMirrorPort(port_outside_extra, vm_ipv4addr,
                                                                                port_mirrored_extra)
                    if output6:
                        print('成功创建额外端口: ' + port_mirrored_extra + '->' + port_outside_extra)
                        config.ConfigWriter.PortConfigWriter(vm_name, port_mirrored_extra, port_outside_extra,
                                                             vm_ipv4addr, 'localhost')
            else:
                print('失败5')

            # Linux系统一定要把这个注释掉再创建
            # 创建完成以后别忘了再取消掉注释
            # output6 = func.vm_setter.set_commander.vm_set_computer_name(vm_name, vm_location, 'Administrator',
            #                                                             'Aa123456')
            #
            # if output6 == True:
            #     print('成功1')
            # else:
            #     print('失败1')
            break

        else:
            continue

guiwriter()
=======
        vmaddress=utilities.getAddress.getAddress(vm_name)
        if vmaddress != "null":
            break
        else:
            config.ConfigWriter.VMConfWriter(vm_name,vmid,vm_cpunum,vm_ramsize,vmaddress,"null","null","null",vm_location,maturity_start_year,maturity_start_month,maturity_start_day,maturity_end_year,maturity_end_month,maturity_end_day)
            continue


>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
