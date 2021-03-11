
from Interface.__main__ import MainInjector
import sys

'''
此处配置方案请参考 HMI 的 GitHub
'''

# Interface 类型（默认：PowerShell）
it_interface='PowerShell'
# 裸金属模式开关（开启后Hyper-V将独享宿主机配置，每台虚拟机将独立分配固定内存）
it_bare_metal_mode=True
# 新建虚拟机/导入虚拟机时默认开放的链接端口（Windows建议填3389；Linux SSH建议填22）
it_vm_netsh_default_connect_port='3389'
# 新建虚拟机/导入虚拟机时开放的额外端口数量（默认外网端口均为随机制，范围10000-20000）
it_vm_netsh_extra_connect_port_number='4'
# 新建虚拟机/导入虚拟机时开放的额外端口内网端口起始值（默认为10000开始，往后依次加1）
it_vm_netsh_extra_mirrored_port_started='10000'
# HMI 运行目录（填写 MainInterface.py 所在的目录即可）
it_hmi_location='D:\\Services\\HyperV-Management-Interface\\'
# Hyper-V 虚拟机运行目录（最好单独用一块磁盘）
it_vm_location='D:\\HMI-Files\\Resources\\'
# ISO 镜像所在目录
it_iso_location='D:\\HMI-Files\\ISO\\'
# 模板所在目录
it_template_location='D:\\HMI-Files\\Templates\\'
# 虚拟机模板登录用户名
it_template_login_user_name='Administrator'
# 虚拟机模板登录密码
it_template_login_user_password='Aa123456'
# 虚拟机到期保留时间（单位：天）
it_mature_keep_time=7
# 虚拟机超过到期保留时间是否直接抹掉数据（默认：True）
it_mature_delete_file=True
# 上面的开关如果为False，则下面的需要填写
# 超过到期保留时间后虚拟机将移动到哪个文件夹，填写 vm_location 则不会对虚拟机做出任何更改
it_mature_recycle_bin=''
# SMTP 邮件服务器地址
it_smtp_server_address='smtp.163.com'
# SMTP 登录用户名
it_smtp_login_user='HydrogenCloud@163.com'
# SMTP 登录密码
it_smtp_login_password='LECOGDYYBJUJJBST'
# SMTP 发送者名称
it_smtp_sender_user='HydrogenCloud@163.com'
# SMTP 邮件接收者（支持群发）
it_smtp_receiver_user=["Mr_Notch@163.com","2222002611@qq.com","2628869101@qq.com","80421117@qq.com","42402007@qq.com"]

# 网络模式（NAT或Bridge，NAT模式需要设置NAT网关，Bridge模式需要更改网段为物理路由器的网段）
it_network_mode='NAT'
# NAT网关名称
it_nat_name='NATNetwork'
# 虚拟交换机名称
it_vm_switch_name='NATSwitch'
# 网段（若为192.168.100.x就填192.168.100）
it_nat_segment='192.168.100'
# DNS（虚拟机上网用的DNS）
it_nat_dns='223.5.5.5'
# Telnet 的链接地址
it_telnet_address='192.168.2.1'
# Telnet 的连接用户
it_telnet_user='root'
# Telnet 的用户密码
it_telnet_password='adminHW'



if __name__ == '__main__':
    sys.exit(MainInjector())