Monitorowanie logów za pomocą NodeRed
############################################
:date: 2016-01-19 21:31
:author: Hrv
:tags: node-red, mikrotik, DIY
:slug: monitoring-logow-node-red


Uwielbiam NodeRED_ za prostotę prototypowania i przejrzystosć. W domu używam NodeRed głównie do spinania różnych podzespołów mojego "mądrego domu". 

.. _NodeRed: http://nodered.org/

W pewnym momencie pojawiła się potrzeba zasilenia całej logiki domowej danymi z routera/access pointa. Jako, że MikroTik ma wsparcie rsysloga pomyślałem, że może będzie można to łatwo wykorzystać. Skoro router potrafi dane wysyłać to NodeRED powinien potrafić je odebrać. Skonfigurowałem logowanie na interesujące mnie tematy w MikroTiku tak żeby, je wysyłał na konkretny port i adres serwera gdzie zainstalowany jest NodeRed. Na tymże serwerze dodałem node udp nasłuchujący na porcie, który skonfigurowałem w MiroTiku i logi zaczęły płynąć szerokim strumieniem.

Do wpływających informacji można ewentualnie dodać timestamp:

.. code-block:: javascript 


        //Stupid timestamp building 
        var d = new Date();

        var y = d.getFullYear();
        var m = (d.getMonth()+1);
        var day = d.getDate();
        var h = d.getHours();
        var min = d.getMinutes(); 

        if (m < 10 ) {
            var m = "0"+m;
        }
        if (h < 10 ) {
            var h = "0"+h;
        }
        if (min < 10 ) {
            var min = "0"+min;
        }
        var loc = y+ "-" + m + "-"+ day + " "+ h+ ":"+min;
        msg.payload = loc +" - "+ msg.payload; 

        return msg; 

Oczywiście teraz sky is the limit, z w ten sposób przekazywanymi danymi można zrobić wszytko co tylko potrzebujecie. :) 

Oto początek flowu z functionblockiem z dwoma outputami, jeden do dalszych akcji, a drugi np do logowania do pliku:

.. code-block:: json

        [{"id":"ab00522d.85df08","type":"function","z":"5afe902f.a220a8","name":"ToString + logging","func":"log = {};\n\n//Stupid timestamp building \nvar d = new Date();\n\nvar y = d.getFullYear();\nvar m = (d.getMonth()+1);\nvar day = d.getDate();\nvar h = d.getHours();\nvar min = d.getMinutes(); \n\nif (m < 10 ) {\n    var m = \"0\"+m;\n}\nif (h < 10 ) {\n    var h = \"0\"+h;\n}\nif (min < 10 ) {\n    var min = \"0\"+min;\n}\nvar loc = y+ \"-\" + m + \"-\"+ day + \" \"+ h+ \":\"+min;\nlog.payload = loc +\" - \"+ msg.payload; \n\n\n\nreturn [msg, log];","outputs":"2","noerr":0,"x":311,"y":500,"wires":[["ac4887de.c98148"],["52376ca9.a9e6fc"]]},{"id":"fbe53849.90ec8","type":"udp in","z":"5afe902f.a220a8","name":"","iface":"","port":"6666","ipv":"udp4","multicast":"false","group":"","datatype":"utf8","x":94,"y":433,"wires":[["ab00522d.85df08"]]}]
