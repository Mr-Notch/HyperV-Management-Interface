import sys
import time

def MainInjector():
    python_version = sys.version_info.major + sys.version_info.minor * 0.1
    if python_version < 3.8:
        print('Python 3.8+ is needed')
        raise Exception('Python version {} is too old'.format(python_version))
    try:
        
        from Interface.GUI import guiwriter
        
        # from Interface.hmi_server import HyperV_Management_Interface_Server
        # print(constants.requirements_installer())
        # print(PowershellActuator.catch_vm_getVMID('python_createvm_func_1'))
        # guiwriter.welcome_gui()
        
        guiwriter.main_gui()
        
    except Exception as e:
        return e