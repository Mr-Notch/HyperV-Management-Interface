# -- coding: utf-8 --
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import func.vm_control.control_commander
import Injector
sys_loc=Injector.getSysLocation()
# print(sys_loc)
vmname='test-vm-1'
exportloc='D:\VirtualMachine\Templates'
output1=func.vm_control.control_commander.vm_export(vmname,exportloc)

if output1 == True:
    print('成功1')
else:
    print('失败1')