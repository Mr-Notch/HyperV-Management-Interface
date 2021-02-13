# -- coding: utf-8 --
from terminal_layout.extensions.choice import *
from terminal_layout import *

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import ImportVMGUI
import CreateVMGUI

def drawChoiseMenu():
    mainmenu = Choice('Welcome to use Hyper-V Management Interface:',
                      ['Import-VM', 'Export-VM', 'New-VM', 'Delete-VM', 'Create-PortMirror', 'Edit-VM', '*Exit*'],
                      icon_style=StringStyle(fore=Fore.yellow),
                      selected_style=StringStyle(fore=Fore.red))

    Main_Choice = mainmenu.get_choice()
    if Main_Choice:
        index, value = Main_Choice
        if value == 'Import-VM':
            print(value, '导入虚拟机')

            ImportVMGUI.guiwriter()
            return True

        elif value == 'Export-VM':
            print(value, '导出虚拟机')

            return True

        elif value == 'New-VM':
            print(value, '新建虚拟机')
            CreateVMGUI.guiwriter()
            return True

        elif value == 'Delete-VM':
            print(value, '删除虚拟机')

            return True

        elif value == 'Create-PortMirror':
            print(value, '创建端口映射')

            return True

        elif value == 'Edit-VM':
            print(value, '编辑虚拟机配置')

            return True

        else:
            print(value, '退出程序')
            return False

drawChoiseMenu()