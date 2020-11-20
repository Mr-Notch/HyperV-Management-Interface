param($vmname,$dvdcontrollernum,$dvdcontrollerloc)
# controller 详细用法请见 remove_vhd 模块
Remove-VMDvdDrive -VMName $vmname -ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc