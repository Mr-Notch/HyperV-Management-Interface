#param($vmname,$isoloc,$dvdcontrollernum,$dvdcontrollerloc)
param($vmname,$isoloc)

Set-VMDvdDrive -VMName $vmname -Path "$isoloc" #-ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc
