import subprocess
import MainInterface

# ----------------------
# |  Actuator - catch  |
# ----------------------

def catch_disk_getDVD(vm_name,format):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\catch\\catch_disk_getDVD.ps1'+' '+vm_name+' '+format],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def catch_disk_getVHD(vm_name,format):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\catch\\catch_disk_getVHD.ps1'+' '+vm_name+' '+format],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def catch_vm_getAddress_ipv4(vm_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\catch\\catch_vm_getAddress_ipv4.ps1'+' '+vm_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode().replace(" ","")
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def catch_vm_getAddress_ipv6(vm_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\catch\\catch_vm_getAddress_ipv6.ps1'+' '+vm_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def catch_vm_getPowerStatus(vm_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\catch\\catch_vm_getPowerStatus.ps1'+' '+vm_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def catch_vm_getVMID(vm_name):
    # vm_loc 已经集成里面
    # 修改的话需要修改 MainInterface 里的 it_vm_location
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\catch\\catch_vm_getVMID.ps1'+' '+vm_name+' '+MainInterface.it_vm_location],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

# ---------------------
# |  Actuator - disk  |
# ---------------------

def disk_loadDVD(vm_name, iso_name):
    
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_loadDVD.ps1'+' '+vm_name+' '+MainInterface.it_iso_location+iso_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def disk_loadVHD(vm_name, vhd_name):
    
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_loadVHD.ps1'+' '+vm_name+' '+MainInterface.it_vm_location + vm_name+' '+vhd_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def disk_newVHD_dynamic(vhd_size, vhd_loc, vhd_name):
    # vhd_loc 需要在外部手动指定（例如C:\Hyper-V\xxx\）
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_newVHD_dynamic.ps1'+' '+vhd_size+' '+vhd_loc+' '+vhd_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def disk_newVHD_static(vhd_size, vhd_loc, vhd_name):
    # vhd_loc 需要在外部手动指定（例如C:\Hyper-V\xxx\）
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_newVHD_static.ps1'+' '+vhd_size+' '+vhd_loc+' '+vhd_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def disk_removeVHD(vhd_name, vhd_loc):
    # vhd_loc 需要在外部手动指定（例如C:\Hyper-V\xxx\）
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_removeVHD.ps1'+' '+vhd_name+' '+vhd_loc],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def disk_unloadDVD(vm_name, dvd_controller_num, dvd_controller_loc):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_unloadDVD.ps1'+' '+vm_name+' '+dvd_controller_num+' '+dvd_controller_loc],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def disk_unloadVHD(vm_name, vhd_controller_type, vhd_controller_num, vhd_controller_loc):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\disk\\disk_unloadVHD.ps1'+' '+vm_name+' '+vhd_controller_type+' '+vhd_controller_num+' '+vhd_controller_loc],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

# ----------------------
# |   Actuator - kms   |
# ----------------------

def kms_slmgr(vm_name,vm_login_user,vm_login_password):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\kms\\kms_slmgr.ps1'+' '+vm_name+' '+vm_login_user+' '+vm_login_password],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e
        
# ----------------------
# |  Actuator - netsh  |
# ----------------------

def netsh_createMirrorPort(listen_port, connect_address, connect_port):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\netsh\\netsh_createMirrorPort.ps1'+' '+listen_port+' '+connect_address+' '+connect_port],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def netsh_removeMirrorPort(listen_port):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\netsh\\netsh_removeMirrorPort.ps1'+' '+listen_port],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def network_vm_createMirrorPort(listen_port, connect_address, connect_port, protocol):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\network\\network_vm_createMirrorPort.ps1'+' '+MainInterface.it_nat_name+' '+listen_port+' '+connect_address+' '+connect_port+' '+protocol],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

<<<<<<< HEAD
def network_vm_setIPAddress_ipv4(vm_name,ipaddr_v4,ipaddr_gateway,ipaddr_dns):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\network\\network_vm_setIPAddress_ipv4.ps1'+' '+vm_name+' '+ipaddr_v4+' '+ipaddr_gateway+' '+ipaddr_dns],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

=======
>>>>>>> 8291ecbd3c59516c3ac439ec0cd2a1231e6695ae
# -------------------
# |  Actuator - vm  |
# -------------------

def vm_exportVM(vm_name):
    # export_loc 为 MainInterface 里的 it_template_location
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_exportVM.ps1'+' '+vm_name+' '+MainInterface.it_template_location],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_importVM(template_name, vm_name):
    # template_loc 为 MainInterface 里的 it_template_location
    # vm_loc 为 MainInterface 里的 it_vm_location
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_importVM.ps1'+' '+template_name+' '+MainInterface.it_template_location+' '+vm_name+' '+MainInterface.it_vm_location],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_newRecovery(vm_name, recovery_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_newRecovery.ps1'+' '+vm_name+' '+recovery_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_newVM(vm_name, vm_ram, vm_cpu, vm_switch_name):
    # vm_loc 为 MainInterface 里的 it_vm_location
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_newVM.ps1'+' '+vm_name+' '+vm_ram+' '+vm_cpu+' '+vm_switch_name+' '+MainInterface.it_vm_location],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_removeVM(vm_name):
    # vm_loc 为 MainInterface 里的 it_vm_location
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_removeVM.ps1'+' '+vm_name+' '+MainInterface.it_vm_location],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_setComputerNameToVMID(vm_name, vm_login_user, vm_login_password):
    # vm_loc 为 MainInterface 里的 it_vm_location
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_setComputerNameToVMID.ps1'+' '+vm_name+' '+MainInterface.it_vm_location+' '+vm_login_user+' '+vm_login_password],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_setCPU(vm_name, vm_cpu):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_setCPU.ps1'+' '+vm_name+' '+vm_cpu],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_setRAM_dynamic(vm_name, vm_ram):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_setRAM_dynamic.ps1'+' '+vm_name+' '+vm_ram],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_setRAM_static(vm_name, vm_ram):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_setRAM_static.ps1'+' '+vm_name+' '+vm_ram],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_startVM(vm_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_startVM.ps1'+' '+vm_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_stop_conventional(vm_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_stop_conventional.ps1'+' '+vm_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

def vm_stop_force(vm_name):
    try:
        pipes = subprocess.Popen(['powershell.exe',MainInterface.it_hmi_location+'Interface\\Actuator\\vm\\vm_stop_force.ps1'+' '+vm_name],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            return output
    except BrokenPipeError as e:
        return e

