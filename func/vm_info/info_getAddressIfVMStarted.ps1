param($vmname)
Get-VMNetworkAdapter $vmname | Select-Object IPAddresses | Format-Wide