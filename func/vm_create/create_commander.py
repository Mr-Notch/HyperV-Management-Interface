# -- coding: utf-8 --
import subprocess
import Injector
sys_path=Injector.getSysLocation()

def vm_create_recovery(vmname, checkpointname):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_create/create_recovery.ps1" + ' ' + vmname + ' ' + checkpointname],
        stdout=subprocess.PIPE)
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

def vm_create_vhd_dynamic(vhdsize, vhdloc, vhdname):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_create/create_vhd_dynamic.ps1" + ' ' + vhdsize + ' ' + vhdloc + ' ' + vhdname],
        stdout=subprocess.PIPE)
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

def vm_create_vhd_static(vhdsize, vhdloc, vhdname):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_create/create_vhd_static.ps1" + ' ' + vhdsize + ' ' + vhdloc + ' ' + vhdname],
        stdout=subprocess.PIPE)
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

def vm_create_vm(vmname, ramsize, cpunum, vmswitchname, vmloc):
    output = subprocess.Popen(['powershell.exe',
                               sys_path+"func/vm_create/create_vm.ps1" + ' ' + vmname + ' ' + ramsize + ' ' + cpunum + ' ' + vmswitchname + ' ' + vmloc],
                              stdout=subprocess.PIPE)
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