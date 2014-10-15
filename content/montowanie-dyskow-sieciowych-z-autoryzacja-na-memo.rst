Montowanie dysków sieciowych z autoryzacją na Memo
##################################################
:date: 2009-01-23 20:55
:author: Hrv
:tags: maemo, NFS, samba
:slug: montowanie-dyskow-sieciowych-z-autoryzacja-na-memo

Używając tabletu internetowego w domu, często przewijał się problem z
dostępem do plików, które akurat miałem na głównym komputerze.
Żonglowanie kartami SD jest średnio wygodne, każdorazowe podpinanie się
przez USB, bluetooth, podobnie, szczególnie, że mam WiFi w całym domu.
Postanowiłem więc podmontować sobie dyski serwerowe i w ten sposób
wymieniać się plikami pomiędzy n800, a resztą domu.

Brzmi genialnie prosto, niestety, jak na linuxa przystało, wcale takie
nie jest :) Pomijając zbędny wstęp przejdźmy do how-to.

Po pierwsze będziemy potrzebowali dostęp do konta roota. Sposobów na
jego osiągnięcie jest kilka, ja używam pakietu
`rootsh/gainroot <http://maemo.org/downloads/product/OS2008/rootsh/>`_.

Następnie, będzie nam potrzebny moduł jądra obsługujący CIFS, można go
pobrać z `forum
Internettabletalk <http://www.internettablettalk.com/forums/showthread.php?t=11836&highlight=CIFS&page=2>`_,
lub `przemirrorowany
odemnie <http://www.harv.pl/wp-content/uploads/2009/01/diablo-cifstar.gz>`_.

Gdy już zbierzemy komplet narzędzi, zabierzmy się do pracy.  Paczka z
modułem, jest spakowana z pełną ścieżką dostępową i po zastosowaniu :

::

    tar xzvf diablo-cifs.tar.gz

moduł powinien znaleźć się w katalogu: /lib/modules/2.6.21-omap1/

Następnie przechodzimy na konto roota (gainroot) i 'włączamy' moduł cifs

::

    insmod /lib/modules/2.6.21-omap1/cifs.ko

Po udanym insmodowaniu możemy już swobodnie podmontowywać nasze zasoby
sieciowe. Przykładowa składnia komendy montującej:

::

    mount.cifs //SERVER/współdzielony_zasób /home/user/MyDocs/lan/dysk_sieciowy -o user=SERVER\\użytkownik,pass=hasło

Dla własnej wygody warto stworzyć sobie skrypt w bashu automatyzujący tą
czynność i dodać go do `Personal
Menu <http://maemo.org/downloads/product/OS2008/personal-menu>`_.
Aplikacja ta jest o tyle użyteczna, że pozwala wywoływać skrypty z
uprawnieniami roota, więc możemy w naszym skrypcie pominąć
gainroot-owanie.
