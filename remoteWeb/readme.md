测试内网远程虚拟机（NetBIOS层）

外网通过Web访问

内核使用RDP

------

## Remote for Hyper-V Virtual Machines

基于 Hyper-V RDP 通讯协议的 Web RDP界面

通过在硬件层面调用虚拟机主窗口

同时在远程界面增加对触摸屏的支持

以及对 BIOS 层面的控制与键盘输入

协议基于 RDP，目前仅在 Windows Server 2012 R2 上测试了 RemoteFX 显卡加速功能

![image-20201128002941428](https://i.loli.net/2020/11/28/HzynaRDAwb9c2XT.png)

- XXX：虚拟机名称（不是 VMID）

- 下方的快捷指令：Ctrl+Alt+Delete、软键盘、VPS操作、VPS交互

  - Ctrl Alt Delete：向RDP发送该热键

  - 软键盘：在下方弹出虚拟键盘（适用于触摸屏）

  - VPS操作：关机、重启、重置、进入还原状态等

  - VPS交互：远程信道、网络信道、扬声器、麦克风等交互方式

    