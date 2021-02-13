# -- coding: utf-8 --
import func.vm_control.control_commander
import func.vm_setter.set_commander


# templateloc='D:\VirtualMachine\Templates'
# templatename='test-vm-1'
# vmname='test-vm-2'
# vmloc='D:\VirtualMachine\Hyper-V'


output1=func.vm_control.control_commander.vm_import(templatename,templateloc,vmname,vmloc)
if output1 == True:
    print('成功1')
else:
    print('失败1')

cpunum='4'
# output2=func.vm_control.control_commander.vm_start(vmname)
output2=func.vm_setter.set_commander.vm_set_cpunum(vmname,cpunum)
if output2 == True:
    print('成功2')
else:
    print('失败2')

ramsize='4GB' # 这个设置内存必须是xGB。GB！！！誰再不写单位我就把你塞到马桶里
output3=func.vm_setter.set_commander.vm_set_ramsize_static(vmname,ramsize)
if output3 == True:
    print('成功3')
else:
    print('失败3')

output4=func.vm_control.control_commander.vm_start(vmname)
if output4 == True:
    print('成功3')
else:
    print('失败3')
