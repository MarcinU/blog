Pelican w kontenerze
####################
:date: 2016-07-30 22:05
:author: Hrv
:tags: DIY, docker
:Category: Linux
:slug: pelian-i-docker

Ostatnimi czasy jest bardzo modne tworzenie kontenerów Dockera właściwie ze wszystkim. Dlatego pomyślalem, dlaczego nie zbudować kontenera do generowania i/lub serwowania treści Pelicana. 

Cudowna wygoda. Nie trzeba walczyć z zależnościami Pythona wszystko czego nam potrzeba w jednej 50 MB paczce gotowe do działania 24/7. 

Jak pomyślałem tak zrobiłem. Efekty mozecie znaleźć na docker-hubie_.

.. _docker-hubie: https://hub.docker.com/u/harv/

W ten oto sposób jesteśmy w stanie z każdej maszyny z zainstalowanym docker-engine kompilować treści dla Pelicana jednym poleceniem:

.. code-block:: bash

	docker run -i --name pelican-render -v [ścieżka/do/plików/pelicana]:/blog harv/pelican-alpine

Jeśli pozostaniemy wierni ścieżkom jakie podaliśmy w komendzie wyżej. Przy następnych aktualizacjach wystarczy:

.. code-block:: bash

	docker start pelican-render


