# -- coding: utf-8 --
import Injector
import os
import deamon.checkMaturityTime
import time
import datetime
import sys

sys_path = Injector.getSysLocation()


# 遍历所有虚拟机检查是否到期
def walkVM():
    path = sys_path + "config/vmconfig/"
    for root, dirs, files in os.walk(path):
        # print(files)
        for i in files:
            # print(i)
            deamon.checkMaturityTime.checkMaturityTime(i.replace('.json', ''))
            time.sleep(1)


# 每天凌晨执行检查虚拟机
def timerTask():
    print('---------------')
    print('Main Timer Task')
    print('---------------')
    hour = 0
    minute = 0
    while True:


        now = datetime.datetime.now()

        if now.hour == hour and now.minute == minute:
            walkVM()
            print('Scan over. Wait 1 minute.')
            time.sleep(60)
            print('Running, wait 120 sec for next scan.')
            continue
        else:
            print('Running, wait 120 sec for next scan.')
            time.sleep(120)





timerTask()