# -- coding: utf-8 --
import func.netsh.netsh_commander
import utilities.RandomDice

listenport='16339'
output = func.netsh.netsh_commander.netsh_removeMirrorPort(listenport)

if output == True:
    print('成功1')
else:
    print('失败1')