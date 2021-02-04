#param($vmname,$isoloc,$dvdcontrollernum,$dvdcontrollerloc)
param($vmname,$isoloc)
# controller 详细用法请见 remove_vhd 模块
Set-VMDvdDrive -VMName $vmname -Path "$isoloc" #-ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc