param($vmname,$isoloc,$dvdcontrollernum,$dvdcontrollerloc)
# controller ��ϸ�÷���� remove_vhd ģ��
Set-VMDvdDrive -VMName $vmname -Path $isoloc -ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc