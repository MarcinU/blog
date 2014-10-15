Krytyczny Bug w Wizard Mounterze!
#################################
:date: 2009-03-07 15:46
:author: Hrv
:tags: maemo, NFS, samba
:slug: krytyczny-bug-w-wizard-mounterze

Jak to zwykle w życiu bywa po odrobinie słodyczy, nadchodzi całe wiadro
goryczy.  Tak stało się też w przypadku `czarodziejskiego mountera,
którego przywary opisywałem post
niżej <http://www.harv.pl/2009/01/montowanie-dyskow-sieciowych-z-gui/>`_.

Okazuje się, że owy czarnoksiężnik poza łatwym i prostym zamontowaniem
naszych plików na tablecie, potrafi je równie sprawnie usunąć.  Nie będę
tutaj wylewał gorzkich łez, ani wymachiwał pięciami przeklinając każdy
bit kodu tej aplikacji. Pozwolę sobię tylko suchy opis problemu.

Jeśli zainstalowaliście Wizard Mountera w wersji wcześniejszej niż
obecnie akutalna (1.2), czyli np 1.1 , i dodaliście odpowiednie
repozytoria, przy przeprowadzaniu aktualizacji programów zainstalowanych
na Waszym tablecie, zostanie Wam zaproponowana też akualizacja Wizard
Mountera. I w tym miejscu przechodzimy do sedna.

**Nie pozwalajcie na aktualizacje Wizard Mountera jeśli wcześniej ręcznie nie odmontowaliście podmontowanych zasobów.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wersja 1.1 podczas aktualizacji rekursywnie usuwa wszystkie foldery z
Remote\_Filesystems (bez sprawdzania czy zasoby zostały odmontowane czy
nie). **USUWAJĄC** **jednocześnie (jeśli user zalogowany do zasobu
posiada odpowienie uprawnienia) WSZYSTKIE WASZE PODMONTOWANE PLIKI.**\ 

Dość niemiła niespodzianka, nieprawdaż?  Błąd zgłosiłem developerom,
póki co bez odzewu.

W następnym odcinku małe how-to jak odzykać część usuniętych plików w
systemie ext3.

PS Nie pytajcie ile danych straciłem...
