param($vmname,$vhdcontrollertype,$vhdcontrollernum,$vhdcontrollerloc)
# vhdcontrollertype: VHD�����������ͣ�����IDE��SATA��SCSI֮���
# vhdcontrollernum��VHD��������ֵ��Ĭ��Ϊ0��
# vhdcontrollerloc��VHD�����ڿ������ϵ�λ�ã�Ĭ��Ϊ0��
Remove-VMHardDiskDrive -VMName $vmname -ControllerType $vhdcontrollertype -ControllerNumber $vhdcontrollernum -ControllerLocation $vhdcontrollerloc