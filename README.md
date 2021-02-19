## HyperV Management Interface (HMI)
基于 Python 与 Powershell 的 Hyper-V 远程管理工具（前HyperVisorLink）

### 运行原理
> 底层为 PowerShell，Python 作为执行器。WebSocket 作为受控与主控之间的通信。HTML5 与 JavaScript 作为前端网页控制器

### 当前版本为生产力版本，可以脱离 IDE 运行

如需查看开发版本（旧版）可以前往 `Main Branch` 查看

生产力版本相比开发版本更稳定。并且具备 `GUI` 与 `Log` 日志记录功能

### 配置方法

使用编辑器（推荐Visual Studio Code）打开 `MainInterface.py`

此时，应该会发现里面有一些可配置的参数：

```

'''
此处配置方案请参考 HMI 的 GitHub
'''

# Interface 类型（默认：PowerShell）
it_interface='PowerShell'

# 裸金属模式开关（开启后Hyper-V将独享宿主机配置，每台虚拟机将独立分配固定内存）
it_bare_metal_mode=True

# 虚拟交换机名称
it_vm_switch_name='NAT'

# 新建虚拟机/导入虚拟机时默认开放的链接端口（Windows建议填3389；Linux SSH建议填22）
it_vm_netsh_default_connect_port='3389'

# 新建虚拟机/导入虚拟机时开放的额外端口数量（默认外网端口均为随机制，范围10000-20000）
it_vm_netsh_extra_connect_port_number='4'

# 新建虚拟机/导入虚拟机时开放的额外端口内网端口起始值（默认为10000开始，往后依次加1）
it_vm_netsh_extra_mirrored_port_started='10000'

# HMI 运行目录（填写 MainInterface.py 所在的目录即可）
it_hmi_location=''

# Hyper-V 虚拟机运行目录（最好单独用一块磁盘）
it_vm_location=''

# ISO 镜像所在目录
it_iso_location=''

# 模板所在目录
it_template_location=''

# 虚拟机模板登录用户名
it_template_login_user_name='Administrator'

# 虚拟机模板登录密码
it_template_login_user_password='Aa123456'

# 虚拟机到期保留时间（单位：天）
it_mature_keep_time='7'

# 虚拟机超过到期保留时间是否直接抹掉数据（默认：True）
it_mature_delete_file=True
# 上面的开关如果为False，则下面的需要填写

# 超过到期保留时间后虚拟机将移动到哪个文件夹，填写 vm_location 则不会对虚拟机做出任何更改
it_mature_recycle_bin=''

# SMTP 邮件服务器地址
it_smtp_server_address=''

# SMTP 登录用户名
it_smtp_login_user=''

# SMTP 登录密码
it_smtp_login_password=''

# SMTP 发送者名称
it_smtp_sender_user=''

# SMTP 邮件接收者（支持群发）
it_smtp_receiver_user=[]

```

按照提示完成填写参数，需要严格按照格式填写

> 注意事项：
>
> - 路径需要使用双反斜杠 `\\` 表示（例如：`E:\\HyperVisorLink\\HMI\\`
> - HMI 导入虚拟机的方式以模板为主。如需自制模板，请参考下方说明
> - SMTP 邮件服务必填
>
> - 运行 HMI 需要至少 1GB 的存储空间；虚拟机存放目录最好单独放一个硬盘里

### 初次运行与配置

当完成上述操作后，使用处于 `管理员模式` 下的 `PowerShell` 前往 HMI 运行路径

输入 `pip install -r requirement.txt` 安装所需环境

安装完毕后，输入 `py MainInterface.py` 打开 HMI

*一般情况下，打开后应该会弹出类似如下窗口的 GUI*

![image-20210219131821245](https://i.loli.net/2021/02/19/lhWdns69HVt5Xmq.png)

*此时应等待其注入完成，若没有报错，会弹出一个 Logger 窗口。该窗口用来记录日志信息*

*此外，主窗口应该会变为类似如下界面：*

![image-20210219131927440](https://i.loli.net/2021/02/19/FKdj8nOGQHE1Bya.png)