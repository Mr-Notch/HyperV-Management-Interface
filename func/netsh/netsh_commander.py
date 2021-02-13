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


<<<<<<< HEAD
def netsh_removeMirrorPort(listenport):
    output = subprocess.Popen(
        ['powershell.exe',
         sys_path + "func/netsh/netsh_removeMirrorPort.ps1" + ' ' + listenport],
=======
def netsh_removeMirrorPort(listenport, connectaddress, connectport):
    output = subprocess.Popen(
        ['powershell.exe',
         sys_path + "func/netsh/netsh_createMirrorPort.ps1" + ' ' + listenport + ' ' + connectaddress + ' ' + connectport],
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
        stdout=subprocess.PIPE)
    dt = output.stdout.read()
    popen_call = subprocess.call
    if popen_call == 0:
        print('stdout_err')
        return False

    else:
        print('successes')
        return True
