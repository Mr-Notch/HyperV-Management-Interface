param($vmname,$vmloc,$username,$userpasswd)
#$vmname="test_244"
#$vmloc="D:\VMachines\Hyper-V"
#$username="vmachine"
#$userpasswd="Aa123456"
# �趨UAC�û��˻�����
$PassWord = ConvertTo-SecureString -String "$userpasswd" -AsPlainText -Force
$Cred = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $username, $PassWord
# �½�ͨ����ͨ��UACԶ�̵������
$Session = New-PSSession -VMName $vmname -Verbose -Credential $Cred
# Ѱ��VMCX�ļ�
$vmcx_name = Get-ChildItem -Path "$vmloc\$vmname\Virtual Machines" -Filter "*.vmcx" -Name
## $vmcx_name = Get-ChildItem -Path "D:\VMachines\Hyper-V\test_244\Virtual Machines\test_244\Virtual Machines" -Filter "*.vmcx" -Name
# ɾ��.VMCX��׺����ȡVMID
$vmid = $vmcx_name.Replace(".vmcx","")
## Write-Output $vmid
# ���������ִ�и��Ĳ���������
Invoke-Command -Session $Session -ScriptBlock {param($vmid) & Rename-Computer -NewName "$vmid" -Force -Restart} -ArgumentList $vmid

