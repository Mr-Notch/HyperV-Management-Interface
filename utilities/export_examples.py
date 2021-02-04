# -- coding: utf-8 --
import func.vm_control.control_commander

vmname='test-vm-1'
exportloc='D:\VirtualMachine\Templates'
output1=func.vm_control.control_commander.vm_export(vmname,exportloc)

if output1 == True:
    print('成功1')
else:
    print('失败1')