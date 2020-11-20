param($vhdsize,$vhdloc,$vhdname)
#$vhdsize=5GB
#$vhdloc="E:\VirtualMachine\Hyper-V\python_createvm_func_0"
#$vhdname="static-5GB"

New-VHD -SizeBytes $vhdsize -Path "$vhdloc\Virtual Hard Disks\$vhdname.vhdx"  -Dynamic