Title: Instalacja Sensu na FreeNAS
Date: 2016-10-26 19:50
Author: Hrv
Tags: freeNAS, sensu
Slug: instalacja-sensu-freenas

Od jakiegoś czasu monitoruję swoje systemy z użyciem Sensu (po ucieczce z Nagiosa). Niedawno naszła mnie ochota zainstalować sensu-client też na moim domowym NASie. Zatem stworzyłem sobie na tę potrzebę jail, i zacząłem się bawić. 

## Co będzie potrzebne? 
- Jako, że tu konfigurujemy tylko klienta, dostęp do serwera Sensu
- FreeNAS w wersji 9.10+ lub FreeBSD w wersji 10+
- Dostęp do internetu. 


## Instalacja 

Ja wybrałem instalację w jailu, ale generlanie pewnie z powodzeniem możecie tę instalację przeprowadzić na głównym systemie, choć ja bym tego nie robił :) 

Zaczynamy od pobrania odpowiedniej paczki ze strony Sensu - [Sensu](https://sensuapp.org/downloads)

```
wget https://sensu.global.ssl.fastly.net/freebsd/10.0/amd64/sensu-0.26.3_1.txz
```
Możliwe, że wget będzie Wam brakował więc:
```
pkg install wget
```

Następnie instalujemy paczkę sensu:

```
pkg add sensu--0.26.3_1.txz
```

Tada! ;) 

## Podstawowa konfiguracja 

Wszystkie standardowe pliki konfiugracyjne znajdziecie w 
```
/usr/local/etc/sensu/ 
```

Tak jak na innych platformach wystarczy stworzyć swój config.json i plik konfiguracji transportu w /usr/local/etc/sensu/conf.d. To akurat jest dobrze opisane w [dokumentacji](https://sensuapp.org/docs/latest/platforms/sensu-on-freebsd.html#sensu-core)

## Uruchomienie 

Aby uruchomić klienta najpierw musimy go włączyć w /etc/rc.conf. Zatem dodajemy tę linię:

```
sensu_client_enable="yes"
```
Następnie odplamy serwis:
```
service sensu-client start  && service sensu-client status
```

Możemy się utwierdzić w przekonaniu czy się udało czy nie zaglądając do /var/log/sensu/


## Checki

I tu kosa trafia na kamień. Niestety, sporo standardowych checków Sensu na FreeBSD/NAS nie działa (czego z resztą można było się spodziewać). Zatem należołby utworzyć dla tej maszyny osobną subskrybcję z własnymi checkami.

Checki które działają, mniej lub bardziej:

- sensu-plugins-network-checks
- sensu-plugins-disk-checks
 

## Problemy, bonusy ;)

Okazuje się, że Sensu-client na BSD nie jest tak stabilny jak na pozostałych platformach i potrafi czasami umrzeć. Jako, że standardowo usługi nie są z automatu restartowane jeśli sfailują. Napisałem sobie watchera, którego odpalam co dwie minuty z crontaba:

``` bash
#!/usr/local/bin/bash

pid=$(cat /var/run/sensu/sensu_client.pid)

status=$(/usr/sbin/service sensu-client status | grep $pid > /dev/null ; echo $?)

if [ $status -eq 1 ]; then
	/usr/sbin/service sensu-client start
fi
```
Dlaczego akurat co dwie? Bo chciałbym dostać informację, że były jakieś problemy, a mój standardowy próg pierwszego powiadomienia o braku komunikacji z jakimś urządzeniem to 60 sekund. Może za jakiś czas, jeśli mnie to bardzo będzie nękało, będę odpalał watchera co minutę żeby cieszyć się spokojem ;)
  
