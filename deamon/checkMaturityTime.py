# -- coding: utf-8 --
import json
import func.vm_control.control_commander
import datetime

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
        return 'Exceptions.Error'


# print(readJsonMaturityTime('_sample-2016'))
# print(nowTime())
def checkMaturityTime(vmname):
    MaturityTime = readJsonMaturityTime(vmname)

    if now_time > MaturityTime:
        func.vm_control.control_commander.vm_stop_default(vmname)
        now_time_new_wheels = datetime.date.today()
        # remove_time = now_time_new_wheels + datetime.timedelta(days=int(maturity_keep_time))
        # 求差公式
        if (now_time_new_wheels-datetime.date(*map(int,MaturityTime.split('-')))).days >= int(maturity_keep_time):

            return '到期超过7天，抹掉数据'

        # return '过期remove_time=' + str(remove_time)

        else:

            return '到期未超过7天，继续停机'
    else:
        return '未过期'


print(checkMaturityTime('_sample-2016'))
