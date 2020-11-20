param($vmname,$vhdname,$vmloc)
#$vmname="test_277"
#$vhdname="seewo-recovery"
#$vmloc="D:\VMachines\Hyper-V"
Remove-Item -Path "$vmloc\$vmname\Virtual Hard Disks\$vhdname.*" -Recurse