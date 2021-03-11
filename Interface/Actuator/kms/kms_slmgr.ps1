param($vmname,$username,$userpasswd)

$PassWord = ConvertTo-SecureString -String "$userpasswd" -AsPlainText -Force
$Cred = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $username, $PassWord
# 新建通道并通过UAC远程到虚拟机
$Session = New-PSSession -VMName $vmname -Verbose -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {slmgr -skms kms.03k.org | slmgr -ato}

