import func.vm_info.info_commander


# vmname='test-vm-2'
# vmloc='D:\VirtualMachine\Hyper-V'

def getVMID(vmname, vmloc):
    output = func.vm_info.info_commander.vm_info_getVMID(vmname, vmloc)
    return output
