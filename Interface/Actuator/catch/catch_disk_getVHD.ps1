param($vmname,$format)
# $format有多种格式：
# VMName ControllerType ControllerNumber ControllerLocation DiskNumber Path

# 不要修改if条件语句s
# 获取类型依赖此BUG运行
# 获取Path的时候为null，而获取其他东西的时候确是返回结果
# 故此py那边的判断path获取为 not in

# 已修复此BUG（Issue-201）
$var=(Get-VM -Name $vmname | Get-VMHardDiskDrive).$format

if([String]::IsNullOrEmpty($var)){write-output 'null'} else {& { "'$($var -join "','")'" }}