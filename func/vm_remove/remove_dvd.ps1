param($vmname,$dvdcontrollernum,$dvdcontrollerloc)
# controller ��ϸ�÷���� remove_vhd ģ��
Remove-VMDvdDrive -VMName $vmname -ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc