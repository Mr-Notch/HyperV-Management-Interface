# -- coding: utf-8 --
import func.vm_create.create_commander
import func.vm_setter.set_commander

<<<<<<< HEAD
vmname = 'sample-win-2016'
ramsize = '2GB'
cpunum = '2'
vmswitchname = 'NAT'
vmloc = 'D:\\HyperV-Management-Interface-main\\VirtualMachine\\Hyper-V'
=======
vmname = 'test-vm-3'
ramsize = '2GB'
cpunum = '2'
vmswitchname = 'NATBridge'
vmloc = 'D:\VirtualMachine\Hyper-V'
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006


output = func.vm_create.create_commander.vm_create_vm(vmname, ramsize, cpunum, vmswitchname, vmloc)

if output == True:
    print('成功1')
else:
    print('失败1')

vhdsize = '30GB'
<<<<<<< HEAD
vhdloc = 'D:\\HyperV-Management-Interface-main\\VirtualMachine\\Hyper-V\\' + vmname # E:\VirtualMachine\Hyper-V\python_createvm_func_0
=======
vhdloc = 'D:\VirtualMachine\Hyper-V\\' + vmname # E:\VirtualMachine\Hyper-V\python_createvm_func_0
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
vhdname = vmname+'-'+vhdsize
vhdcontrollertype = 'IDE'
vhdcontrollernum = '0'
vhdcontrollerloc = '0'

output2 = func.vm_create.create_commander.vm_create_vhd_dynamic(vhdsize, vhdloc, vhdname)

if output2 == True:
    print('成功2')
else:
    print('失败2')

output3 = func.vm_setter.set_commander.vm_set_vhd(vmname,vhdloc,vhdname,vhdcontrollertype,vhdcontrollernum,vhdcontrollerloc)
if output3 == True:
    print('成功3')
else:
    print('失败3')

dvdcontrollernum = '0'
dvdcontrollerloc = '0'


<<<<<<< HEAD
isoloc='D:\\HyperV-Management-Interface-main\\VirtualMachine\\ISO\\win-server-2016-zhCn.iso'
=======
isoloc='D:\cn_windows_10_consumer_editions_version_1909_x64_dvd_76365bf8.iso'
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
# output4 = func.vm_setter.set_commander.vm_set_dvd(vmname,isoloc,dvdcontrollernum,dvdcontrollerloc)
output4 = func.vm_setter.set_commander.vm_set_dvd(vmname,isoloc,)
if output4 == True:
    print('成功4')
else:
    print('失败4')

