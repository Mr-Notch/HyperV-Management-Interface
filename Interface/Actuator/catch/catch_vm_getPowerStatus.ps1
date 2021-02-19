param($vmname)
Get-VM $vmname | Select-Object State | Format-Wide