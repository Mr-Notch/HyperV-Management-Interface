# -- coding: utf-8 --
import func.netsh.netsh_commander
import utilities.RandomDice

listenport=str(utilities.RandomDice.randomDice())
connectport='3389'
connectaddress='192.168.137.151'
output = func.netsh.netsh_commander.netsh_createMirrorPort(listenport,connectaddress,connectport)

if output == True:
    print('成功1')
else:
    print('失败1')