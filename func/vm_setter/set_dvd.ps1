#param($vmname,$isoloc,$dvdcontrollernum,$dvdcontrollerloc)
param($vmname,$isoloc)
# controller ��ϸ�÷���� remove_vhd ģ��
Set-VMDvdDrive -VMName $vmname -Path "$isoloc" #-ControllerNumber $dvdcontrollernum -ControllerLocation $dvdcontrollerloc