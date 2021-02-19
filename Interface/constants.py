import os
import subprocess

def requirements_installer():
    try:
        pipes = subprocess.Popen(['powershell.exe','pip freeze'],stdout=subprocess.PIPE)
        output = pipes.stdout.read().decode('GB2312')
        pipes_call = subprocess.call
        if pipes_call == 0:
            raise BrokenPipeError
        else:
            while True:
                if 'rich' not in output:
                    try:
                        # Install rich (GUI Needed)
                        os.system('pip install rich')
                        continue
                    except OSError as e:
                        return e
                elif 'colorama' not in output:
                    try:
                        # Install colorama (Colored Messages Needed)
                        os.system('pip install colorama')
                        continue
                    except OSError as e:
                        return e
                else:
                    return False
    except BrokenPipeError as e:
        return e



    
