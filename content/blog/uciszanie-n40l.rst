Wymiana wentylatorów w HP N40L
###############################
:date: 2015-01-07 22:47
:author: Hrv
:tags: DIY
:slug: wymiana-wentylatorow-hp-n40l

Hałaśliwość tego malutkiego serwerka nie dawała mi spokoju. Zwłaszcza, że zawsze miałem na tym punkcie delikatnie mówiąc hopla. 

Po chwili researchu w sieci kupiłem set sprawdzonych Fanderów:

.. role:: strike
       :class: strike

- Fander Roxo 4020L 40mm FRX3-4020L 3000rpm
- :strike:`Fander Roxo 12025P 120mm FRX3-12025P PWM 600-1600rpm` [1]_
- Fander Roxo 12018P 120mm FRX3-12018P PWM 800-1800rpm

Oba są niemal bezgłośne, choć szczerze mówiąc nie spodziewałem się tego po tym 40mm maleństwie.

Wentylator obudowy
------------------
Proces wymiany jest w zasadzie bezproblemowy, trzeba tylko pamiętać o kilku szczegołach: 


HP żeby nam ułatwić nie stosuje się ogólno przyjętego standardu podłączenia wentylatrów i kolejność pinów jest inna. Bardzo dobrze opisane jest to tutaj_.

.. _tutaj: http://www.silentpcreview.com/article1193-page7.html 

TIP: Fander stosuje kolorystykę jak "Some AMD CPU Fans" :) 

Tak wygląda wtyczka pierwotnie:

.. figure:: /images/N40L_fan_1.jpg
        :alt: Wtyczka Fander
        :align: center
        
A tak po zamianie pinów:

.. figure:: /images/N40L_fan_2.jpg
        :alt: Wtyczka Fander dostosowana
        :align: center

Kratki ochronnej nie zamontujemy za pomocą bajeranckich klinów dostarczonych przez HP tylko musimy je wkręcić śrubami dostarczonymi w zestawie przez Fandera. 

Nie poprowadzimy również kabla tak jak pierwotnie bo jest na to zbyt krótki. Jednak bez problemu wystarczy jeśli puśmy go dołem nad płytą główną. 

Wentylator zasilacza
----------------------

.. figure:: /images/N40L_fan_3.jpg
        :alt: Zasilacz po modyfikacji
        :align: center

Przy wymianie wentylatora w zasilaczu czekają na nas tylko trzy pułapki. 

Pierwsza to dwupinowe łącze zasilania i  mało miejsca na kabel więc raczej nie obejdzie się bez docinania i przeróbek. 

Druga, tylko wyczytana w sieci_, to fakt że zasilacz na to złącze podaje tylko 5V co dla niektórych wentylatorów może stanowić problem przy rozruchu.

.. _sieci: http://kevinelp.wordpress.com/2014/10/13/replacing-the-fans-in-my-hp-n40l-microserver 

Ja postanowiłem sobie życie uprościć i wypuściłem kabel zasilający poza obudowę zasilacza, podłączając go do Molexa na 12V :) 




Ostatni problem do rozwiązania to wielkość otworów montażowych Fandera. Niestety nie pasowały do niego ani pierwotne śruby, ani o dziwo te dostarczone przez producenta wentylatora, na szczęście miałem dwie stare śruby sprzed kilku lat :) 

U mnie po przeprowadzeniu poważyszych modyfikacji zmiana jest kolosalna.

.. [1] Oryginalny wentylator HPka kręci się ponad 1000rpm. Dlatego serwer ten dość panicznie (twardym shutdown) reaguje jeśli wykryje, że obroty spadły poniżej 500rpm (co się czasami zdarza wolniejszemu Fanderowi). Po kilkunastu nieplanowanych restartach zdecydowałem się na głośniejszego Fandera startującego od 800 obrotów na minutę. Po problemie.
