Last.fm na Twitterze i Blipie w PHP
###################################
:date: 2008-11-23 10:04
:author: Hrv
:tags: Blip, Last.fm, Twitter
:slug: lastfm-na-twitterze-i-blipie-w-php

Jakiś czas temu opublikowałem `swoją wersję
skryptu </blog/lastfm-na-twitterze-i-blipie.html>`_
wyświetlającego nasze ulubione utwory z `Last.fm <http://last.fm>`_ na
`Blipie <http://blip.pl>`_ i `Twitterze <http://www.twitter.com>`_. 
Jako, że pojawiło się zapotrzebowanie na wersję w PHP, postanowiłem go
szybko przepisać.

Nie jest to 100% odpowiednik wersji Ruby, ale chyba będzie spełniał
swoje zadanie. Skrypt używa pliku tymczasowego do przechowywania
ostatnich danych z Last.fm, aby uniknąć nieskończonej pętli i wysyłania
jednego statusu w kółko. Dlatego też należy nadać odpowiednie prawa
katalogowi w którym ten plik będzie tworzony, jego ścieżkę możecie
określić zmienną w 'części konfiguracyjnej' skryptu. Jako parsera XML
użyłem gotowej klasy z
`php.net <http://pl2.php.net/manual/en/function.xml-parse.php#83416>`_,
także nie zapomnijcie wypakować `wszystkich plików z
paczki </uploads/last2blip.zip>`_
do katalogu w którym będzie działał skrypt.

Pamiętajcie żeby przed każdym odpaleniem usunąć plik tymczasowy, na tej
podstawie skrypt orientuje się czy jest odpalony po raz pierwszy, czy
nie. Chyba, że chcecie żeby przy pierwszym przebiegu już zaktualizował
microblogi.

.. code-block:: php5

    <?php
    /*
    Last.fm 2 Twitter and Blip Script 
    by Harv - http://harv.pl
          v.0.1
    */
    include_once "xx_xml.php";

    #Dane dla blipa
    $bl_user = '';
    $bl_pass = '';
    #Dane dla Twittera
    $tw_user = '';
    $tw_pass = '';
    #User Last.fm
    $lfm_user = '';
    #Sciezka pliku tmp
    $tmp_fn = "lsfm_tw";

    #Adresy API etc
    $lfm_url = 'http://ws.audioscrobbler.com/1.0/user/'.$lfm_user.'/recentlovedtracks.xml';
    $tw_url  = 'http://twitter.com/statuses/update.xml';
    $bl_url  = 'http://api.blip.pl/updates';

    function postTwitter($message) {
    global $tw_user, $tw_pass, $tw_url ;
        
       $curl_handle = curl_init();
        curl_setopt($curl_handle,CURLOPT_URL,"$tw_url");
        curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);
        curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);
        curl_setopt($curl_handle,CURLOPT_POST,1);
        curl_setopt($curl_handle,CURLOPT_POSTFIELDS,"status=$message");
        curl_setopt($curl_handle,CURLOPT_USERPWD, "$tw_user:$tw_pass");
        $buffer = curl_exec($curl_handle);
        curl_close($curl_handle);
        // check for success or failure
        if ($buffer) {
            echo 'Twitter success';
        } else {
            echo $buffer;
        }

    }

    function postBlip($message) {
    global $bl_user, $bl_pass, $bl_url;

        $curl_handle = curl_init();
        curl_setopt($curl_handle,CURLOPT_URL,"$bl_url");
        curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);
        curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);
        curl_setopt($curl_handle,CURLOPT_POST,1);
        curl_setopt($curl_handle,CURLOPT_POSTFIELDS,"body=$message");
        curl_setopt($curl_handle,CURLOPT_USERPWD, "$bl_user:$bl_pass");
        $buffer = curl_exec($curl_handle);
        curl_close($curl_handle);
        // check for success or failure
        if ($buffer) {
            echo 'Blip success';
        } else {
            echo $buffer;
        }

    }

    #Czyta XML
    $raw = new xx_xml($lfm_url ,'url');

    $last_url = $raw->data ['recentlovedtracks|track|url']['data'][0] ;
    $last_artist = $raw->data ['recentlovedtracks|track|artist']['data'][0] ;
    $last_track = $raw->data ['recentlovedtracks|track|name']['data'][0] ;
    $lat_date = $raw->data ['recentlovedtracks|track|date']['data'][0] ;

    #Skroc URL
    $sh_url = 'http://is.gd/api.php?longurl='.$last_url;
    $short_url = file_get_contents($sh_url);

    #Wiadomosc
    $message = 'Last.fm: '.$last_artist.' - '.$last_track.' '.$short_url ;

    #Pierwszy raz ? 
    if(file_exists($tmp_fn)) {

      $fh = fopen($tmp_fn, 'r') or die("Can't open file");
      $tmp_data = fread($fh, filesize($tmp_fn));
      fclose($fh);
     
      if($tmp_data != $last_url) {
     
        if(!empty($tw_user))
          postTwitter($message);
        sleep(2);
        if(!empty($bl_user))
          postBlip($message);
      
         
        $fh = fopen($tmp_fn, 'w+') or die("Can't open file");
        fwrite($fh, $last_url);
        fclose($fh);
      }
      else 
        echo 'Bez zmian';
      }
      #Pliku nie ma, pierwsze odpalenie
      else {
        $fh = fopen($tmp_fn, 'w+') or die("Can't open file");
        fwrite($fh, $last_url);
        fclose($fh);
        echo 'First Run';



      }

    ?>



Skrypt  ten, w przeciwieństwie do tego napisanego w Ruby, oczywiście nie
rezyduje w pamięci monitorując stale zmiany na Last.fm i potrzebuje
pomocy np. crona, aby aktualizować dane na bieżąco.  Przykładowy zapis
crontab uruchamiający skrypt co 2 minuty:

.. code-block:: bash

    */2 *  * * *   root   php [lokalizacja skryptu]

W razie jakichkolwiek problemów postaram się pomóc, potestujcie i
wytknijcie błędy, które z pewnością popełniłem.

`Pobierz paczkę ze skryptem </uploads/last2blip.zip>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

