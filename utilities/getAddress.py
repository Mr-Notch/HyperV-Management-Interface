# -- coding: utf-8 --
import func.vm_info.info_commander
def getAddress(vmname):
<<<<<<< HEAD
    output=func.vm_info.info_commander.vm_info_getAddress(vmname).replace('\r\n','')
=======
    output=func.vm_info.info_commander.vm_info_getAddress(vmname).replace('\\r','').replace('\\n','')
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
    if "{}" in output:
        return "null"
    else:
        return output.replace('{','')

<<<<<<< HEAD
def getAddressIfVMStarted(vmname):
    output=func.vm_info.info_commander.vm_info_getAddressIfVMStarted(vmname).replace('\r\n','')
    if "{}" in output:
        return "null"
    else:
        return output.replace('{','')

# ttt=getAddress("sample-2016")
=======
# ttt=getAddress("test-vm-import")
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
# print(ttt)