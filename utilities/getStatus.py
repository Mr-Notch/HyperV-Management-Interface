# -- coding: utf-8 --
import func.vm_info.info_commander


def getStatus(vmname):
    check = func.vm_info.info_commander.vm_info_getPowerStatus(vmname)
    if "Off" in check:
        print('关闭')
        return 'Off'
    elif "Running" in check:
        print('运行中')
        return 'Running'
    elif "Saving" in check:
        print('保存中')
        return 'Saving'
    elif "Saved" in check:
        print('已保存')
        return 'Saved'
    elif "Paused" in check:
        print('已暂停')
        return 'Paused'
    else:
        print('未知状态')
        return 'Unknown'


