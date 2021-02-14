import func.vm_control.control_commander
import func.vm_setter.set_commander
import func.netsh.netsh_commander
import utilities.getVMID
import utilities.getStatus
import utilities.getAddress
import utilities.RandomDice
import config.ConfigWriter
import Injector
import time

temloc = Injector.getTemLoc()
vmloc = Injector.getVMLocation()


def guiwriter():
    print('-------------')
    print('| Import-VM |')
    print('-------------')
    print('')
    template_name = input('Template Name (String) : ')
    template_location = temloc
    vm_name = input('VM Name (String) : ')
    vm_location = vmloc
    vm_cpunum = input('CPU Number (Int64) : ')
    vm_ramsize = input('RAM Size (Int64) : ') + 'GB'
    port_num = input('Port Mirrored Number (Int64) : ')
    # maturity_start_year = input('Maturity Start year (Int Date) : ')
    # maturity_start_month = input('Maturity Start month (Int Date) : ')
    # maturity_start_day = input('Maturity Start day (Int Date) : ')

    maturity_start_year = time.strftime('%Y', time.localtime(time.time()))
    maturity_start_month = time.strftime('%m', time.localtime(time.time()))
    maturity_start_day = time.strftime('%d', time.localtime(time.time()))

    maturity_end_year = input('Maturity End year (Int Date) : ')
    maturity_end_month = input('Maturity End month (Int Date) : ')
    maturity_end_day = input('Maturity End day (Int Date) : ')
    if template_name == vm_name:
        print('Error: VM Name cannot be the same as Template Name')
        return False

    output1 = func.vm_control.control_commander.vm_import(template_name, template_location, vm_name, vm_location)
    if output1 == True:
        print('成功1')
    else:
        print('失败1')

    output2 = func.vm_setter.set_commander.vm_set_cpunum(vm_name, vm_cpunum)
    if output2 == True:
        print('成功2')
    else:
        print('失败2')

    output3 = func.vm_setter.set_commander.vm_set_ramsize_static(vm_name, vm_ramsize)
    if output3 == True:
        print('成功3')
    else:
        print('失败3')

    output4 = func.vm_control.control_commander.vm_start(vm_name)
    if output4 == True:
        print('成功4')
    else:
        print('失败4')

    while True:
        if utilities.getStatus.getStatus(vm_name) == 'Running':
            break
        else:
            continue
    print('执行第二个循环')
    vmid = utilities.getVMID.getVMID(vm_name, vm_location).replace('\r\n', '')
    while True:
        print('开始获取IP地址, 检测虚拟机是否进入系统')
        vmaddress = utilities.getAddress.getAddressIfVMStarted(vm_name)
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
                print('成功创建远程端口: ' + mirrored_port + '->' + outside_port)
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

            output7 = func.vm_setter.set_commander.vm_set_computer_name(vm_name, vm_location, 'Administrator',
                                                                        'Aa123456')

            if output7 == True:
                print('成功6')
            else:
                print('失败6')
            break
        else:
            continue


guiwriter()
