param($vmname,$vmloc)
$vmcx_name = Get-ChildItem -Path "$vmloc\$vmname\Virtual Machines" -Filter "*.vmcx" -Name
$vmcx_name.Replace(".vmcx","")