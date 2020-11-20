# -- coding: utf-8 --
import subprocess


def vm_set_computer_name(vmname, vmloc, username, userpasswd):
    output = subprocess.Popen(
        ['powershell.exe', "../func/vm_set/set_computer_name.ps1" + ' ' + vmname + ' ' + vmloc + ' ' + username + ' ' + userpasswd],
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

def vm_set_dvd(vmname, isoloc):
    output = subprocess.Popen(['powershell.exe', "../func/vm_set/set_dvd.ps1" + ' ' + vmname + ' ' + isoloc], stdout=subprocess.PIPE)
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

def vm_set_vhd(vmname, vhdloc, vhdname):
    output = subprocess.Popen(['powershell.exe', "../func/vm_set/set_vhd.ps1" + ' ' + vmname + ' ' + vhdloc+' '+vhdname], stdout=subprocess.PIPE)
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