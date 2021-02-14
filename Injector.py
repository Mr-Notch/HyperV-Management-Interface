# -- coding: utf-8 --
import json
import time

import os




# HMI运行路径
sys_location = "D:\\HyperV-Management-Interface-main\\HyperV-Management-Interface-main\\"
# Hyper-V虚拟机存放路径
vm_location = "D:\\VirtualMachine\\Hyper-V\\"
# ISO镜像文件存放路径
iso_location = "D:\\HyperV-Management-Interface-main\\VirtualMachine\\ISO\\"
# 模板存放路径
template_location = "D:\\HyperV-Management-Interface-main\\VirtualMachine\\Templates\\"
# 虚拟机到期保持时间
maturity_keep_time = "7"
# 虚拟机超过到期保留时间后是否删除（若否则存放在虚拟机路径的recovery文件夹内）
maturity_delete_switch = True




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

def nowTime():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

def getMaturityKeepTime():
    return maturity_keep_time

def getMaturityDeleteSwitch():
    return maturity_delete_switch

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

