#param($vmname,$vhdsize,$vhdloc)
#New-VHD -Path $vhdloc -SizeBytes $vhdsize

param($vmname,$vhdloc,$vhdname,$vhdcontrollertype,$vhdcontrollernum,$vhdcontrollerloc)
# controller 详细用法请见 remove_vhd 模块
Add-VMHardDiskDrive -VMName $vmname -Path "$vhdloc\Virtual Hard Disks\$vhdname.vhdx" -ControllerType $vhdcontrollertype -ControllerNumber $vhdcontrollernum -ControllerLocation $vhdcontrollerloc

