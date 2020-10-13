# -- coding: utf-8 --

from colorama import Fore,Back,Style
import time,sys

def currectmsg(string):
    print(Style.RESET_ALL)
    print(Fore.WHITE+Style.BRIGHT + 'Great! Your setting is ' + Fore.LIGHTRED_EX + string)
    print(Style.RESET_ALL)
    time.sleep(1)

def finishmsg():
    print('')
    print(Back.GREEN, Fore.RED + '*** Execution finished *** ' + Style.RESET_ALL)
    print(Style.RESET_ALL + '')

def successmsg():
    print('')
    print(Back.LIGHTGREEN_EX, Fore.RED + '*** Execution succeed *** ' + Style.RESET_ALL)
    print(Style.RESET_ALL + '')

def runningmsg():
    print(Style.RESET_ALL)
    print('Now loading thread process, Please wait...')
    print(Style.RESET_ALL)


def wrongmsg():
    print(Style.RESET_ALL)
    print(Fore.LIGHTRED_EX, Style.BRIGHT + 'Wrong format, try it again please.')
    print(Style.RESET_ALL)
    time.sleep(1)

def faildmsg():
    print('')
    print(Back.LIGHTYELLOW_EX, Fore.RED+'*** Execution failed *** '+Style.RESET_ALL)
    print(Style.RESET_ALL+'')

def errormsg():
    print(Style.RESET_ALL)
    print(Fore.YELLOW, Style.BRIGHT+'*** The daemon encountered an unrecoverable error and the process will be killed due to security issues ***')
    print(Style.RESET_ALL)

def settingmsg():
    print('')
    print('*** Welcome to use HyperVisor Link Settings Menu ***')
    print('')
    print(Fore.YELLOW, Style.BRIGHT + 'Please complete all option values as much as possible')
    print(Style.RESET_ALL + '')
    time.sleep(1)
    print('--------------------------')
    print('1. MySQL Settings')
    print('2. Port Settings')
    print('3. API Settings')
    print('--------------------------')
    time.sleep(1)

def mainmenumsg():
    print('')
    print('*** Welcome to use HyperVisor Link Main Menu ***')
    print('')
    time.sleep(1)
    print('--------------------------')
    print('1. Install requests')
    print('2. Settings menu')
    print('3. Web menu')
    print('4. Control menu')
    print('--------------------------')
    time.sleep(1)

def controlmenumsg():
    print('')
    print('*** Welcome to use HyperVisor Link Control Menu ***')
    print('')
    time.sleep(1)
    print('--------------------------')
    print('1. List all VMs')
    print('2. Start a VM')
    print('3. Stop a VM')
    print('4. Reset a VM')
    print('5. Find a VM')
    print('q. Exit the menu')
    print('--------------------------')
    time.sleep(1)


