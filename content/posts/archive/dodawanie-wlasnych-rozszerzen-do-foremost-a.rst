Dodawanie własnych rozszerzeń do foremost-a
###########################################
:date: 2009-03-11 16:34
:author: Hrv
:category: Linux 
:tags: how-to
:slug: dodawanie-wlasnych-rozszerzen-do-foremost-a

Tak jak obiecałem w moim poprzednim `tekście o odzyskiwaniu danych z
partycji
ext3 <http://www.harv.pl/2009/03/odzyskiwanie-danych-w-ext3/>`_,
podzielę się kilkoma swoimi doświadczeniami z używania foremost-a.

Jak już pisałem wcześniej, Foremost standardowo obsługuje tylko
najbardziej popularne formaty plików. Problem pojawia się w momencie,
gdy zginie nam coś bardziej nietypowego. W moim przypadku, były to pliki
psd. Po krótkim poczytaniu manuala postanowiłem sobie dodać ten format
do definicji foremost-a. Aby to zrobić należy wyedytować standardowy
plik konfiguracyjny (domyślnie /etc/foremost.conf). Bezpośrednio po
instalacji wszystkie obsługiwane typy plików są zakomentowane, w takim
przypadku foremost wykonuje wyszukiwanie za pomocą wbudowanych filtrów.
 Przejdźmy jednak do rzeczy. Proces dodawania nowego rozszerzenia opiszę
na przykładzie w/w pliku psd.  Oto co musiałem dodać, żeby foremost
rozpoznawał ten format:

.. code::

    psd     y       10000000      \x38\x42\x50\x53

Od lewej: rozszerzenie, czy wielkość liter ma znaczenie, wielkość pliku
, nagłówek. Można jeszcze dodać stopkę pliku, jednak przy psd nie byłem
w stanie takowej stwierdzić. Pierwsze trzy pozycje myślę, że są jasne i
nie wymagają szerszego omówienia. Ale skąd wziąc informacje do
wypełnienia czwartek i ewentualnie piątej pozycji ?

Ja w tym celu posłużyłem się hexeditorem, wrzucałem do niego kolejno
kilka plików z rozszerzeniem psd i szukałem elementów wspólnych. Okazało
się, że wszystkie zaczyną się tak
samo:


.. figure:: /images/2009/03/hex.jpg
        :alt: Hex
        :align: center

        Plik PSD

Zgodnie z manualem każdą z wartości hexadecymalnch poprzecamy znakiem
" x " , a poszczególne zapisy oddzielamy za pomocą " \\ " . Dopuszczalne
są też symbole maski - " \* " dla wielu i " ? " dla pojedynczego znaku.

Jeśli format plików, który dodajemy posiada też jakąś standardową
stopkę, dodajemy ją po definicji nagłówka oddzielając je tabulatorem.

Skuteczność nie jest stuprocentowa, ale udało mi się odzyskać kilka
wyjątkowo mi potrzebnych plików. Zachęcam do eksperymentów, byćmoże da
się ten pattern udoskonalić.

