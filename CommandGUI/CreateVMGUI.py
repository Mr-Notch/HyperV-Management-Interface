# -- coding: utf-8 --
import func.vm_create.create_commander
import func.vm_setter.set_commander
import func.vm_control.control_commander
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
        vmaddress=utilities.getAddress.getAddress(vm_name)
        if vmaddress != "null":
            break
        else:
            config.ConfigWriter.VMConfWriter(vm_name,vmid,vm_cpunum,vm_ramsize,vmaddress,"null","null","null",vm_location,maturity_start_year,maturity_start_month,maturity_start_day,maturity_end_year,maturity_end_month,maturity_end_day)
            continue


