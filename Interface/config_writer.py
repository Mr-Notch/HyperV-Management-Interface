import json
import os
from MainInterface import it_hmi_location
from MainInterface import it_vm_location
from MainInterface import it_iso_location



def VMConfWriter(vm_name,vm_id,vm_cpu,vm_ram,vm_address_ipv4,vm_address_ipv6,vm_netsh_port_mirrored,vm_netsh_port_connect,vm_disk_controller_type,vm_disk_controller_number,vm_disk_controller_location,vm_disk_type,vm_disk_location,maturity_start_date,maturity_end_date):
    json_file = {
        'vm.name': vm_name,
        'vm.id': vm_id,
        'vm.cpu': vm_cpu,
        'vm.ram': vm_ram,
        'vm.address.ipv4': vm_address_ipv4,
        'vm.address.ipv6': vm_address_ipv6,
        'vm.location': it_vm_location+vm_name,
        'vm.maturity.start.date': maturity_start_date,
        'vm.maturity.end.date': maturity_end_date,
        'vm.netsh.ports': {
            vm_netsh_port_mirrored: vm_netsh_port_connect
        },
        'vm.disk': {
            vm_disk_location: {
                'vm.disk.controller.type': vm_disk_controller_type,
                'vm.disk.controller.number': vm_disk_controller_number,
                'vm.disk.controller.location': vm_disk_controller_location,
                'vm.disk.type': vm_disk_type
            }
        }
    }

    path = it_hmi_location+'Config\\'+vm_name+'.json'
    if not os.path.isfile(path):
        fd = open(path, mode='w', encoding='utf-8')
        fd.close()
        exist_switch = False
    elif os.path.isfile(path):
        exist_switch = True
    
    if exist_switch == False:
        json_data = json.dumps(json_file, indent=4)
        with open(path, mode='w') as this:
            this.write(json_data)
    else:
        with open(path, mode='r') as that:
            new_json_file = json.load(that)
            new_netsh_ports_dict = new_json_file['vm.netsh.ports']
            if vm_netsh_port_mirrored not in new_netsh_ports_dict.keys():
                new_netsh_ports_dict[vm_netsh_port_mirrored] = vm_netsh_port_connect

            new_disk_dict = new_json_file['vm.disk']
            if vm_disk_location not in new_disk_dict.keys():
                new_disk_dict[vm_disk_location] = {
                    'vm.disk.controller.type': vm_disk_controller_type,
                    'vm.disk.controller.number': vm_disk_controller_number,
                    'vm.disk.controller.location': vm_disk_controller_location,
                    'vm.disk.type': vm_disk_type
                }

        new_json_data = json.dumps(new_json_file, indent=4)
        with open(path, mode='w') as new_this:
            new_this.write(new_json_data)

# VMConfWriter('test','xxxx-xxxx-xxxx-xxxx','2','2GB','192.168.137.xxx','fe80::xxxx','25565','11111','IDE','0','1','VHDX','bbb\\xxx.vhdx','2021-02-18','2021-03-01')


