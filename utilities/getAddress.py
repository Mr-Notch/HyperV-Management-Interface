# -- coding: utf-8 --
import func.vm_info.info_commander
def getAddress(vmname):
    output=func.vm_info.info_commander.vm_info_getAddress(vmname).replace('\\r','').replace('\\n','')
    if "{}" in output:
        return "null"
    else:
        return output.replace('{','')

# ttt=getAddress("test-vm-import")
# print(ttt)