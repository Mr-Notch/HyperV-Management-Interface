## HyperV Management Interface (HMI)
基于 Python 与 Powershell 的 Hyper-V 远程管理工具（前HyperVisorLink）

### 运行原理
> 底层为 PowerShell，Python 作为执行器。WebSocket 作为受控与主控之间的通信。HTML5 与 JavaScript 作为前端网页控制器

### API
目前已经添加以下 API 支持：
- 新建/删除虚拟机
- 修改虚拟机硬件配置
- 修改虚拟机计算机名
- 导入/导出虚拟机
- 远程访问 Hyper-V 服务器
> 2021/2累计更新：
- NAT网桥的创建
- NAT自动转发
- NAT端口映射
- 为虚拟机添加NAT网卡
- 自动获取虚拟机状态

目前正在制作的：
- WebSocket 的支持

两个月咕咕了，现在恢复正常更新
先不做WebSocket，先弄封装以及XML虚拟机标签。
