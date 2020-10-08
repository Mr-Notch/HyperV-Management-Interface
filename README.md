# HyperVisor Link

![HyperVistor Link (3)](https://i.loli.net/2020/10/08/bCyt5SV6maIlP9Q.png)

English

> 这是一个基于 Python38 的 Hyper-V 虚拟机管理工具

HyperVisor Link（简称 HVL）是一个由底层 PowerShell 脚本控制 Hyper-V 服务并不需要安装其他复杂功能的 Python 程序。

HVL 提供一套完整的 API 方便与 WHMCS 等虚拟机部署服务进行对接。

该程序由 HydrogenCloud 编写

## 它是如何工作的？

HVL 使用 `Popen` 调用 PowerShell 脚本执行 Hyper-V 指令，并通过写入 `.tmp` 文件的方式获取回调。

## 优点

- 仅需在宿主机配置好 Python 环境即可，无需配置冗杂的配置文件
- 所有的指令回调均以文件的形式存放并等待调用
- HVL 承诺永远开源，遵循 LGPL-3 协议
- 提供完整的 API 文档，方便二次开发
- 多线程支持，同时控制几百台虚拟机不成问题

## 环境需求

Python 的版本需要在 Python 3.8+。仅限在 Windows 使用。Windows 需配备 Hyper-V 服务。

我们已经在以下环境测试尚未发现严重问题：

- `Windows Server 2019 Service Pack 1909` + `Python 3.8`
- `Windows 10 Pro Service Pack 2004` + `Python 3.8`

Hydrogen Cloud 在以下环境中已经将 HVL 用于实际生产环境：

- `Windows Server 2012 R2` + `Python 3.8`

### HVL 需要以下 Python 模块的支持

- requests
- colorlog
- ruamel.yaml
- shellsystem

## 使用方法

1. 在 Release 中下载最新的 HVL 受控端程序包
2. 在已经配置好 Python 环境的计算机中释放程序包
3. 使用**管理员模式的 PowerShell 窗口**输入 `python HVL-Main.py` 并等待其加载完成

对于一般环境，其加载过程在 3-5 分钟不等

