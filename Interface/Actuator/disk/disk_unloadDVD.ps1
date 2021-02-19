param($vmname,$dvdcontrollernum,$dvdcontrollerloc)

Remove-VMDvdDrive -VMName $vmname -ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc