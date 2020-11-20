# -- coding: utf-8 --
import func.vm_control.control_commander


templateloc='E:\VirtualMachine\Hyper-V\\template\\test_sample'
templatename='test_277'
vmname='python_importvm_func_1'
vmloc='E:\VirtualMachine\Hyper-V'

output1=func.vm_control.control_commander.vm_import(templatename,templateloc,vmname,vmloc)
if output1 == True:
    print('成功1')
else:
    print('失败1')

output2=func.vm_control.control_commander.vm_start(vmname)
if output2 == True:
    print('成功2')
else:
    print('失败2')



