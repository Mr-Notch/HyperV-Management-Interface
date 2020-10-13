# -- coding: utf-8 --
import pymysql, os, time, threading
import Packs.menu_settings, Packs.messages, Scripts.pwfunc
from colorama import Fore, Back, Style

'''
Injector 注入
提供从 Main 到 Func 的桥梁
'''


# Get-Settings
def settinginject():
    global mysqlout, portout, apiout
    Packs.messages.settingmsg()
    confirm_config2 = open('confirm_config.txt', 'w')
    confirm_config2.write('False')
    choise_sum = 0
    while True:
        if choise_sum == 3:
            print('Successfully to set.')
            break
        choise = input('Type-in the options in 1-3: ')
        choise_sum += 1

        if choise == '1':
            os.system("cls")
            mysqlout = Packs.menu_settings.mysqlfx()
            continue

        elif choise == '2':
            os.system("cls")
            portout = Packs.menu_settings.portfx()
            continue

        elif choise == '3':
            os.system("cls")
            apiout = Packs.menu_settings.apifx()
            time.sleep(0.3)
            continue

        else:
            Packs.messages.wrongmsg()
            Packs.messages.settingmsg()
            continue

    return mysqlout, portout, apiout


def controlinject():
    Packs.messages.controlmenumsg()
    while True:
        choise = input('Type-in the options in 1-5 or q to exit: ')

        if choise == '1':
            listvm = Scripts.pwfunc.listVM()
            continue
        elif choise == '2':
            startvmname = input('Type-in the value of the vmname: ')
            Packs.messages.runningmsg()
            startvm = Scripts.pwfunc.startVM(startvmname)
            continue
        elif choise == '3':
            stopvmname = input('Type-in the value of the vmname: ')
            forcestop = input('Should I execute force shutdown? (Y/N): ')
            if forcestop == 'Y':
                Packs.messages.runningmsg()
                time.sleep(0.3)
                forcestopvm = Scripts.pwfunc.stopVM_fo(stopvmname)
                time.sleep(0.3)
            elif forcestop == 'N':
                Packs.messages.runningmsg()
                time.sleep(0.3)
                slostopvm = Scripts.pwfunc.stopVM_sl(stopvmname)
                time.sleep(0.3)
            else:
                Packs.messages.wrongmsg()
            continue
        elif choise == '4':
            resetvmname = input('Type-in the value of the vmname: ')
            Packs.messages.runningmsg()
            resetvm = Scripts.pwfunc.resetVM(resetvmname)
            continue

        elif choise == '5':
            findervmname = input('Type-in the value of the vmname: ')
            findervm = Scripts.pwfunc.showVM(findervmname)
            continue

        elif choise == 'q':
            return True
        else:
            Packs.messages.wrongmsg()
            Packs.messages.controlmenumsg()
            continue
