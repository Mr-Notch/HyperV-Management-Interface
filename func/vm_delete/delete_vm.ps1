param($vmname,$vmloc)
#$vmname="python_importvm_func_1"
#$vmloc="E:\VirtualMachine\Hyper-V"
# 小心重命名以后Hyper-V与路径下的vmname不符合
# 后期一定要做好对照表工作（将改过名的vmname与路径下的vmname做键值对比对）
#Remove-VM -Name $vmname -Force
Remove-Item -Path "$vmloc\$vmname\*" -Recurse
Remove-Item -Path "$vmloc\$vmname" -Recurse