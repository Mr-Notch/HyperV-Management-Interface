# -- coding: utf-8 --
import subprocess
import Injector
sys_path=Injector.getSysLocation()


def vm_remove_dvd(vmname, dvdcontrollernum, dvdcontrollerloc):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_remove/remove_dvd.ps1" + ' ' + vmname + ' ' + dvdcontrollernum+' '+dvdcontrollerloc], stdout=subprocess.PIPE)
    dt = output.stdout.read()

    popen_call = subprocess.call
    if popen_call == 0:
        # PIPE 未成功创建，返回False
        print('stdout_err')
        return False

    else:
        # PIPE 成功创建，返回True
        print('successes')
        return True

def vm_remove_vhd(vmname, vhdcontrollertype,vhdcontrollernum, vhdcontrollerloc):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_remove/remove_dvd.ps1" + ' ' + vmname + ' ' + vhdcontrollertype+' '+vhdcontrollernum+' '+vhdcontrollerloc], stdout=subprocess.PIPE)
    dt = output.stdout.read()

    popen_call = subprocess.call
    if popen_call == 0:
        # PIPE 未成功创建，返回False
        print('stdout_err')
        return False

    else:
        # PIPE 成功创建，返回True
        print('successes')
        return True

def vm_remove_vm(vmname):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_remove/remove_vm.ps1" + ' ' + vmname], stdout=subprocess.PIPE)
    dt = output.stdout.read()

    popen_call = subprocess.call
    if popen_call == 0:
        # PIPE 未成功创建，返回False
        print('stdout_err')
        return False

    else:
        # PIPE 成功创建，返回True
        print('successes')
        return True