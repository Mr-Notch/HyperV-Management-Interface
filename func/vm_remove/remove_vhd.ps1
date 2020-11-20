param($vmname,$vhdcontrollertype,$vhdcontrollernum,$vhdcontrollerloc)
# vhdcontrollertype: VHD控制器的类型，例如IDE、SATA、SCSI之类的
# vhdcontrollernum：VHD控制器的值（默认为0）
# vhdcontrollerloc：VHD挂载在控制器上的位置（默认为0）
Remove-VMHardDiskDrive -VMName $vmname -ControllerType $vhdcontrollertype -ControllerNumber $vhdcontrollernum -ControllerLocation $vhdcontrollerloc