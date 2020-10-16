param($vmname)

Start-VM -Name $vmname | Out-File -Encoding utf8 -FilePath startVM-out.txt
