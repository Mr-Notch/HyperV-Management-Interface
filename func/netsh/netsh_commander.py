import subprocess
def netsh_createMirrorPort(listenport, connectaddress, connectport):
    output = subprocess.Popen(
        ['powershell.exe', "../vm_create/create_recovery.ps1" + ' ' + listenport + ' ' + connectaddress + ' ' + connectport],
        stdout=subprocess.PIPE)
    dt = output.stdout.read()
    popen_call = subprocess.call
    if popen_call == 0:
        print('stdout_err')
        return False

    else:
        print('successes')
        return True

def netsh_removeMirrorPort(listenport, connectaddress, connectport):
    output = subprocess.Popen(
        ['powershell.exe', "../vm_create/create_recovery.ps1" + ' ' + listenport + ' ' + connectaddress + ' ' + connectport],
        stdout=subprocess.PIPE)
    dt = output.stdout.read()
    popen_call = subprocess.call
    if popen_call == 0:
        print('stdout_err')
        return False

    else:
        print('successes')
        return True