import func.vm_info.info_commander
vmname='test-vm-2'
vmloc='D:\VirtualMachine\Hyper-V'

output=func.vm_info.info_commander.vm_info_getVMID(vmname,vmloc)
print(output)