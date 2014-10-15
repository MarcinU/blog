Odzyskiwanie danych w ext3
##########################
:date: 2009-03-09 16:38
:author: Hrv
:category: Linux
:tags: ext3, restore
:slug: odzyskiwanie-danych-w-ext3

Na wstępie chciałem zaznaczyć, że nie czuję się mega ekspertem w
sprawach linuxowych systemów operacyjnych i ratowania danych. Jednak
dzięki `Wizard Mounterowi wyparowało mi trochę
danych <http://www.harv.pl/2009/03/krytyczny-bug-w-wizard-mounterze/>`_,
przez co nabyłem trochę doświadczenia w tej materii. Stąd pomysł, żeby
conieco napisać.

Pierwsza, podstawowa zasada w tej trudnej sytuacji - **nie panikować**.
Google na pierwszy rzut oka nie nastraja pozytywnie, w różnych FAQ
wyczytamy, że w ext3 nie ma undelete, i że się nie da odzyskiwać danych.
Nie jest to do końca prawda. Metoda, którą opisze poniżej, nie jest
idealna, ale u mnie zadziałała całkiem nieźle.

Krok pierwszy po utracie danych to podmontowanie dysku z którego
zniknęły dane w trybie read only, żebyśmy niczego sobie przez przypadek
nie nadpisali. Np. następującym poleceniem

::

    mount -o remount,ro /dev/[nasz dysk]

Teraz już jesteśmy relatywnie bezpieczni i więcej szkody już sobie nie
wyrządzimy.  Do dalszej pracy będziemy potrzebowali dwóch narzędzi
*debugfs* oraz *Sleuth Kit*. Ten pierwszy raczej jest dość powszechnie
instalowany domyślnie. \ *Sleuth Kit* możemy doinstalować, np. w
debianopochonych systemach komendą

::

    apt-get install sleuthkit

Krok drugi, "podpinamy" się debugiem pod nasz system plików

::

    # debugfs /dev/[nasz dysk]

    debugfs 1.40-WIP (14-Nov-2006)

    debugfs:

Teoretycznie da się w debugfs zmieniać swobodnie katalogi używając
komendy *cd*, próbowałem na różne sposoby, i zawsze pluło errorami. Ale
cóż, bez tego też można żyć. Aby wylistować zawrtość dysku używamy:

::

    debugfs:  ls -d

Wynikiem są  takie ciągi :
 `` <32705> (16) Filmy ``
 W nawiasach jest zawarty numer inode, będzie nam on potrzebny do
zlokalizowania danych fizycznie na dysku. W tym celu wpisujemy
 `` debugfs: imap <32705>``
 I otrzymujemy coś takiego:

::

    Inode 32705 is part of block group 1

            located at block 32780, offset 0x0000

Stąd wiemy, że folder *Filmy* należy do grupy pierwszej.  Wychodzimy z
debugfs (komenda *q* ). Teraz trzeba się dowiedzieć jakie bloki należą
do grupy 1.  Do tego celu użyjemy narzędzia fsstat. Przy dużych dyskach
wynik może być zbyt długi, żeby się "zmieścić" w konsoli zatem wrzucimy
go do pliku:

::

    # fsstat /dev/[nasz dysk] > fs 

Otwieramy plik fs, i szukamy interesującej nas grupy.

::

    Group: 1:

      Inode Range: 32705 - 65408

      Block Range: 32768 - 65535

Skoro już wiemy gdzie fizycznie, leżą nasze dane. Zrzućmy sobie ten
obszar pamięci do pliku:

::

    # dls /dev/hdb5 32768 - 65535 > /tmp/raw_data

Oczywiście zakładam, że /tmp jest na innej partycji/dysku niż /dev/hdb5.

Gdy już mamy gotowy plik źródłowy, czas wyszukać nasze pliki. Pomoże nam
tu pakiet foremost, służy on do wyszukiwania nagłówków plików, domyślnie
obsługuje kilkanaście formatów obrazów (jpg, png, tif,) , plików
skompresowanych (zip), dokumentów worda, pdf itp. Do dzieła. W konsoli
wpisujemy:

::

    # foremost -d -i /tmp/raw_data  -o /tmp/restore

W zależności od tego jak duży był plik źródłowy po kilku/kilkunastu
minutach w katalogu /tmp/restore znajdziemy wszystkie pliki,
pokatalogowane według typu, które foremostowi udało się dopasować.
 Niestety pojedyncze pliki nazywane są kolejnymi numerami, więc przy
większej ilości zagubionych danych czeka nas żmudne przeglądanie i
zmienianie nazw plików.

Jak już pisałem metoda nie jest idealna, ale za to relatywnie łatwa w
implementacji i raczej skuteczna. W następnym odcinku opiszę trochę
samego foremosta i kilka słów jak dodawać swoje sygnatury plików.

**Oczywiście wszystkie powyższe czynności wykonujesz na własną
odpowiedzialność. Nie daję gwarancji, że u Ciebie to zadziała.**
