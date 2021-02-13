param($vmname)
#$ipv4=Get-VMNetworkAdapter $vmname | Select-Object IPAddresses | Format-Wide
#$ipv4 | Where-Object {$_ -notmatch ':'}

# ÷ªªÒ»°IPV4
$IP = ( GEt-VM -VMName $vmname | Get-VMNetworkAdapter).IpAddresses[0]
Write-Output $IP