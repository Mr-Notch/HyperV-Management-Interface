# -- coding: utf-8 --
import json
import func.vm_control.control_commander
import func.vm_delete.delete_commander
import datetime
import deamon.mailSender
import config.ConfigWriter

import Injector

sys_path = Injector.getSysLocation()
now_time = Injector.nowTime()
maturity_keep_time = Injector.getMaturityKeepTime()
maturity_delete_switch = Injector.getMaturityDeleteSwitch()


def readJsonMaturityTime(vmname):
    path = sys_path + 'config/vmconfig/' + vmname + '.json'
    try:
        with open(path, mode='r') as this:
            dict = json.load(this)
            maturity_end_dict = dict['vm.maturity.end']
            # 读取到期时间字典的年月日值
            maturity_end_year = maturity_end_dict['maturity.end.year']
            maturity_end_month = maturity_end_dict['maturity.end.month']
            maturity_end_day = maturity_end_dict['maturity.end.day']
            # 格式化到期时间
            if int(maturity_end_month) <= 9 and maturity_end_month.startswith('0'):
                if int(maturity_end_day) <=9 and maturity_end_day.startswith('0'):
                    return maturity_end_year + '-' + maturity_end_month + '-' + maturity_end_day
                elif int(maturity_end_day) <=9 and not maturity_end_day.startswith('0'):
                    return maturity_end_year + '-' + maturity_end_month + '-' + '0' + maturity_end_day
                elif int(maturity_end_day) > 9:
                    return maturity_end_year + '-' + maturity_end_month + '-' + maturity_end_day
            elif int(maturity_end_month) <= 9 and not maturity_end_month.startswith('0'):
                if int(maturity_end_day) <= 9 and maturity_end_day.startswith('0'):
                    return maturity_end_year + '-' + '0' + maturity_end_month + '-' + maturity_end_day
                elif int(maturity_end_day) <= 9 and not maturity_end_day.startswith('0'):
                    return maturity_end_year + '-' + '0' + maturity_end_month + '-' + '0' + maturity_end_day
                elif int(maturity_end_day) > 9:
                    return maturity_end_year + '-' + '0' +  maturity_end_month + '-' + maturity_end_day
                # return maturity_end_year + '-' + '0' + maturity_end_month + '-' + maturity_end_day
            elif int(maturity_end_month) > 9:
                if int(maturity_end_day) <= 9 and maturity_end_day.startswith('0'):
                    return maturity_end_year + '-' + maturity_end_month + '-' + maturity_end_day
                elif int(maturity_end_day) <= 9 and not maturity_end_day.startswith('0'):
                    return maturity_end_year + '-' + maturity_end_month + '-' + '0' + maturity_end_day
                elif int(maturity_end_day) > 9:
                    return maturity_end_year + '-' + maturity_end_month + '-' + maturity_end_day
                # return maturity_end_year + '-' + maturity_end_month + '-' + maturity_end_day



    except Exception as e:
        return e

def readJsonStartTime(vmname):
    path = sys_path + 'config/vmconfig/' + vmname + '.json'
    try:
        with open(path, mode='r') as this:
            dict = json.load(this)
            maturity_start_dict = dict['vm.maturity.start']
            maturity_start_year = maturity_start_dict['maturity.start.year']
            maturity_start_month = maturity_start_dict['maturity.start.month']
            maturity_start_day = maturity_start_dict['maturity.start.day']
            return maturity_start_year+'-'+maturity_start_month+'-'+maturity_start_day
    except Exception as e:
        return e

def readJsonVMConfig(vmname):
    path = sys_path + 'config/vmconfig/' + vmname + '.json'
    try:
        with open(path, mode='r') as this:
            dict = json.load(this)
            vm_cpu_number = dict['vm.cpu.number']
            vm_ram_size = dict['vm.ran.size']

            return vm_cpu_number+' CPU Core(s) - '+vm_ram_size+' RAM GB(s)'
    except Exception as e:
        return e

def readJsonConnectConfig(vmname):
    path = sys_path + 'config/portconfig/' + vmname + '.json'
    try:
        with open(path, mode='r') as this:
            dict = json.load(this)
            o=list(dict.keys())
            # print(o[1:])
            # vm_ram_size = dict['vm.ran.size']

            return str(o[1:])
    except Exception as e:
        return e

# print(readJsonConnectConfig("ecs-5Ap23"))

# print(readJsonMaturityTime('_sample-2016'))
# print(nowTime())
def checkMaturityTime(vmname):
    StartTime = readJsonStartTime(vmname)
    MaturityTime = readJsonMaturityTime(vmname)
    vmloc=Injector.getVMLocation()
    vmconfig= readJsonVMConfig(vmname)
    connectconfig=readJsonConnectConfig(vmname)

    if now_time == MaturityTime:
        deamon.mailSender.mailSender(Injector.smtp_receiver_user, "Finish-MaturityTime", vmname, StartTime,
                                     MaturityTime,
                                     vmconfig, connectconfig)

    if now_time > MaturityTime:
        func.vm_control.control_commander.vm_stop_default(vmname)

        now_time_new_wheels = datetime.date.today()
        # remove_time = now_time_new_wheels + datetime.timedelta(days=int(maturity_keep_time))
        # 求差公式
        if (now_time_new_wheels-datetime.date(*map(int,MaturityTime.split('-')))).days >= int(maturity_keep_time):

            func.vm_delete.delete_commander.vm_delete_vm(vmname,vmloc)

            config.ConfigWriter.deleteVMConfig(vmname)
            config.ConfigWriter.deletePortConfig(vmname)
            config.ConfigWriter.deleteDiskConfig(vmname)
            deamon.mailSender.mailSender(Injector.smtp_receiver_user,"Delete-VM",vmname,StartTime,MaturityTime,vmconfig,connectconfig)
            print('到期超过7天，抹掉数据')
            return '到期超过7天，抹掉数据'

        # return '过期remove_time=' + str(remove_time)

        else:
            func.vm_control.control_commander.vm_stop_default(vmname)
            print('到期未超过7天，继续停机')
            return '到期未超过7天，继续停机'
    else:
        print('未过期')
        return '未过期'



# print(checkMaturityTime('_sample-2016'))
