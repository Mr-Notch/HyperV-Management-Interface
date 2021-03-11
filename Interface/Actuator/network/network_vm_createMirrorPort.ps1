param($NatName,$ExternalPort,$InternalIPAddress,$InternalPort,$Protocol)

Add-NetNatStaticMapping -ExternalIPAddress "0.0.0.0/24" -ExternalPort $ExternalPort -Protocol $Protocol -InternalIPAddress "$InternalIPAddress" -InternalPort $InternalPort -NatName $NatName