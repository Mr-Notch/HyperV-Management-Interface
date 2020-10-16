param($vmname)

Stop-VM -Name $vmname -TurnOff | Out-File -Encoding utf8 -FilePath stopVM-out.txt