Smokeping w FreeNASowym jailu
############################################
:date: 2016-01-03 17:20
:author: Hrv
:tags: DIY, FreeNAS
:slug: smokeping-freenas-jail

Już jakiś czas nosiłem się z zamiarem zmontowania jakiegoś lokalnego systemu do monitoringu jakości łącza dostarczanego przez mojego ISP. A cóż :strike:`prostszego` lepszego niż Smokeping_? :) 

.. _Smokeping: http://oss.oetiker.ch/smokeping/

.. role:: strike
          :class: strike


Pozostało pytanie gdzie go zainstalować. Pierwsza myśl to oczywiście jeden z moich Raspberry, ale szczerze mówiąc odkąd padła mi jedna karta SD staram się bardzo ograniczać usługi które piszą po karcie do minimum. Skoro nie Rasp to co? Od dobrego roku korzystam z FreeNASa, dlaczego zatem nie postawić osobnego jaila dla Smokepinga, skoro i tak jest włączony 24/7. Jak to Branson mawia: screw it, lets do it. 

Instalacja Smokeping
--------------------

Nowego jaila można spokojnie wyklikać za pomocą webGUI. Jak już je stworzymy trzeba się do niego dostać. Ja raczej nie włączam SSH dla poszczególnych jaili jako, że w 90% potrzebuję konsoli do konfiguracji usługi, a potem już tam nie zaglądam. Zatem się po prostu do niego przenosimy będąc zalogowanym przez SSH do naszego FreeNASa:

.. code-block:: bash

        jls 
        jexec [nr jaila] tcsh 

Następnie aktualizujemy repozytoria pkg i instalujemy smokeping

.. code-block:: bash

        pkg update
        pkg install smokeping 


Główny plik konfiguracyjny znajdziemy tutaj:

.. code-block:: bash

        /usr/local/etc/smokeping/config

Najważniejsze sekcje to owner, contact, Alerts, secrets, Targets. Ta ostatnia sekcja może wyglądać np. tak

.. code-block:: bash
        
        *** General ***

        owner    = J.Doe
        contact  = jdoe@example.com
        mailhost = localhost
        sendmail = /usr/sbin/sendmail
        
        [...]
        
        *** Alerts ***
        to = jdoe@example.com
        from = jdoe@example.com
        
        [...]

        *** Targets ***

        + Local
        menu= Local
        title= Local hosts

        ++ Gateway

        menu = Gateway
        title = Gateway
        host = 192.168.0.1

        + Remote
        menu= Remote
        title= Remote hosts

        ++ Google-DNS

        menu = Google-DNS
        title= Google DNS
        host= 8.8.8.8

Po konfiguracji możemy włączyć smokeping, poprzez dodanie następującego wpisu do */etc/rc.conf*:

.. code-block:: bash

   smokeping_enable="YES"


Instalacja Apache
-----------------

Teraz pozostała nam tylko instalacja serwera Apache.

.. code-block:: bash

   pkg install apache24

I od razu możemy go włączyć w */etc/rc.conf*:

.. code-block:: bash

   apache24_enable="YES"


W moim przypadku apache nie będzie serwował nic poza plikami ze Smokepinga, więc katalog */usr/local/smokeping/htdocs* będzie moim DocumentRootem:

.. code-block:: bash

   <IfModule mpm_prefork_module>
           LoadModule cgi_module libexec/apache24/mod_cgi.so
   </IfModule>

   DocumentRoot "/usr/local/smokeping/htdocs"

   <Directory /usr/local/smokeping/htdocs>
            Require all granted
            AllowOverride none
            Options Indexes FollowSymLinks ExecCGI
            AddHandler cgi-script .cgi .fcgi
            DirectoryIndex index.html smokeping.fcgi
  </Directory>

Pozostaje tylko spradzić konfigurację:

.. code-block:: bash

   service apache24 configtest

I wystartowanie usług:

.. code-block:: bash

   service apache24 start
   service smokeping start


Jeśli wszystko poszło zgodnie z planem po 5-10 minutach powinniśmy pod adresem, który zdefiniowaliśmy dla naszego jaila zobaczyć pojawiające się wykresy. 

.. figure:: /images/Google-DNS_last_10800.png
        :alt: Smokeping wykres
        :align: center

