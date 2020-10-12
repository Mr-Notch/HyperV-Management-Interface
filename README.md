# HyperVisor Link

![HyperVistor Link (3)](https://i.loli.net/2020/10/08/bCyt5SV6maIlP9Q.png)

English

> 这是一个基于 Python38 的 Hyper-V 虚拟机管理工具

HyperVisor Link（简称 HVL）是一个由底层 PowerShell 脚本控制 Hyper-V 服务并不需要安装其他复杂功能的 Python 程序。

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

1. 在 Release 中下载最新的 HVL 受控端程序包
2. 在已经配置好 Python 环境的计算机中释放程序包
3. 使用**管理员模式的 PowerShell 窗口**前往根目录输入 `python Main-Injector.py` 并等待其加载完成

对于一般环境，其加载过程在 3-5 分钟不等

### 第一次使用需配置的常规项目（必看）

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

#### Settings menu - 设置二级菜单

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



##### 第一步：MySQL Settings

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



##### 第二步：Port Settings

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



##### 第三步：API Settings

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
