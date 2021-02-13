# -- coding: utf-8 --
import json

import os





<<<<<<< HEAD
sys_location = "D:\\HyperV-Management-Interface-main\\HyperV-Management-Interface-main\\"
vm_location = "D:\\VirtualMachine\\Hyper-V\\"
iso_location = "D:\\HyperV-Management-Interface-main\\VirtualMachine\\ISO\\"
template_location = "D:\\HyperV-Management-Interface-main\\VirtualMachine\\Templates\\"

=======
sys_location = "C:\\Users\\HGR\\Documents\\PhantomHyper\\"
vm_location = "D:\\VirtualMachine\\Hyper-V\\"
iso_location = "D:\\"
template_location = "D:\\VirtualMachine\\Templates\\"
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006


def getSysLocation():
    sysloc = sys_location
    return sysloc

def getVMLocation():
    vmloc = vm_location
    return vmloc

def getISOLocation():
    isoloc = iso_location
    return isoloc

def getTemLoc():
    temloc = template_location
    return temloc


main_config = {
    "hmi.system.location": sys_location,
    "hmi.system.func.location": sys_location + '\\func',
    "hmi.system.utilities.location": sys_location + '\\utilities',
    "hmi.system.config.location": sys_location + '\\config',
    "hmi.vm.location": sys_location + '\_Files\VTs',
    "hmi.iso.location": sys_location + '\_Files\iso',
    "hmi.template.location": sys_location + '\_Files\\templates',
    "hmi.system.interface": "PowerShell"
}

path = sys_location + "\hmi.json"
if not os.path.isfile(path):
    fd = open(path, mode="w", encoding="utf-8")
    fd.close()
    # with open(path, 'r') as this:
    #     json_data=json.load(this)
json_data = json.dumps(main_config, indent=4)
with open(path, mode="w") as this:
    this.write(json_data)

