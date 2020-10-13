param($vmname)

Get-VM -Name $vmname | Out-File -Encoding utf8 -FilePath showVM-out.txt