param($vmname)

Stop-VM -Name $vmname -Force | Out-File -Encoding utf8 -FilePath stopVM-out.txt