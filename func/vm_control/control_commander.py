# -- coding: utf-8 --
import subprocess


def vm_export(vmname, exportloc):
    output = subprocess.Popen(['powershell.exe', "../func/vm_control/vm_export.ps1" + ' ' + vmname + ' ' + exportloc],
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

# vm_export('test_244','D:\VMachines\Hyper-V\outputVM')

def vm_import(templatename, templateloc, vmname, vmloc):
    output = subprocess.Popen(
        ['powershell.exe', "../func/vm_control/vm_import.ps1" + ' ' + templatename + ' ' + templateloc + ' ' + vmname + ' ' + vmloc],
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

def vm_start(vmname):
    output = subprocess.Popen(['powershell.exe', "../func/vm_control/vm_start.ps1" + ' '+vmname],stdout=subprocess.PIPE)
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

def vm_stop_default(vmname):
    output = subprocess.Popen(['powershell.exe', "../func/vm_control/vm_stop_default.ps1" + ' '+vmname],stdout=subprocess.PIPE)
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

def vm_stop_force(vmname):
    output = subprocess.Popen(['powershell.exe', "../func/vm_control/vm_stop_force.ps1" + ' '+vmname],stdout=subprocess.PIPE)
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

def vm_stop_save(vmname):
    output = subprocess.Popen(['powershell.exe', "../func/vm_control/vm_stop_save.ps1" + ' '+vmname],stdout=subprocess.PIPE)
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