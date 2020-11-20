# -- coding: utf-8 --
import subprocess


def vm_delete_vhd(vmname,vhdname,vmloc):
    output = subprocess.Popen(['powershell.exe', "../func/vm_delete/delete_vm.ps1" + ' ' + vmname+' '+vhdname+' '+vmloc], stdout=subprocess.PIPE)
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

def vm_delete_vm(vmname,vmloc):
    output = subprocess.Popen(['powershell.exe', "../func/vm_delete/delete_vm.ps1" + ' ' + vmname+' '+vmloc], stdout=subprocess.PIPE)
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