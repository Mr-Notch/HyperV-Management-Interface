param($vmname,$vmloc)

Remove-VM -Name $vmname -Force
Remove-Item -Path "$vmloc\$vmname\*" -Recurse
Remove-Item -Path "$vmloc\$vmname" -Recurse