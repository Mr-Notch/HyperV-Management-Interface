from MainInterface import it_hmi_location
import json

def VMConfReader(vm_name,type):
    path = it_hmi_location+'Config\\'+vm_name+'.json'
    with open(path, mode='r') as this:
        json_file = json.load(this)
        typora = json_file[type]
        return typora

# print(VMConfReader('2','vm.maturity.end.date'))