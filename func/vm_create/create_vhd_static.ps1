param($vhdsize,$vhdloc,$vhdname)

#$vhdsize=5GB
#$vhdloc="D:\VMachines\Hyper-V\test_277\"
#$vhdname="static-5GB"

#Write-Output $vhdsize

New-VHD -SizeBytes $vhdsize -Path "$vhdloc\Virtual Hard Disks\$vhdname.vhdx"  -Fixed


