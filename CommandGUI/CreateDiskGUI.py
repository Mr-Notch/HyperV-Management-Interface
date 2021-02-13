# -- coding: utf-8 --
import utilities.RandomDice
import utilities.getAddress
import func.vm_create.create_commander
import func.vm_setter.set_commander
import config.ConfigWriter
import Injector

vmloc=Injector.getVMLocation()

def guiwriter():
    print('---------------')
    print('| Create-Disk |')
    print('---------------')
    print('')
    vm_name = input('VM Name (String) : ')
    vhd_size = input('VHD Size (Int64) : ')+'GB' # VHD大小
    vhd_loc = vmloc+vm_name
    vhd_name = vm_name+'-'+vhd_size

    output = func.vm_create.create_commander.vm_create_vhd_dynamic(vhd_size,vhd_loc,vhd_name)

    if output == True:
        print('成功1')
        output2 = func.vm_setter.set_commander.vm_set_vhd(vm_name,vhd_loc,vhd_name,'IDE','1','0')
        if output2:
            config.ConfigWriter.DiskConfigWriter(vm_name,vhd_size,vhd_loc,'IDE','1','0')
            print('成功2')
        else:
            print('失败2')
    else:
        print('失败1')

guiwriter()
