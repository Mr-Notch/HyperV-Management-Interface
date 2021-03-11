import curses
import time
import random
import os
from terminal_layout.extensions.choice import *
from terminal_layout import *
from Interface.UT import utility_wheels

def welcome_gui():
    curses.initscr()
    screen = curses.initscr()
    
    screen.border(0)
    screen.addstr(1,2,'Welcome To Use Hyper-V Management Interface')
    screen.addstr(2,2,'*** Daemon will start on 1 seconds ***')
    screen.refresh()
    height = 6; width = 40
    # define win_1
    win_1 = curses.newwin(height,width,0,0)
    win_1.border(0)
    win_1.addstr(1,2,'Loading Daemon')
    time.sleep(1)
    win_1.refresh()
     
    time.sleep(random.randint(1,3))
    # define win_2
    win_2 = curses.newwin(height,width,0,0)
    win_2.border(0)
    win_2.addstr(1,2,'Load successful')
    win_2.refresh()
    time.sleep(random.uniform(0.1,0.9))
    win_2.addstr(2,2,'Injector started')
    win_2.refresh()
    time.sleep(random.uniform(0.4,0.9))
    win_2.addstr(3,2,'Login from UAC...')
    win_2.refresh()
    time.sleep(random.uniform(0.3,0.8))
    # loggerinterface.openLogWindow()
    win_2.addstr(4,2,'Loading Main Menu...')
    win_2.refresh()
    time.sleep(0.5)
    curses.endwin()



def main_gui():
    os.system('cls')
    c = Choice('HMI Daemon GUI Controller (Press "ESC" to quit):',
           ['Virtual Machine Options', 'HMI Logger', 'Computer Status'],
           icon_style=StringStyle(fore=Fore.green),
           selected_style=StringStyle(fore=Fore.green))

    choice = c.get_choice()
    if choice:
        index, value = choice
        if value == 'Virtual Machine Options':
            os.system('cls')
            c_0 = Choice('Virtual Machine Options:',
                    ['Import a Virtual Machine', 'Create a Virtual Machine', 'Export a Virtual Machine','Delete a Virtual Machine','Rebuild a Virtual Machine','NetSH Setting Options'],
                    icon_style=StringStyle(fore=Fore.green),
                    selected_style=StringStyle(fore=Fore.green))
            choice_0 = c_0.get_choice()
            if choice_0:
                index_0, value_0 = choice_0
                if value_0 == 'Import a Virtual Machine':
                    os.system('cls')
                    template_name=input('Input Template Name: ')
                    vm_name=input('Input VM Name: ')
                    vm_ram=input('Input VM Ram Size: ')+'GB'
                    vm_cpu=input('Input VM CPU Num: ')
                    maturity_end_date=input('Input Maturity End Date (eg: 2021-02-01): ')

                    print(utility_wheels.VMImportWheel(template_name,vm_name,vm_ram,vm_cpu,maturity_end_date))
                elif value_0 == 'Create a Virtual Machine':
                    os.system('cls')
                    vm_name=input('Input VM Name: ')
                    vm_ram=input('Input VM Ram Size: ')+'GB'
                    vm_cpu=input('Input VM CPU Num: ')
                    vhd_size=input('Input VHD Size: ')+'GB'
                    iso_name=input('Input ISO Name: ')

                    # vm_name='test_import_vm'
                    # vm_ram='2'
                    # vm_cpu='2'
                    # vhd_size='30'
                    # iso_name=''
                    # vm_login_user='Administrator'
                    # vm_login_password='Aa123456'
                    # maturity_end_date='2021-03-31'

                    print(utility_wheels.VMCreateWheel(vm_name,vm_ram,vm_cpu,vhd_size,iso_name))
                    
                elif value_0 == 'Export a Virtual Machine':
                    os.system('cls')
                    vm_name=input('Input VM Name: ')

                    print(utility_wheels.VMExportWheel(vm_name))

                elif value_0 == 'Delete a Virtual Machine':
                    os.system('cls')
                    vm_name=input('Input VM Name: ')
                    print(utility_wheels.VMDeleteWheel(vm_name))
                    
                elif value_0 == 'Rebuild a Virtual Machine':
                    os.system('cls')
                    print('*** WARNING: ALL DATA WILL BE DELETED ***')
                    print('')
                    vm_name=input('Input VM Name: ')
                    template_name=input('Input Template Name: ')
                    print(utility_wheels.VMRebuildWheel(vm_name,template_name))


        elif value == 'HMI Logger':
            os.system('cls')
            print('Logger Info')
        
        elif value == 'Computer Status':
            os.system('cls')
            print('Computer Status')