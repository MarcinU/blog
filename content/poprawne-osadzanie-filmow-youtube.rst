Poprawne osadzanie filmów Youtube
#################################
:date: 2008-10-19 12:37
:author: Hrv
:category: Internet
:tags: how-to, Youtube
:slug: poprawne-osadzanie-filmow-youtube

Często mamy ochotę z wizualizować nasze treści w Sieci osadzając film z
YouTube. Tylko  co zrobić żeby element osadzony na naszej stronie był
poprawnym XHTMLem? Niestety kod, który dostarcza nam domyślnie YouTube
jest stary i przy walidacji generuje masę błędów, niwecząc godziny
naszej walki z kodem, aby strona była XHTML 1.0 Valid ;)

Znalazłem rozwiązanie tego problemu na blogu
`artsea <http://blog.artesea.co.uk/2008/05/youtube-and-embedding-correctly.html>`_.
Autor oprócz poprawienia kodu proponuje nam także zmniejszenie rozmiaru
osadzanego filmu do 320px. Mnie domyślne skalowanie filmów do 425 px nie
razi więc pozostawiłem te parametry bez zmian.

Oto jak przebiega cały proces:

Youtube dostarcza nam coś na ten kształt:

.. raw:: html

   <div class="pre">

<object width="425" height="344"><param name="movie"
value="http://www.youtube.com/v/USW96TRargU&hl=pl&fs=1"></param><param
name="allowFullScreen" value="true"></param><embed
src="http://www.youtube.com/v/USW96TRargU&hl=pl&fs=1"
type="application/x-shockwave-flash" allowfullscreen="true" width="425"
height="344"></embed></object>

.. raw:: html

   </div>

Wklejając ten kod na swoja stronę dodajemy jakieś 6 nowych błędów
walidacji. Zapiszmy go jednak w innej postaci:

.. raw:: html

   <div class="pre">

<object type="application/x-shockwave-flash" style="width:425px;
height:350px;"
data="http://www.youtube.com/v/USW96TRargU&hl=pl&fs=1"><param
name="movie" value="http://www.youtube.com/v/USW96TRargU&hl=pl&fs=1"
/></object>

.. raw:: html

   </div>

Oto efekt naszej pracy:

Metoda ta jest kompatybilna z dodatkowymi parametrami, do np. `omijania
wstępu filmu </2008/10/jak-ominac-wstep-do-filmu-youtube/>`_.

Dla leniwych jest też strona, która przygotuje nam `poprawny kod
automatycznie <http://www.tools4noobs.com/online_tools/youtube_xhtml/>`_.
