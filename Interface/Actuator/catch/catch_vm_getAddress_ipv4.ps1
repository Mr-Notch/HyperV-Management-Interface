param($vmname)

$IP = ( GEt-VM -VMName $vmname | Get-VMNetworkAdapter).IpAddresses[0]
if(!$IP){
    Write-Output "null"
} else {
    Write-Output $IP
}

