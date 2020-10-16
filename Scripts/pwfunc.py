# -- coding: utf-8 --
import os, subprocess, chardet, time
import Packs.messages


# 尝试解决编码问题
def check_chardet(file_path):
    with open(file_path, "rb") as f:
        data = f.read(4)
        charset = chardet.detect(data)['encoding']
    return charset







# 查看VM
def showVM(vmname):
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\showVM.ps1 " + vmname])
    time.sleep(1)
    path = 'showVM-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('showVM-out.txt'):

        Packs.messages.finishmsg()
        os.remove('showVM-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('showVM-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# 开启VM
def startVM(vmname):
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\startVM.ps1 " + vmname])
    time.sleep(5)
    path = 'startVM-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('startVM-out.txt'):
        Packs.messages.finishmsg()
        os.remove('startVM-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('startVM-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# 温柔地关闭VM
def stopVM_sl(vmname):
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\stopVMsl.ps1 " + vmname])
    time.sleep(5)
    path = 'stopVM-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('stopVM-out.txt'):

        Packs.messages.finishmsg()
        os.remove('stopVM-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('showVM-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# 硬性关闭VM
def stopVM_fo(vmname):
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\stopVMfo.ps1 " + vmname])
    time.sleep(5)
    path = 'stopVM-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('stopVM-out.txt'):

        Packs.messages.finishmsg()
        os.remove('stopVM-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('stopVM-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# 重启VM
def resetVM(vmname):
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\\resetVM.ps1 " + vmname])
    time.sleep(7)
    path = 'resetVM-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('resetVM-out.txt'):

        Packs.messages.finishmsg()
        os.remove('resetVM-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('resetVM-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# 枚举所有VMs
def listVM():
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\\listVMs.ps1 "])
    time.sleep(5)
    path = 'listVMs-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('listVMs-out.txt'):
        Packs.messages.finishmsg()
        os.remove('listVMs-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('listVMs-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# 枚举网卡
def showVMSwitch():
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\\showVMSwitch.ps1 "])
    time.sleep(2)
    path = 'showVMSwitch-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('showVMSwitch-out.txt'):
        Packs.messages.finishmsg()
        os.remove('showVMSwitch-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('showVMSwitch-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

def newVM(vmname,ramsize,cpunum,vmswitchname,vmdiskname,vmdisksize,vmloc,isoloc):
    subprocess.Popen(["powershell.exe", ".\Scripts\pwscript\\newVM.ps1 " + vmname + ' ' + ramsize + ' ' + ' ' + cpunum + ' ' + vmswitchname + ' ' + vmdiskname + ' ' + vmdisksize + ' ' + vmloc + ' ' + isoloc])
    time.sleep(30)
    path = 'newVM-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('newVM-out.txt'):
        Packs.messages.finishmsg()
        os.remove('newVM-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('newVM-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# newVM('TEST3','1GB','2','TEST','C','10GB','D:\VMachines\Hyper-V','D:\迅雷下载\cn_windows_server_version_1909_updated_jan_2020_x64_dvd_cd782fbe.iso')

def importvmcopy(vmname,vmloc,templatename,templateloc):
    subprocess.Popen(["powershell.exe",".\Scripts\pwscript\\importVM-Copy.ps1 " + vmname + ' ' + vmloc + ' ' + ' ' + templatename + ' ' + templateloc])
    time.sleep(15)
    path = 'importVM_Copy-out.txt'
    with open(path, encoding=check_chardet(path)) as f:
        data = f.read()
        print(data)
    if os.path.exists('importVM_Copy-out.txt'):
        Packs.messages.finishmsg()
        os.remove('importVM_Copy-out.txt')
        time.sleep(1)
        return True
    else:
        time.sleep(3)
        if os.path.exists('importVM_Copy-out.txt'):
            Packs.messages.finishmsg()
            return True
        else:
            Packs.messages.faildmsg()
            return False

# importvmcopy('TEST6','D:\VMachines\Hyper-V','TEST2','D:\VMachines\Hyper-V\outputVM\TEST2\TEST2')