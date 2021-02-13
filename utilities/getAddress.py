# -- coding: utf-8 --
import func.vm_info.info_commander
def getAddress(vmname):
    output=func.vm_info.info_commander.vm_info_getAddress(vmname).replace('\r\n','')
    if "{}" in output:
        return "null"
    else:
        return output.replace('{','')

def getAddressIfVMStarted(vmname):
    output=func.vm_info.info_commander.vm_info_getAddressIfVMStarted(vmname).replace('\r\n','')
    if "{}" in output:
        return "null"
    else:
        return output.replace('{','')

# ttt=getAddress("sample-2016")
# print(ttt)