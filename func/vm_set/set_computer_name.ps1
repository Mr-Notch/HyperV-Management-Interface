param($vmname,$vmloc,$username,$userpasswd)
#$vmname="test_244"
#$vmloc="D:\VMachines\Hyper-V"
#$username="vmachine"
#$userpasswd="Aa123456"
# 设定UAC用户账户控制
$PassWord = ConvertTo-SecureString -String "$userpasswd" -AsPlainText -Force
$Cred = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $username, $PassWord
# 新建通道并通过UAC远程到虚拟机
$Session = New-PSSession -VMName $vmname -Verbose -Credential $Cred
# 寻找VMCX文件
$vmcx_name = Get-ChildItem -Path "$vmloc\$vmname\Virtual Machines" -Filter "*.vmcx" -Name
## $vmcx_name = Get-ChildItem -Path "D:\VMachines\Hyper-V\test_244\Virtual Machines\test_244\Virtual Machines" -Filter "*.vmcx" -Name
# 删除.VMCX后缀，获取VMID
$vmid = $vmcx_name.Replace(".vmcx","")
## Write-Output $vmid
# 在虚拟机内执行更改操作并重启
Invoke-Command -Session $Session -ScriptBlock {param($vmid) & Rename-Computer -NewName "$vmid" -Force -Restart} -ArgumentList $vmid

