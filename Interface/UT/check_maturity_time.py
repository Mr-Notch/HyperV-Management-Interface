import json
from datetime import date, timedelta
from Interface.Actuator import PowershellActuator
from Interface.UT import send_mail
from MainInterface import it_hmi_location
from MainInterface import it_mature_keep_time
from json.decoder import JSONDecodeError
# it_hmi_location='C:\\Users\\HGR\\Documents\\GitHub\\HyperV-Management-Interface\\'
# it_mature_keep_time=7

def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return date(int(year_s),int(mon_s),int(day_s))

def checkMaturityTime(vm_name):
    path = it_hmi_location+'Config\\'+vm_name+'.json'
    try:
        with open(path,mode='r') as this:
            dic = json.load(this)
    except JSONDecodeError as e:
        return e

    maturity_end_date = parse_ymd(dic['vm.maturity.end.date'])
    now_time = date.today()
    if now_time >= maturity_end_date:
        # 如果订购时间大于当前时间，则判断为已过期
        # 否则返回False
        # if maturity_end_date > now_time, then return True
        # else return False

        # print(now_time)
        # print(maturity_end_date)
        # print(maturity_end_date + timedelta(days=it_mature_keep_time))
        
        if now_time == maturity_end_date + timedelta(days=it_mature_keep_time):
            # print('已过期且超过7天')
            # already expired & out of keep time
            msg_2 = '----------------------------------'+'\n'+'虚拟机名称: '+vm_name+'\n'+'----------------------------------'+'\n'+'虚拟机已经到期且已经抹除数据, 系统已经回收资源'
            send_mail.sendMail('已抹掉虚拟机数据',msg_2)
            PowershellActuator.vm_removeVM(vm_name)
            return 2
        else:
            # print('已过期未超过7天')
            # already expired but not out of keep time
            msg_2 = '----------------------------------'+'\n'+'虚拟机名称: '+vm_name+'\n'+'虚拟机到期时间: '+str(maturity_end_date)+'\n'+'删除时间: '+str(maturity_end_date + timedelta(days=it_mature_keep_time))+'\n'+'到期保留天数: '+str(it_mature_keep_time)+'\n'+'----------------------------------'+'\n'+'虚拟机已到期, 但仍未超过保留天数, 请立即与虚拟机所有者取得联系'
            print(send_mail.sendMail('虚拟机已到期',msg_2))
            PowershellActuator.vm_stop_force(vm_name)
            return 1
    else:
        # print('未过期')
        # not expired
        return 0


# More Faster Than datetime.strptime():
'''
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))
print(parse_ymd('2021-03-01'))
# return datetime format.
# https://www.cnblogs.com/baxianhua/p/9934878.html
'''