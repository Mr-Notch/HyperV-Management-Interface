import telnetlib
import time
from MainInterface import it_telnet_address
from MainInterface import it_telnet_password
from MainInterface import it_telnet_user

def execute_func(command):
    tn=telnetlib.Telnet(it_telnet_address)
    tn.open(it_telnet_address,port=23)

    tn.read_until(b'Login:',timeout=10)
    tn.write(it_telnet_user.encode('ascii')+b'\n')
    tn.read_until(b'Password:',timeout=10)
    tn.write(it_telnet_password.encode('ascii')+b'\n')

    time.sleep(3)

    tn.write(command.encode('ascii')+b'\n')

    result=tn.read_very_eager().decode('ascii')
    return result

# print(execute_func(it_telnet_address,it_telnet_user,it_telnet_password,'nat port mapping add interface wan1 protocol TCP/UDP external-port 1200 internal-ip 192.168.2.202 internal-port 3389'))
