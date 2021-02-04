# -- coding: utf-8 --
from terminal_layout.extensions.choice import *
from terminal_layout import *

c = Choice('Welcome to use Hyper-V Management Interface:',
           ['Import-VM', 'Export-VM', 'New-VM', 'Delete-VM', 'Create-PortMirror','*Exit*'],
           icon_style=StringStyle(fore=Fore.yellow),
           selected_style=StringStyle(fore=Fore.red))

choice = c.get_choice()
if choice:
    index, value = choice
    if value == 'Import-VM':
        print(value, '导入虚拟机')
    elif value == 'Export-VM':
        print(value, '导出虚拟机')
    elif value == 'New-VM':
        print(value, '新建虚拟机')
    elif value == 'Delete-VM':
        print(value, '删除虚拟机')
    elif value == 'Create-PortMirror':
        print(value, '创建端口映射')
    else:
        print(value, '退出程序')