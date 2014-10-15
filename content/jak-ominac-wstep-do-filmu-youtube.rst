Jak ominąć wstęp do filmu Youtube?
##################################
:date: 2008-10-14 13:34
:author: Hrv
:category: Internet
:tags: how-to, Youtube
:slug: jak-ominac-wstep-do-filmu-youtube

Osadzamy filmy z YouTube aby zwizualizować treść artykułu, jednak nie
zawsze film jest dla nas od początku interesujący. Co w przypadku jeśli
chcielibyśmy, aby rozpoczynał się w okreslonym momencie, pomijając np.
pierwsze 90 sekund?

Żaden problem. Osadzajac odtwarzacz na naszej stronie możemy mu nadać
serię parametrów, jednym z nich jest

.. raw:: html

   <div class="pre">

``&start= ilość sekund``

.. raw:: html

   </div>

Demo:

Oto źródło:

.. raw:: html

   <div class="pre">

``<object width="425" height="344"> <param name="movie" value="http://www.youtube.com/v/O9mEKMz2Pvo&hl=pl&fs=1&start=40"></param> <param name="allowFullScreen" value="true"></param> <embed src="http://www.youtube.com/v/9mEKMz2Pvo&hl=pl&fs=1&start=40" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"> </embed></object>``

.. raw:: html

   </div>

Metoda ta ma jedną 'wadę', mianowicie po obejrzeniu całego filmu,
odtwarzanie rozpoczyna się od początku.
