param($vmname,$ramsize,$cpunum,$vmswitchname,$vmdiskname,$vmdisksize,$vmloc,$isoloc)
New-VM -Name $vmname -Path $vmloc\$vmname -MemoryStartupBytes $ramsize -NewVHDPath $vmloc\$vmname\Disks\$vmdiskname.vhdx -NewVHDSizeBytes $vmdisksize -SwitchName $vmswitchname -Generation 1 -Force | Out-File -Encoding utf8 -FilePath newVM-out.txt

Set-VMDvdDrive -VMName $vmname -Path $isoloc
Set-VMProcessor -VMName $vmname -Count $cpunum