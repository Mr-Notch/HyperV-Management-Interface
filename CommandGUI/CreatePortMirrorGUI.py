# -- coding: utf-8 --
import utilities.RandomDice
import utilities.getAddress
import func.netsh.netsh_commander
import config.ConfigWriter
def guiwriter():
    print('---------------------')
    print('| Create-PortMirror |')
    print('---------------------')
    print('')
    vm_name = input('VM Name (String) : ')
    mirrored_port = input('VM Mirrored Port (Int64) : ') # 内网映射端口
    # outside_port = str(utilities.RandomDice.randomDice()) # 随机的外网端口
    outside_port = '19132'  # 随机的外网端口

    vm_ipv4addr = str(utilities.getAddress.getAddress(vm_name))

    output = func.netsh.netsh_commander.netsh_createMirrorPort(outside_port,vm_ipv4addr,mirrored_port)

    if output == True:
        print('成功创建端口: '+mirrored_port+'->'+outside_port)
        config.ConfigWriter.PortConfigWriter(vm_name,mirrored_port,outside_port,vm_ipv4addr,'localhost')
    else:
        print('失败1')

guiwriter()
