Automatyczny renice dla Aide - Debian
#####################################
:date: 2014-12-21 18:45
:category: Linux
:author: Hrv
:slug: automatyczne-renice-dla-Aide

Instalacja Aide w Debianie jak większość operacji na tym systemie przebiega bezproblemów. Developerzy paczek zadbali o pełny zestaw, więc instalując Aide przez apt dostajemy skrypty startowe do codziennego sprawdzania plików konfiguracyjnych. 

Skrypty te są dość skomplikowane jako, że nie tylko odpalają aplikację z odpowiednimi parametrami, ale również zajmują się stworzeniem odpowiednich logów itd. To trochę utrudniło moja zadanie dopasowania wartości nice dla właściwego procesu Aide. 

Poniżej najelpszy sposób rozwiązania tego problemu na który wpadem po kilku testach:

.. code-block:: bash

        #Added my renice hack
        (sleep 5; \
        renice 16 `ps ax | grep /usr/bin/aide | grep -v wrapper | grep -v grep | awk '{ print $1 }'`) &
         
        aide.wrapper $AIDEARGS "--$COMMAND" >|"$ARUNLOG" 2>|"$AERRLOG" && ARETVAL="$?"; 
    
Niestety właściwy proces nie jest tu wywoływany bezpośrednio, lecz za pomocą wrappera stąd wywołanie go przez np. *nice 18* nic by nam nie dało. 

Ostatecznie wpadłem na pomysł na wywołania renice w tle dla odpowiedniego procesu poprzedzonego 5 sekundowym timeoutem. Dirty but works ;) 
