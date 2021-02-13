param($vmname,$ramsize,$cpunum,$vmswitchname,$vmloc)

#$vmname='test-233'
#$ram=2GB
#$cpu=2
#$vmswitchname='vmnet'
#$disk=30GB
#$vmloc='D:\VMachines\Hyper-V'
#$isoloc='D:\迅雷下载\cn_windows_server_2019_updated_july_2020_x64_dvd_2c9b67da\cn_windows_server_2019_updated_july_2020_x64_dvd_2c9b67da.iso'



#New-VM -Name $vmname -Path "$vmloc" -MemoryStartupBytes $ram -NewVHDPath "$vmloc\$vmname\Virtual Hard Disks\Main-$disk.vhdx" -NewVHDSizeBytes $disk -SwitchName $vmswitchname -Generation 1 -Force
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

# 其实我想写是否安装VHD来着，但打算放到日后更新里写，我怕和web网页对接不上

New-VM @VM -NoVHD | Set-VMProcessor -Count $cpunum
#Set-VMDvdDrive -VMName $vmname -Path $isoloc
#
#Set-VMProcessor -VMName $vmname -Count $cpunum