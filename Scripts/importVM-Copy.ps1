param($vmname,$vmloc,$templatename,$templateloc)
$vmcxloc=Get-ChildItem -Path $templateloc -Recurse -ErrorAction SilentlyContinue -Filter *.VMCX -Name
Write-Output $vmcxloc
Import-VM -Path $templateloc\$vmcxloc -Copy -GenerateNewId -VirtualMachinePath $vmloc\$vmname\$vmname -VhdDestinationPath $vmloc\$vmname\Disks -SnapshotFilePath $vmloc\$vmname\$vmname
Rename-VM -Name $templatename -NewName $vmname
Get-VM -Name $vmname | Out-File -Encoding utf8 -FilePath importVM_Copy-out.txt

