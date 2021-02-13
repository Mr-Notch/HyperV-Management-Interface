
# -- coding: utf-8 --
import func.vm_setter.set_commander

vm_name='ecs-4nz9V'
vm_loc='D:\\VirtualMachine\\Hyper-V'
username='Administrator'
userpasswd='Aa123456'

output = func.vm_setter.set_commander.vm_set_computer_name(vm_name,vm_loc,username,userpasswd)

if output == True:
    print('成功1')
else:
    print('失败1')