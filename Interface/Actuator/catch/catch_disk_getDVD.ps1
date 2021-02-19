param($vmname,$format)
# $format有多种格式：
# VMName ControllerType ControllerNumber ControllerLocation DiskNumber Path
$var=(Get-VM -Name $vmname | Get-VMDvdDrive).$format
if([String]::IsNullOrEmpty($var)){write-output 'null'} else {& { "'$($var -join "','")'" }}