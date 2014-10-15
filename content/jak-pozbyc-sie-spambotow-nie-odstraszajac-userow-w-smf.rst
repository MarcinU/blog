Jak pozbyć się spambotów nie odstraszając userów w SMF
######################################################
:date: 2011-02-01 23:02
:author: Hrv
:category: Internet
:tags: smf
:slug: jak-pozbyc-sie-spambotow-nie-odstraszajac-userow-w-smf

Od zarania internetu trwa nieprzerwana walka między developerami
opracowującymi coraz to nowe sposoby odsiewania spamu z spamerami
piszącymi coraz sprawniejsze i bardziej "inteligentne" spamboty. Do
niedawna lekiem na całe zło w przypadku forów na silniku SMF była
implementacja ReCaptcha, i przyznaje działała całkiem sprawnie. Niestety
jak donosi  `world wide
łeb <http://tech.slashdot.org/story/11/01/11/1411254/Google-ReCAPTCHA-Cracked?from=rss>`_
(a przedewszystkim ilość spambotów na moich forach) na złamanie i tego
mechanizmu znalazł się sposób. Obserwując średnio 10-15 wrogich
rejestracji na dzień, rozpocząłem poszukiwania odpowiedniej broni.
Szukałem rozwiązań jak najmniej uciążliwych dla użytkowników z krwi i
kości, bo przecież co mi po sprawnej filtracji Spambotów jeśli userzy
też będą mieli problem z przejściem weryfikacji. Po odrobinie researchu
i kilku dniach testów mogę zdecydowanie polecić dwie modyfikacje:

1.
`Areyouhuman <http://custom.simplemachines.org/mods/index.php?mod=999>`_-
mechanizm genialny w swojej prostocie, zadaje użytkownikowi przy
rejestracji jedno dodatkowe pytanie "Czy jesteś człowiekem?" (lub "Czy
jesteś robotem?").  Oczywiście zastosowano odpowiednie środki
utrudniające zautomatyzowanie udzielenia prawidłowej odpowiedzi -
kolejność odpowiedzi jak i pytanie jest generowane losowo.  To jako
samodzielny spamblocker bez ReCaptcha przepuszczało około 5  Spambotów
na dzień - czyli około 30-50% procent tego co puszczała ReCaptcha.

2.
`Stopforumspam <http://custom.simplemachines.org/mods/index.php?mod=1519>`_-
to prawdziwy strzał w 10tkę. Jest to mechanizm całkowicie transparentny
dla użytkownika, działający podobnie jak popularny min. w Wordpressie
Akismet.
Korzysta z  API -
`www.stopforumspam.com <http://www.stopforumspam.com/>`_ i jest
wyjątkowo skuteczny. Od implementacji  tego moda kilka dni temu jeszcze
żadnem botowi nie udało się zarejestrować, więc rokuje bardzo dobrze :)

Myślę, że samo Stopforumspam da sobie radę wyśmienicie. Areyouhuman mi
się bardzo spodobało, do tego może być przykrywką dla innych rzeczy
które dzieją się 'pod spodem' ;)

