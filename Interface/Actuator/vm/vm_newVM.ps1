param($vmname,$ramsize,$cpunum,$vmswitchname,$vmloc)
# https://docs.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/try-hyper-v-powershell
$VM = @{
    Name = $vmname
    MemoryStartupBytes = $ramsize
    Generation = 1
#    NewVHDPath = "$vmloc\$vmname\Virtual Hard Disks\Main-$disksize.vhdx"
#    NewVHDSizeBytes = $disksize
#    BootDevice = "VHD"
    Path = "$vmloc"
    SwitchName = "$vmswitchname"
}

New-VM @VM -NoVHD | Set-VMProcessor -Count $cpunum
#Set-VMDvdDrive -VMName $vmname -Path $isoloc
#
#Set-VMProcessor -VMName $vmname -Count $cpunum