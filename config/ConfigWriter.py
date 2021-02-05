# -- coding: utf-8 --
import json
import os
# from collections import defaultdict, OrderedDict

# vmname = 'test'
# maturity_start_year = '2021'
# maturity_start_month = '2'
# maturity_start_day = '1'
# maturity_end_year = '2022'
# maturity_end_month = '3'
# maturity_end_day = '1'
# end_time = '2022-3-5'
# vmid = 'xxxxx-xxxxx-xxxxx-xxxxx-xxxxx'
# vmcpunum = '2'
# vmramsize = '3'
# network_ipv4addr = '192.168.137.xxx'
# network_ipv6addr = 'fe80:xxxx:xxxx:xxxx:xxxx:xxxx'
# network_macaddr = '00:xx:xx:xx:xx:xx'
# os_version = 'Windows 10 2004'
# locate_location = 'D:\\HM\\VM\\' + vmname
import Injector
sys_path = Injector.getSysLocation()

def VMConfWriter(vmname, vmid, vmcpunum, vmramsize, network_ipv4addr, network_ipv6addr, network_macaddr, os_version,
                 locate_location,
                 maturity_start_year, maturity_start_month, maturity_start_day, maturity_end_year, maturity_end_month,
                 maturity_end_day):
    # time_dict=defaultdict(list)
    # time_dict["maturity.start"].append(maturity_start)
    # time_dict["maturity.end"].append(maturity_end)

    # mirror_dict = defaultdict(list)
    # 端口映射暂时存到另一个文件里面

    json_file = {
        "vm.maturity.start": {
            "maturity.start.year": maturity_start_year,
            "maturity.start.month": maturity_start_month,
            "maturity.start.day": maturity_start_day,
        },
        "vm.maturity.end": {
            "maturity.end.year": maturity_end_year,
            "maturity.end.month": maturity_end_month,
            "maturity.end.day": maturity_end_day,
        },
        "vm.name": vmname,
        "vm.id": vmid,
        "vm.cpu.number": vmcpunum,
        "vm.ran.size": vmramsize,
        "vm.network.ipv4addr": network_ipv4addr,
        "vm.network.ipv6addr": network_ipv6addr,
        "vm.network.macaddr": network_macaddr,
        "vm.os.version": os_version,
        "vm.locate.location": locate_location,

    }

    path = sys_path+"config/vmconfig/" + vmname + ".json"
    if not os.path.isfile(path):
        fd = open(path, mode="w", encoding="utf-8")
        fd.close()
    # with open(path, 'r') as this:
    #     json_data=json.load(this)
    json_data = json.dumps(json_file, indent=4)
    with open(path, mode="w") as this:
        this.write(json_data)


# VMConfWriter(vmname, vmid, vmcpunum, vmramsize, network_ipv4addr, network_ipv6addr, network_macaddr, os_version, locate_location,
#               maturity_start_year, maturity_start_month, maturity_start_day, maturity_end_year, maturity_end_month,
#               maturity_end_day)

# disk_size = '20GB'
# disk_location = 'D:\\HMI\\VM\\' + vmname + '\\Virtual Hard Disks\\' + vmname + '.vhdx'
# disk_connector_type = 'IDE'
# disk_connector_num = '0'
# disk_connector_loc = '2'


def DiskConfigWriter(vmname, disk_size, disk_location, disk_connector_type, disk_connector_num, disk_connector_loc):
    global exist_switch
    json_file = {
        "vmname": vmname,
        disk_connector_type + "." + disk_connector_num + "." + disk_connector_loc: {
            "disk.location": disk_location,
            "disk.size": disk_size,
            "disk.connector.type": disk_connector_type,
            "disk.connector.num": disk_connector_num,
            "disk.connector.loc": disk_connector_loc
        }
    }
    path = "./diskconfig/" + vmname + ".json"
    if not os.path.isfile(path):
        fd = open(path, mode="w", encoding="utf-8")
        fd.close()
        exist_switch = False
    elif os.path.isfile(path):
        exist_switch = True

    if exist_switch == False:
        json_data = json.dumps(json_file, indent=4)
        with open(path, mode="w") as this:
            this.write(json_data)
    else:
        with open(path, mode="r") as that:
            new_json_file = json.load(that)
            new_json_file[disk_connector_type + "." + disk_connector_num + "." + disk_connector_loc] = {
                "disk.location": disk_location,
                "disk.size": disk_size,
                "disk.connector.type": disk_connector_type,
                "disk.connector.num": disk_connector_num,
                "disk.connector.loc": disk_connector_loc
            }
        new_json_data = json.dumps(new_json_file, indent=4)
        with open(path, mode="w") as superthis:
            superthis.write(new_json_data)


# port_listen_port = '25565'
# port_connect_port = '22392'
# port_listen_address = '192.168.137.xxx'
# port_connect_address = '*'


# DiskConfigWriter(vmname,disk_size,disk_location,disk_connector_type,disk_connector_num,disk_connector_loc)
def PortConfigWriter(vmname, port_listen_port, port_connect_port, port_listen_address, port_connect_address):
    global exist_switch
    json_file = {
        "vmname": vmname,
        port_listen_port + "->" + port_connect_port: {
            "port.listen.port": port_listen_port,
            "port.connect.port": port_connect_port,
            "port.listen.address": port_listen_address,
            "port.connect.address": port_connect_address
        }
    }
    path = "./portconfig/" + vmname + ".json"
    if not os.path.isfile(path):
        fd = open(path, mode="w", encoding="utf-8")
        fd.close()
        exist_switch = False
    elif os.path.isfile(path):
        exist_switch = True

    if exist_switch == False:
        json_data = json.dumps(json_file, indent=4)
        with open(path, mode="w") as this:
            this.write(json_data)
    else:
        with open(path, mode="r") as that:
            new_json_file = json.load(that)
            new_json_file[port_listen_port + "->" + port_connect_port] = {
                "port.listen.port": port_listen_port,
                "port.connect.port": port_connect_port,
                "port.listen.address": port_listen_address,
                "port.connect.address": port_connect_address
            }
        new_json_data = json.dumps(new_json_file, indent=4)
        with open(path, mode="w") as superthis:
            superthis.write(new_json_data)


# PortConfigWriter(vmname,port_listen_port,port_connect_port,port_listen_address,port_connect_address)
