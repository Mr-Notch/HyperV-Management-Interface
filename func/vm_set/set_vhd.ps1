#param($vmname,$vhdsize,$vhdloc)
#New-VHD -Path $vhdloc -SizeBytes $vhdsize

param($vmname,$vhdloc,$vhdname,$vhdcontrollertype,$vhdcontrollernum,$vhdcontrollerloc)
# controller ��ϸ�÷���� remove_vhd ģ��
Add-VMHardDiskDrive -VMName $vmname -Path "$vhdloc\Virtual Hard Disks\$vhdname.vhdx" -ControllerType $vhdcontrollertype -ControllerNumber $vhdcontrollernum -ControllerLocation $vhdcontrollerloc

