param($vmname,$ramsize)
Set-VMMemory -VMName $vmname -StartupBytes $ramsize -DynamicMemoryEnabled $true
