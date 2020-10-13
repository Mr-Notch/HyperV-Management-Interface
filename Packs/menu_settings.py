# -- coding: utf-8 --

import platform, os, time
from colorama import Fore, Back, Style
import Packs.messages


def mysqlfx():
    print('')
    print('*** MySQL Settings ***')
    print('')
    print('We need MySQL Port / Address / UserName / Database')
    print('Please enter them carefully and separate them with commas')
    print(Style.BRIGHT + 'Example: 3306,localhost,root,hypervisorlinkdb')
    print('')
    print(Fore.YELLOW, Style.BRIGHT + 'Input these strings below.')
    mysqlstr = input(' Input: ')
    if len(mysqlstr) > 0:
        Packs.messages.currectmsg(mysqlstr)

        dickeys = ['Port', 'Address', 'UserName', 'Database']
        mysqllist = mysqlstr.split(",")

        return_dict = dict(map(lambda x, y: [x, y], dickeys, mysqllist))
        return return_dict

    elif mysqlstr != str():
        Packs.messages.wrongmsg()
        mysqlfx()
    else:
        Packs.messages.wrongmsg()
        mysqlfx()


def portfx():
    print('')
    print('*** Port Settings ***')
    print('')
    print('Type in the port you like below, do not set the same as other ports' + Style.BRIGHT + ' (Default: 6400)')
    print(Fore.YELLOW, Style.BRIGHT)
    portstr = input(' Input: ')
    if len(portstr) > 0:
        Packs.messages.currectmsg(portstr)
        return_dict = {'SRV-Port': portstr}
        return return_dict
    else:
        Packs.messages.wrongmsg()
        portfx()


def apifx():
    print('')
    print('*** API Settings ***')
    print('')
    print('Enter the API-Key you want, preferably a little more complicated. (More than 6 bit)')
    print(Fore.YELLOW, Style.BRIGHT)
    apikeystr = input(' Input: ')
    if len(apikeystr) < 6:
        Packs.messages.wrongmsg()
        apifx()
    else:
        Packs.messages.currectmsg(apikeystr)
        return_dict={'API-Key':apikeystr}
        return return_dict





#
# def setfx_status(status):
#     if status == True:
#         print()
#         print('Successfully setup default values! Now load Main-Thread...')
#         print('Welcome to use HyperVisor Link System')
#         return True
#
#     if status == False:
#         print('')
#         again = input('Well... Do you want to try again? (Type Y or N): ')
#         if again == "Y":
#             setupfx()
#         elif again == "N":
#             print('Now exit the main thread. Goodbye!')
#             exit(0)
#         else:
#             print('Invalid value. Exit the main thread. Goodbye!')
#             exit(0)
#         return False
#
#
# def setupfx():
#     def setfx_3() -> List[str]:
#         print('')
#         print('Step-3: MySQL Setting:')
#         print('Type-in your MySQL-SRV address (Default: localhost):')
#         mysqladdr=input('MySQL-Address: ')
#         if len(mysqladdr)>0:
#             print('MySQL-Address is '+mysqladdr)
#         else:
#             print('MySQL-Address is localhost')
#             mysqladdr="localhost"
#
#         print('')
#         print('Type-in your MySQL-SRV port (Default: 3306):')
#         mysqlport=input('MySQL-Port: ')
#         if len(mysqlport)>0:
#             print('MySQL-Port is '+mysqlport)
#         else:
#             print('MySQL-Port is 3306')
#
#         print('')
#         print('Type-in your MySQL-Database name (Default: HyperVisorLinkDB):')
#         mysqldb=input('MySQL-DatabaseName: ')
#         if len(mysqldb)>0:
#             print('MySQL-DatabaseName is '+mysqldb)
#         else:
#             print('MySQL-DatabaseName is HyperVisorLinkDB')
#             mysqldb="HyperVisorLinkDB"
#
#         print('')
#         print('Type-in your MySQL-SRV user name (Default: root):')
#         mysqlusr = input('MySQL-User: ')
#         if len(mysqlusr) > 0:
#             print('MySQL-User is ' + mysqlport)
#             setfx_status(True)
#             mysql_setting = [mysqladdr, mysqlport, mysqldb, mysqlusr]
#             return mysql_setting
#         else:
#             print('MySQL-User is root')
#             mysqlusr="root"
#             setfx_status(True)
#             mysql_setting = [mysqladdr, mysqlport, mysqldb, mysqlusr]
#             return mysql_setting
#
#     def setfx_2():
#         print('')
#         print('Step-2: System setting')
#         print('Please check the computer information')
#         print('')
#         print('System information: '+str(platform.platform()))
#         print('System arch: '+str(platform.architecture()))
#         print('Computer name: '+str(platform.node()))
#         print('Python version: '+str(platform.python_version()))
#         print('')
#         check=input('If this is OK, type Y to continue or N to finish the thread: ')
#         if check == "Y":
#             if platform.python_version() <= "3.8.2":
#                 print('No, python version too low. We need 3.8.3+. Your version is '+platform.python_version())
#                 print('Now finish the thread. Goodbye!')
#                 setfx_status(False)
#             else:
#                 print('No problem.')
#                 setfx_3()
#         elif check == "N":
#             print('Now finish the thread. Goodbye!')
#             setfx_status(False)
#         else:
#             print('Invalid value. Type it again.')
#             setfx_2()
#
#     def setfx_1() -> str:
#         print('')
#         print('Step-1: Port setting')
#         print('Type the host port (1-65536, Default: 6400)')
#
#         hostport=input("Port: ")
#
#         if hostport > "65536":
#             print('Invalid value. Type it again.')
#             setfx_1()
#         elif hostport < "1":
#             print('Invalid value. Type it again.')
#             setfx_1()
#         else:
#             print('Your host port is '+hostport)
#
#             setfx_2()
#             return hostport
#
#
#     setfx_1()
#
#     element=[setfx_3(),setfx_1()]
