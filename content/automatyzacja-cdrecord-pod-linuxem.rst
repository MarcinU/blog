Automatyzacja cdrecord pod Linuxem 
###################################
:date: 2008-10-19 00:18
:author: Hrv
:category: Linux
:tags: how to 
:slug: automatyzacja-cdrecord-pod-linuxem

Odkąd zastąpiłem puszkowego PCta notebookiem, mój domowy serwer musi
spełniać coraz  to więcej funkcji. Jedną z nich stało się nagrywanie
płyt CD , DVD, jako , że większość danych trzymam na dysku serwera
głupotą byłoby przesyłanie 4,7 GB danych przez WiFi tylko po to żeby je
wypalić.  Jako że serwer działa tylko w trybie konsoli, o programach
typu k3b, gnomebaker trzeba było zapomnieć i sięgnąć po cdrecord.

Cdrecord to konsolowe narzędzie wykorzystujące pakiet wodim do
nagrywania płyt CD , DVD jednak nagrywa tylko obrazy płyt, które trzeba
sobie przygotować samemu np za pomocą **mkisofs** albo **dd**.  Jednak
zapamiętywanie ich składni, wykonywanie tych poleceń po kolei, do tego
przy większej ilości kopii jest dosyć kłopotliwe.

Nieprzerwanie nękany tymi niedogodnościami postanowiłem popełnić prosty
skrypt shellowy automatyzujący część tych zadań, tak abym nie musiał
pamiętać komend, składni, switchów etc. Skrypt testowałem tylko na
sobie, stąd oznaczony jest wersją 0.1 beta, dodatkowo to pierwsza moja
przygoda z dłuższymi skryptami shellowymi więc za wszelkie komentarze
będę wdzięczny.

Do rzeczy jednak. Co ten skrypt potrafi ? Przede wszystkim to czego
brakowało mi w windowsowym CDBurnerze XP - skopiować płytę kilka razy.
Ale po kolei.

**Skrypt możemy uruchomić z czterema przełącznikami:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  -c - kopia płyty (zadaną ilość razy)
-  -r - nagranie gotowego pliku obrazu(zadaną ilość razy)
-  -b - stworzenie obrazu ze wskazanego folderu i wypalenie go (zadaną
   ilość razy)
-  -batch - nagranie po kolei wszystkich obrazów iso w zadanym folderze

Przed wykonaniem nagrania, skrypt sprawdza czy na pewno w napędzie
znajduje się pusta płyta (zdarzyło mi się przez przypadek jakimś cudem
nadpisać nagrany nośnik)

**Skrypt posiada kilka opcji konfiguracyjnych  w nagłówku:**

.. raw:: html

   <div class="pre">

#Plik tymczasowy
 tf=/tmp/\`date +%s\`.iso

.. raw:: html

   </div>

Tu wybieramy gdzie mają się zapisywać tymczasowe pliki, które powstają
podczas kopiowania i nagrywania folderów, oraz jak mają się nazywać.
Domyślnie nazwą pliku jest ilość sekund od 1970 roku;)

.. raw:: html

   <div class="pre">

#Adres napedu
 DEV=/dev/hdc

.. raw:: html

   </div>

Adres napędu optycznego.  Ten sam odczytuje i nagrywa płyty w przypadku
kopiowania.

.. raw:: html

   <div class="pre">

#Pytaj o parametry nagrywania t/n (domyslnie nie)
 PARAMS=N

.. raw:: html

   </div>

Jeśli wybierzemy 'T' przed każdym nagraniem skrypt będzie pytał o
parametry cdrecord'a.  Przy wybraniu 'N', cdrecord będzie pracował z
domyślną prędkością i parametrami -v -eject .

OBSŁUGA
~~~~~~~

Zakładam, że mkisofs, cdrecord, dd jest już zainstalowane (tutorial jak
te pakiety zainstalować i obsługiwać za jakiś czas). Kopiujemy plik na
naszą linuxową maszynę, nadajemy mu atrybut wykonywalności

.. raw:: html

   <div class="pre">

chmod +x nagraj

.. raw:: html

   </div>

Teraz wystarczy go wykonać z odpowiednim parametrem np:

.. raw:: html

   <div class="pre">

./nagraj -c

.. raw:: html

   </div>

I postępować wg. poleceń na ekranie ;)

BUGI
~~~~

Pliki obrazów iso przy nagrywaniu 'masowym' nie mogą zawierać w nazwie
spacji bo skrypt się wywali ;)

DOWNLOAD
~~~~~~~~

`CD/DVD Burner by
Harv <http://harv.pl/wp-content/uploads/2008/10/nagraj>`_

Za wszelkie komentarze, propozycje funkcji , zgłoszenia błędów itp będę
wdzięczny.
