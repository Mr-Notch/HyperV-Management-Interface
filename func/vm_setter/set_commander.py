# -- coding: utf-8 --
import subprocess
import Injector
sys_path=Injector.getSysLocation()

def vm_set_computer_name(vmname, vmloc, username, userpasswd):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_setter/set_computer_name.ps1" + ' ' + vmname + ' ' + vmloc + ' ' + username + ' ' + userpasswd],
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

# def vm_set_dvd(vmname, isoloc, dvdcontrollernum, dvdcontrollerloc):
def vm_set_dvd(vmname, isoloc):
    # output = subprocess.Popen(['powershell.exe', "../func/vm_setter/set_dvd.ps1" + ' ' + vmname + ' ' + isoloc+' '+dvdcontrollernum+' '+dvdcontrollerloc], stdout=subprocess.PIPE)
    output = subprocess.Popen(['powershell.exe',
                               sys_path+"func/vm_setter/set_dvd.ps1" + ' ' + vmname + ' ' + isoloc + ' '],
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

def vm_set_vhd(vmname, vhdloc, vhdname, vhdcontrollertype, vhdcontrollernum, vhdcontrollerloc):
    output = subprocess.Popen(['powershell.exe', sys_path+"func/vm_setter/set_vhd.ps1" + ' ' + vmname + ' ' + vhdloc+' '+vhdname+' '+vhdcontrollertype+' '+vhdcontrollernum+' '+vhdcontrollerloc], stdout=subprocess.PIPE)
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


def vm_set_ramsize_static(vmname, ramsize):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_setter/set_ramsize_static.ps1" + ' ' + vmname + ' ' + ramsize],
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

def vm_set_ramsize_dynamic(vmname, ramsize):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_setter/set_ramsize_dynamic.ps1" + ' ' + vmname + ' ' + ramsize],
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

def vm_set_cpunum(vmname, cpunum):
    output = subprocess.Popen(
        ['powershell.exe', sys_path+"func/vm_setter/set_cpunum.ps1" + ' ' + vmname + ' ' + cpunum],
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