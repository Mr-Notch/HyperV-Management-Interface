import func.vm_control.control_commander
import func.vm_setter.set_commander
import utilities.getVMID
import utilities.getStatus
import utilities.getAddress
import utilities.RandomDice
import config.ConfigWriter
import Injector
temloc=Injector.getTemLoc()
vmloc=Injector.getVMLocation()


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
    vm_ramsize = input('RAM Size (Int64) : ')+'GB'
    maturity_start_year = input('Maturity Start year (Int Date) : ')
    maturity_start_month = input('Maturity Start month (Int Date) : ')
    maturity_start_day = input('Maturity Start day (Int Date) : ')
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
        print('成功3')
    else:
        print('失败3')

    while True:
        if utilities.getStatus.getStatus(vm_name) == 'Running':
            break
        else:
            continue
    print('执行第二个循环')
    vmid=utilities.getVMID.getVMID(vm_name,vm_location).replace('\r\n','')
    while True:
        print('开始获取IP地址')
        vmaddress=utilities.getAddress.getAddress(vm_name)
        if vmaddress != "null":

            config.ConfigWriter.VMConfWriter(vm_name, vmid, vm_cpunum, vm_ramsize, vmaddress, "null", "null",
                                             "null", vm_location, maturity_start_year, maturity_start_month,
                                             maturity_start_day, maturity_end_year, maturity_end_month,
                                             maturity_end_day)
            break
        else:
            continue


# guiwriter()