Transmission zabezpieczone OpenVPN
##################################
:date: 2015-12-26 17:50
:author: Hrv
:tags: DIY, docker
:Category: Linux
:slug: transmission-via-openvpn

Narafiłem niedawno na następujące rozwiązanie: kontener dockera z od razu skonfigurowanym klientem OpenVPN i obsługą większości providerów usług VPN takich jak:

- Private Internet Access
- BTGuard
- TigerVPN
- FrootVPN
- TorGuard
- NordVPN
- UsenetServerVPN
- IPVanish
- Anonine
 

Dokumentację i repo znajdziecie na GitHubie_. 

.. _GitHubie: https://github.com/haugene/docker-transmission-openvpn 

Instalacja i uruchomienie jest bajcznie proste. Przy testatch jedyny problem jaki zauważyłem to opisany w dokumentacji problem z DNS, jednak dodanie odpowiedniego wpisu do skryptu uruchamiającego kontener rozwiązała problem. 

Przy korzystaniu z TransmissionRemote w zasadzie wygoda korzystania jest taka sama jakby to był normalnie zainstalowany klient transmission. 

