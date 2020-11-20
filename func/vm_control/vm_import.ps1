param($templatename,$templateloc,$vmname,$vmloc)
#$templatename="test_244"
#$templateloc="D:\VMachines\Hyper-V\outputVM"
#$vmname="test_244_copy"
#$vmloc="D:\VMachines\Hyper-V"
$vmcx=Get-ChildItem -Path "$templateloc\$templatename\Virtual Machines" -Recurse -ErrorAction SilentlyContinue -Filter "*.vmcx" -Name
Import-VM -Path "$templateloc\$templatename\Virtual Machines\$vmcx" -Copy -GenerateNewId -VirtualMachinePath "$vmloc\$vmname" -VhdDestinationPath "$vmloc\$vmname\Virtual Hard Disks" -SnapshotFilePath "$vmloc\$vmname" | Rename-VM -NewName $vmname -Passthru
