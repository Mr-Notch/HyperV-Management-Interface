param($vmname)

Restart-VM -Name $vmname -Force | Out-File -Encoding utf8 -FilePath resetVM-out.txt