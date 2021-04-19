Montowanie dysków sieciowych z GUI
##################################
:date: 2009-01-28 16:52
:author: Hrv
:tags: maemo,samba,n800
:slug: montowanie-dyskow-sieciowych-z-gui

Aż dziw bierze, że nikt nie ochrzanił mnie za marny research przed
napisaniem mojego `ostatniego posta o montowaniu dysków sieciowych z
autoryzacją <http://harv.pl/blog/montowanie-dyskow-sieciowych-z-autoryzacja-na-memo.html>`_.
Dopiero przed chwilą, wpadłem i przetestowałem `Wizard
Mounter <https://garage.maemo.org/projects/wizard-mounter/>`_. Program
ten ma za zadanie ułatwić nam montowanie różnego rodzajów zasobów
zarówno NFS jak i Samba, z autoryzacją i bez, a wszystko w trybie
graficznym.

.. figure:: /images/archive/wmounter.png
        :alt: Wizard mounter

Wizard Mouter

Przed instalacją jednak musimy się jak zwykle przygotować. Wizard
Mounter do działania potrzebuje dwóch
pakietów: kernel-diablo-modules-extra i portmap. Znajdziemy je w
repozytorium diablo/tools. Jeśli go nie mamy to musimy je dodać.

.. figure:: /images/archive/repo.png 
   :alt: Konfiguracja repozytorium

Konfiguracja repozytorium

Następnie instalujemy wyżej wymienione pakiety np. za pomocą xterminala:

.. code-block:: bash

    apt-get install kernel-diablo-modules-extra portmap

Po zakończeniu instalacji pobieramy najnowszą paczkę ze `strony projektu
Wizard Mounter <https://garage.maemo.org/frs/?group_id=444>`_,
uruchamiamy w Application managerze i cieszymy się bezproblemowym,
łatwym w obsłudze montowaniem zasobów sieciowych.


