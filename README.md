# HyperVisor Link

![HyperVistor Link (3)](https://i.loli.net/2020/10/08/bCyt5SV6maIlP9Q.png)

[点我](https://github.com/Mr-Notch/HyperVisorLink )



> 这是一个基于 Python38 的 Hyper-V 虚拟机管理工具

HyperVisor Link（简称 HVL）是一个由底层 PowerShell 脚本控制 Hyper-V 服务，并不需要安装其他复杂功能的 Python 程序。

HVL 提供一套完整的 API 方便与 WHMCS 等虚拟机部署服务进行对接。

该程序由 HydrogenCloud 编写

## 它是如何工作的？

HVL 使用 `Popen` 调用 PowerShell 脚本执行 Hyper-V 指令，并通过写入 `.txt` 方式获取回调。

## 优点

- 仅需在宿主机配置好 Python 环境即可，无需配置冗杂的配置文件
- 所有的指令回调均以文件的形式存放并等待调用
- HVL 承诺永远开源，遵循 LGPL-3 协议
- 提供完整的 API 文档，方便二次开发

## 环境需求

Python 的版本需要在 Python 3.8+。仅限在 Windows 使用。Windows 需配备 Hyper-V 服务。

我们已经在以下环境测试尚未发现严重问题：

- `Windows Server 2019 Service Pack 1909` + `Python 3.8`
- `Windows 10 Pro Service Pack 2004` + `Python 3.8`

Hydrogen Cloud 在以下环境中已经将 HVL 用于实际生产环境：

- `Windows Server 2012 R2` + `Python 3.8`

### HVL 需要以下 Python 模块的支持

- ruamel.yaml
- requests
- colorlog
- colorama
- chardet
- pymysql

## 使用方法

**本版块的内容较多、较复杂，请确保自己有充足的时间仔细阅读该板块**

**建议使用实践操作法练习使用 HVL Daemon**

目录：

- [第一次使用需配置的常规项目（必看）](https://github.com/Mr-Notch/HyperVisorLink#%E7%AC%AC%E4%B8%80%E6%AC%A1%E4%BD%BF%E7%94%A8%E9%9C%80%E9%85%8D%E7%BD%AE%E7%9A%84%E5%B8%B8%E8%A7%84%E9%A1%B9%E7%9B%AE%E5%BF%85%E7%9C%8B)
  - [准备工作](https://github.com/Mr-Notch/HyperVisorLink#%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)

- [常规设置二级菜单](https://github.com/Mr-Notch/HyperVisorLink#settings-menu---%E5%B8%B8%E8%A7%84%E8%AE%BE%E7%BD%AE%E4%BA%8C%E7%BA%A7%E8%8F%9C%E5%8D%95)

  - [数据库设置](https://github.com/Mr-Notch/HyperVisorLink#%E7%AC%AC%E4%B8%80%E6%AD%A5mysql-settings)
  - [端口设置](https://github.com/Mr-Notch/HyperVisorLink#%E7%AC%AC%E4%BA%8C%E6%AD%A5port-settings)
  - [API 设置](https://github.com/Mr-Notch/HyperVisorLink#%E7%AC%AC%E4%B8%89%E6%AD%A5api-settings)

- [网页设置二级菜单](https://github.com/Mr-Notch/HyperVisorLink#web-menu---%E7%BD%91%E9%A1%B5%E8%AE%BE%E7%BD%AE%E4%BA%8C%E7%BA%A7%E8%8F%9C%E5%8D%95)

  - 阿巴阿巴阿巴

- [控制面板二级菜单](https://github.com/Mr-Notch/HyperVisorLink#control-menu---%E6%8E%A7%E5%88%B6%E9%9D%A2%E6%9D%BF%E4%BA%8C%E7%BA%A7%E8%8F%9C%E5%8D%95)

  - [列举虚拟机](https://github.com/Mr-Notch/HyperVisorLink#i-%E5%88%97%E4%B8%BE%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [关闭虚拟机](https://github.com/Mr-Notch/HyperVisorLink#iii-%E5%85%B3%E9%97%AD%E4%B8%80%E4%B8%AA%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [重置虚拟机](https://github.com/Mr-Notch/HyperVisorLink#iv-%E9%87%8D%E7%BD%AE%E4%B8%80%E4%B8%AA%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [搜寻虚拟机](https://github.com/Mr-Notch/HyperVisorLink#iiv-%E6%90%9C%E5%AF%BB%E8%99%9A%E6%8B%9F%E6%9C%BA)
  - [新建虚拟机]()

[TOC]



### 第一次使用需配置的常规项目（必看）

#### 准备工作：

1. 在 Release 中下载最新的 HVL 受控端程序包
2. 在已经配置好 Python 环境的计算机中释放程序包
3. 使用**管理员模式的 PowerShell 窗口**前往根目录输入 `python Main-Injector.py` 并等待其加载完成

对于一般环境，其加载过程在 3-5 分钟不等

等待其加载完成后，正常情况下会弹出一个命令行菜单：

```
*** Welcome to use HyperVisor Link Main Menu ***

--------------------------
1. Install requests
2. Settings menu
3. Web menu
4. Control menu
--------------------------
Type-in the option of your choise: 
```

这就是 HyperVisorLink Daemon（下文简称其为 Daemon）的主菜单。

> 1. Install requests - 安装需求的 Python 模块
> 2. Settings menu - 进入设置二级菜单
> 3. Web menu - 进入网页设置二级菜单
> 4. Control menu - 进入虚拟机控制二级菜单

使用键盘输入每一个选项卡的数字标识并按下回车即可进入相应的二级菜单

下文将详细介绍每一个二级菜单。

------

### Settings menu - 常规设置二级菜单

在命令行文本框输入 `2`，跳转至该二级菜单：

```
*** Welcome to use HyperVisor Link Settings Menu ***

 Please complete all option values as much as possible

--------------------------
1. MySQL Settings
2. Port Settings
3. API Settings
--------------------------
Type-in the options in 1-3: 
```

> 1. MySQL Settings - MySQL 数据库常规设置
> 2. Port Settings - 端口通信设置
> 3. API Settings - API 接口设置

每设置完一个选项都需要手动输入下一个选项卡的数字标识，设置完三个以后 Daemon 会自动关闭以应对更改



#### 第一步：MySQL Settings

在命令行文本框输入 `1`，跳转至该三级菜单：

```
*** MySQL Settings ***

We need MySQL Port / Address / UserName / Database
Please enter them carefully and separate them with commas
Example: 3306,localhost,root,hypervisorlinkdb

 Input these strings below.
 Input: 
```

这里需要输入一串包含数据库基本信息的集合。使用 英文的`,`隔开。格式需要严格遵守示范模板：

示范：`3306,localhost,root,hypervisorlinkdb`

集合元素从前到后依次排列为：

1. MySQL 的通信端口（如无更改直接抄示范即可）
2. MySQL 的通信地址（一般为本地`localhost`）
3. MySQL 数据库的用户名（不建议填`root`，如果需要可以自行建立并将建立的用户名填入）
4. MySQL 数据库名（需要手动建立，如无特殊要求抄示范即可）

填入完毕后按下回车键，会弹出一个简短的回复信息并重新弹出输入选项卡的输入框：

```
Great! Your setting is 3306,localhost,root,hypervisorlinkdb

Type-in the options in 1-3: 
```



#### 第二步：Port Settings

在输入框内输入`2`，跳转至该三级菜单：

```
*** Port Settings ***

Type in the port you like below, do not set the same as other ports (Default: 6400)
 
 Input: 
```

这里的设置就比较简单了，仅需要填写一个东西：`通信端口名`

通信端口名需要在`1-65535`之间，切不可与其他服务端口冲突。推荐使用`6400`作为 Daemon 及其 API 的端口

**如需将前端与其他辅助服务部署在非内网服务器，需要将防火墙出入规则加上该端口的 TCP/UDP 双协议**

填入完毕后按下回车，也会有一个小提示并继续让你填写：

```
Great! Your setting is 6400

Type-in the options in 1-3: 
```



#### 第三步：API Settings

键入`3`，进入该三级菜单：

```
*** API Settings ***

Enter the API-Key you want, preferably a little more complicated. (More than 6 bit)
 
 Input: 
```

这里的设置也比较简单，需要的就是**输入一个长度超过 6 个字母的 API-Key 密钥**。

该 API-Key 密钥将被使用 SHA-256 值加密，位数越多，加密效果越明显。

推荐设置为你的个人私人密码。这个密码将被用于与前端对接、安装其他辅助服务功能时所需。也是唯一能够通过 WebSocket 协议与 Daemon 通信的唯一凭据。该凭据一旦泄露，其他人很有可能会透过 API 来取得宿主机的控制权。

输入完毕后按下回车，Daemon 服务将自动关闭。同样地，如果想修改信息既可以通过该步骤菜单，也可以直接在`./Config/inf_config.txt`文件内手动更改集合内容。

（`************`指代的是 API-Key）

```
Great! Your setting is ************

Successfully to set.

({'Port': '3306', 'Address': 'localhost', 'UserName': 'root', 'Database': 'hyperv'}, {'SRV-Port': '6400'}, {'API-Key': '************'})

If its successful, please restart the daemon.
Daemon will be killed in 2 sec.
By the way, you can also modify it in the "./Config/inf_config.txt".


进程已结束,退出代码0

```



**此时，Daemon 的基本设置已经填写完毕。如无需前端，此时已经可以直接通过 Daemon 操作 Hyper-V 了**

如需配置前端（Web面板等），请 **移步至此**

------

### Web menu - 网页设置二级菜单

阿巴阿巴阿巴

------

### Control menu - 控制面板二级菜单

在命令行内输入`4`，跳转至该二级菜单：

```
*** Welcome to use HyperVisor Link Control Menu ***
--------------------------
1. List all VMs
2. Start a VM
3. Stop a VM
4. Reset a VM
5. Find a VM
6. Create a new VM
7. Create a backup-point
8. Delete a VM
9. Delete a backup-point
10. Import a VM from a template
11. Export a VM into the template
q. Exit the menu
--------------------------
Type-in the options in 1-11 or q to exit: 
```

> 1. List all VMs - 列举出所有存在的虚拟机
>
> 2. Start a VM - 开启一个虚拟机
>
> 3. Stop a VM - 关闭一个虚拟机
>
> 4. Reset a VM - 重置一个虚拟机
>
> 5. Find a VM - 在列表中搜寻一个虚拟机
>
> 6. Create a new VM - 创建一个新虚拟机
>
> 7. Create a backup-point - 给虚拟机创建一个备份还原点
>
> 8. Delete a VM - 删除一个虚拟机到回收站
>
> 9. Delete a backup-point - 永久删除一个备份还原点
>
> 10. Import a VM from a template - 从模板中导入虚拟机
>
> 11. Export a VM into the template - 将虚拟机导出到模板
>
>     q. Exit the menu - 退出至一级菜单

#### I. 列举虚拟机

在输入框输入`1`，此时应该会弹出类似这样的文本：

```

Name State   CPUUsage(%) MemoryAssigned(M) Uptime           Status Version
---- -----   ----------- ----------------- ------           ------ -------
TEST Running 0           2048              00:29:06.6460000 正常运行   9.0    
ABCD Running 2           1024              00:29:06.6480000 正常运行   9.0  



 *** Execution finished *** 

Type-in the options in 1-5 or q to exit: 
```

此时，在前几行的小表格内即是在计算机中 Hyper-V 能搜索到的全部的虚拟机。

#### II. 开启一个虚拟机

在输入框内输入`2`，此时仍需要输入一个字符串，字符串内容为要执行命令的虚拟机名称

例如，我需要打开`TEST`虚拟机，此时应在第二个输入框输入`TEST`

```
Type-in the options in 1-5 or q to exit: 2
Type-in the value of the vmname: TEST
```

然后按下回车键，等待其执行完毕：

```
Now loading thread process, Please wait...

警告: 虚拟机已处于指定的状态。


 *** Execution finished *** 

Type-in the options in 1-5 or q to exit: 
```

若中央弹出`警告: 虚拟机已处于指定的状态。`时，证明虚拟机处于开启状态，无法再次执行开启指令。

若中央没有弹出警告，仅提示`*** Execution finished ***`，证明指令执行成功，虚拟机应该被开启。

#### III. 关闭一个虚拟机

在输入框内输入`3`，在第二个输入框输入要执行关机操作虚拟机的名称。

此时提示第三个输入框，该输入框需要输入`Y 或 N`来确认或否认是否需要强制关闭。

如果选择`Y`，即 **强制关闭虚拟机，相当于直接拔掉虚拟机的电源。**

否则将安全关闭虚拟机（向系统发送关机指令，让系统自行处理关机操作）

```
Type-in the options in 1-5 or q to exit: 3
Type-in the value of the vmname: TEST
Should I execute force shutdown? (Y/N): N
```

按下回车后，应当提示类似以下内容：

```
Now loading thread process, Please wait...



 *** Execution finished *** 

Type-in the options in 1-5 or q to exit: 
```

若提示 ``警告: 虚拟机已处于指定的状态。``，证明虚拟机已经处于关闭状态，无法再执行关机操作

否则虚拟机应当被执行关机指令。

#### IV. 重置一个虚拟机

在 Hyper-V 中，重置与重启效果相同。相当于给虚拟机按下了 Reset 键。

在输入框输入`4`，在第二个输入框输入要执行重置操作的虚拟机名称

按下回车后，虚拟机应当被重置。如果弹出报错，虚拟机则处于关闭状态或其他状态（例如正在导出/生成还原点）

#### V. 搜寻虚拟机

虚拟机太多怎么办？在文本框输入`5`，进入虚拟机检索功能。

此时弹出第二个输入框，输入要检索的虚拟机名称或其部分字母，按下回车，系统将自动写出符合要求的虚拟机。

```
Type-in the options in 1-5 or q to exit: 5
Type-in the value of the vmname: TEST

Name State CPUUsage(%) MemoryAssigned(M) Uptime   Status Version
---- ----- ----------- ----------------- ------   ------ -------
TEST Off   0           0                 00:00:00 正常运行   9.0    




 *** Execution finished *** 

Type-in the options in 1-5 or q to exit: 
```

#### VI. 新建虚拟机

最重要的功能。若想要通过 HyperVisorLink 新建虚拟机，请务必阅读该板块。

在输入框输入`6`，进入新建虚拟机二级界面

```
*** New-VM Settings & Manage Menu ***
--------------------------
1. Continue to create a new VM
q. Exit the menu
--------------------------
Type-in the options in 1 or q to exit: 
```

此时，弹出一个确认选项。若选择`1`，则进入创建虚拟机菜单

若选择`q`，则退出返回至上一级菜单

输入`1`，进入下一级菜单：

```
*** Create a VM ***

We need VMName / RamSize / CPUNumber / VMSwitchName / VMDiskName / VMDiskSize / VMLocation / ISOLocation
Please enter them carefully and separate them with commas
Example: TEST,2GB,2,TESTSwitch,C,10GB,D:\Virtual Machines\,D:\ISO Files\

 Input these strings below.
 Input: 
```

在这里，需要输入一个集合，一个包含新建虚拟机必要信息的集合。

其中集合元素有：

- VMName - 虚拟机名称
- RamSize - 虚拟机内存大小
- CPUNumber - CPU个数
- VMSwitchName - 虚拟交换机个数
- VMDiskName - 虚拟机硬盘名称
- VMDiskSize - 虚拟机硬盘大小
- VMLocation - 虚拟机路径
- ISOLocation - 要挂载 ISO 镜像的路径

**所有集合元素必须严格按照格式填写，以逗号分隔，不按格式填写可能会导致其他错误**

标准填写方式：`名称,内存,CPU,虚拟交换机,硬盘名称,硬盘大小,虚拟机路径,ISO路径`

例如：`TEST,2GB,2,TESTSwitch,C,10GB,D:\Virtual Machines\,D:\ISO Files\`

那么将创建一个拥有以下特性的虚拟机：

- 虚拟机名称：TEST
- 内存大小：2GB
- CPU个数：2 个
- 虚拟交换机：TESTSwitch
- 磁盘名称：C
- 磁盘大小：10GB
- 虚拟机位置：D:\Virtual Machines\
- ISO位置：D:\ISO Files\

严格填好元素后，按下回车键

```
Great! Your setting is TEST,2GB,2,TESTSwitch,C,10GB,D:\Virtual Machines\,D:\ISO Files\


Now loading thread process, Please wait...


Name  State CPUUsage(%) MemoryAssigned(M) Uptime   Status Version
----  ----- ----------- ----------------- ------   ------ -------
TEST Off   0           0                 00:00:00 正常运行   9.0   




 *** Execution finished *** 
```

此时，虚拟机已经创建好了。



（此处省略一些：7-9没写）

#### X. 从模板导入一个虚拟机

若要创建大量配置好的虚拟机，避免不了需要实现一个模板批量导入虚拟机的脚本。

下面将学习如何使用 HyperVisor Link 的导入虚拟机功能批量导入虚拟机

在输入框输入`10`，进入下一级菜单：

```
*** Import VM Manage Menu ***

--------------------------
1. Import and create a copy of the VM
2. Import and register the VM in place
3. Import and move the VM to a new location
q. Exit the menu
--------------------------
Type-in the options in 1-3 or q to exit: 
```

> 1. Import and create a copy of the VM - 从模板导入并直接从模板复制一个新虚拟机到指定路径
> 2. Import and register the VM in place - 就地注册虚拟机，直接调用模板
> 3. Import and move the VM to a new location - 将模板转移至指定路径并调用

##### 1. 从模板复制虚拟机并调用

该方法适用于已经设计好的模板，需要直接从模板复制虚拟机副本。

输入框输入`1`，进入下级菜单：

```
*** Import and create a copy of the VM ***

We need VMName / VMLocation / TemplateName / TemplateLocation
Please enter them carefully and separate them with commas
Example: TEST,D:\Virtual Machines\,SAMPLE-WINDOWS,D:\SAMPLE Files\

 Input these strings below.
 Input: 
```

在此需要填一个集合，集合元素由以下构成：

`虚拟机名称,虚拟机路径,模板名称,模板路径`

例如：`TEST,D:\Virtual Machines\,SAMPLE-WINDOWS,D:\SAMPLE Files\`

将元素修改至适当的设置，并使用英文逗号分隔开。如果格式和上方实例相似，那么按下回车，等待其导入完成：

```
Great! Your setting is `TEST,D:\Virtual Machines\,SAMPLE-WINDOWS,D:\SAMPLE Files\`


Now loading thread process, Please wait...

Virtual Machines\684E6F88-3EE2-4FC3-B2CF-9A6040EBE4EB.vmcx

Name           State CPUUsage(%) MemoryAssigned(M) Uptime   Status   Version
-------------- ----- ----------- ----------------- ------   ------   -------
SAMPLE-WINDOWS Off   0           0                 00:00:00 正常运行 9.0    



Name  State CPUUsage(%) MemoryAssigned(M) Uptime   Status Version
----  ----- ----------- ----------------- ------   ------ -------
TEST Off   0           0                 00:00:00 正常运行   9.0    




 *** Execution finished *** 
```

此时，从模板导入的虚拟机已经成功被复制。

虚拟机的名称为 `TEST`.

