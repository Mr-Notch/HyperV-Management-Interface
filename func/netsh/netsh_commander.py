import subprocess
import Injector

sys_path = Injector.getSysLocation()


def netsh_createMirrorPort(listenport, connectaddress, connectport):
    output = subprocess.Popen(
        ['powershell.exe',
         sys_path + "func/netsh/netsh_createMirrorPort.ps1" + ' ' + listenport + ' ' + connectaddress + ' ' + connectport],
        stdout=subprocess.PIPE)
    dt = output.stdout.read()
    popen_call = subprocess.call
    if popen_call == 0:
        print('stdout_err')
        return False

    else:
        print('successes')
        return True


def netsh_removeMirrorPort(listenport):
    output = subprocess.Popen(
        ['powershell.exe',
         sys_path + "func/netsh/netsh_removeMirrorPort.ps1" + ' ' + listenport],
        stdout=subprocess.PIPE)
    dt = output.stdout.read()
    popen_call = subprocess.call
    if popen_call == 0:
        print('stdout_err')
        return False

    else:
        print('successes')
        return True
