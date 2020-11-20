# -- coding: utf-8 --
import func.vm_create.create_commander
import func.vm_set.set_commander

vmname = 'python_createvm_func_1'
ramsize = '2GB'
cpunum = '2'
vmswitchname = 'vmnet'
vmloc = 'E:\VirtualMachine\Hyper-V'


output = func.vm_create.create_commander.vm_create_vm(vmname, ramsize, cpunum, vmswitchname, vmloc)

if output == True:
    print('成功1')
else:
    print('失败1')

vhdsize = '10GB'
vhdloc = 'E:\VirtualMachine\Hyper-V\\' + vmname # E:\VirtualMachine\Hyper-V\python_createvm_func_0
vhdname = vmname+'-'+vhdsize

output2 = func.vm_create.create_commander.vm_create_vhd_dynamic(vhdsize, vhdloc, vhdname)

if output2 == True:
    print('成功2')
else:
    print('失败2')

output3 = func.vm_set.set_commander.vm_set_vhd(vmname,vhdloc,vhdname)
if output3 == True:
    print('成功3')
else:
    print('失败3')

isoloc='E:\系统镜像\Windows_InsiderPreview_Server_vNext_zh-cn_20257.iso'
output4 = func.vm_set.set_commander.vm_set_dvd(vmname,isoloc)
if output3 == True:
    print('成功4')
else:
    print('失败4')

