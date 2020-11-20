#param($vmname,$vhdsize,$vhdloc)
#New-VHD -Path $vhdloc -SizeBytes $vhdsize

param($vmname,$vhdloc,$vhdname)
Add-VMHardDiskDrive -VMName $vmname -Path "$vhdloc\Virtual Hard Disks\$vhdname.vhdx"

