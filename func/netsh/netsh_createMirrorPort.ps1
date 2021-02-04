param($listenport,$connectaddress,$connectport)

netsh interface portproxy add v4tov4 listenport=$listenport connectaddress=$connectaddress connectport=$connectport