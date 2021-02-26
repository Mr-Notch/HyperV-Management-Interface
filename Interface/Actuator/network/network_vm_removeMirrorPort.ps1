param($portid)
Remove-NetNatStaticMapping -StaticMappingID $portid -AsJob
