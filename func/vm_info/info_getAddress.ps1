param($vmname)
<<<<<<< HEAD
#$ipv4=Get-VMNetworkAdapter $vmname | Select-Object IPAddresses | Format-Wide
#$ipv4 | Where-Object {$_ -notmatch ':'}

# Ö»»ñÈ¡IPV4
$IP = ( GEt-VM -VMName $vmname | Get-VMNetworkAdapter).IpAddresses[0]
Write-Output $IP
=======
Get-VMNetworkAdapter $vmname | Select-Object IPAddresses | Format-Wide
>>>>>>> 04cb11b9e8cf5738281d7f8e28fb494eaf24a006
