# -- coding: utf-8 --
# HyperVisor Link
# 主类注入加载入口

import os, time, sys, random
from colorama import Fore, Back, Style
import Packs.messages
import Packs.injector

time.sleep(1)


# 初始化状态函数
def statusfx(bool):
    status = bool
    return status


# 初始化安装函数
def inslib():
    libs = {"chardet", "colorlog", "requests", "ruamel.yaml", "pymysql"}
    print("")
    print(Fore.YELLOW + "*** Auto-Installer will start in 5 sec ***")
    print("")
    time.sleep(5)
    try:
        for lib in libs:
            os.system("pip install " + lib)
            print(Style.RESET_ALL)
    except:
        print("Something wrong! Please check your python & pip path")
        print(Style.RESET_ALL)


# 初始化帮助菜单函数
def mainmenu():
    Packs.messages.mainmenumsg()
    while True:
        choise=input('Type-in the option of your choise: ')
        if choise == '1':
            inslib()
            print(Fore.YELLOW + 'If its successful, please restart the daemon.')
            print(Fore.YELLOW + 'Daemon will be killed in 2 sec.')
            print(Style.RESET_ALL)
            time.sleep(2)
            exit(0)
            break

        elif choise == '2':
            settingmenu_output = Packs.injector.settinginject()
            print('')
            print(settingmenu_output)
            print('')
            if settingmenu_output:
                confirm_config = open('Config/confirm_config.txt', 'w')
                confirm_config.write('True')
                inf_config = open('Config/inf_config.txt', 'w')
                inf_config.write(str(settingmenu_output))
                time.sleep(1)
                print(Fore.YELLOW + 'If its successful, please restart the daemon.')
                print(Fore.YELLOW + 'Daemon will be killed in 2 sec.')
                print(Fore.YELLOW + 'By the way, you can also modify it in the "./Config/inf_config.txt".')
                print(Style.RESET_ALL)
                time.sleep(2)
                exit(0)
                break
            else:
                confirm_config = open('Config/confirm_config.txt', 'w')
                confirm_config.write('False')
                time.sleep(1)
                print(Fore.YELLOW + 'Oops... There were something wrong in the settings.')
                print(Fore.YELLOW + 'Daemon will be killed in 2 sec. Although you need to reset them')
                print(Fore.YELLOW + 'By the way, you can also modify them in the "./Config/inf_config.txt".')
                print(Style.RESET_ALL)
                time.sleep(2)
                exit(0)
                break


        elif choise == '3':
            print('Web Panel')

        elif choise == '4':
            if Packs.injector.controlinject() == True:
                Packs.messages.mainmenumsg()
                continue
            else:
                Packs.messages.errormsg()
                time.sleep(2)
                exit(0)
                break









# def helper():
#     global choise
#     choise = False
#     print("")
#     print("HyperVisor Link Main Helper:")
#     print("----------------------------")
#     print("1: Install request libs")
#     print("2: Set-up settings")
#     print("3: Force start-up")
#     print("q: Stop thread")
#     print("----------------------------")
#     confirm_files = open('Packs/confirm_config.txt', 'w')
#     confirm_choise = confirm_files.read()
#     if confirm_choise == 'True':
#         choise = input("Type-in your choise: ")
#         print("")
#
#     elif confirm_choise == 'False':
#         # Packs.injector.settinginject()
#         print('ee')
#
#     if choise == "1":
#         inslib()
#     elif choise == "2":
#         # Packs.injector.settinginject()
#         print('e')
#     elif choise == "3":
#         print(Back.LIGHTYELLOW_EX,
#               Fore.RED + '---------------------------------------------------------------------' + Style.RESET_ALL)
#         print(Back.LIGHTYELLOW_EX,
#               Fore.RED + 'Are you sure you want to do this? May cause serious errors... (Y/N)  ' + Style.RESET_ALL)
#         print(Back.LIGHTYELLOW_EX,
#               Fore.RED + '---------------------------------------------------------------------' + Style.RESET_ALL)
#         print(Style.RESET_ALL)
#         confirm = input('Type Y/N: ')
#         if confirm == "Y":
#             print('Confirmed!')
#         elif confirm == "N":
#             print('Cancelled!')
#             helper()
#         else:
#             print('Invalid value. Cancelled!')
#             helper()
#
#     elif choise == "q":
#         exit(0)
#     else:
#         print('Invalid value. Try again.')
#         helper()


# for i in range(101):
#     loadnum=random.uniform(0.1,0.2)
#     loadsty={'-','/','|','\\'}
#     for j in loadsty:
#         print('\rProgress: {:^3.0f}%'.format((i/101)*101),' '+j,end='')
#         time.sleep(loadnum)

mainmenu()
