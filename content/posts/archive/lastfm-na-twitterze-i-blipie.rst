Last.fm na Twitterze i Blipie
#############################
:date: 2008-11-10 16:03
:author: Hrv
:tags: Blip, Last.fm, Twitter,how-to
:slug: lastfm-na-twitterze-i-blipie

Pozwoliłem sobie zmodyfikować skrypt w Ruby autorstwa `Nicholasa
Pike <http://blog.npike.net/2008/03/26/twitter-lastfm-a-quick-ruby-script/>`_,
wyświetlający nasze ulubione piosenki z `last.fm <http://last.fm>`_ na
`Twiterze <http://twitter.com>`_, dodając mu także obsługę naszego
rodzimego `Blipa <http://blip.pl>`_. Skrypt sprawdza co 5 min czy nie
zaznaczyliśmy nowej piosenki jako '**lubię**\ ', jeśli odnajdzie taką
zmianę zaktualizuje nasz status na obu mikroblogach.

Jeśli chcemy korzystać tylko z jednego z systemów wystarczy
pozostawić puste pola nazwy użytkownika i hasło dla danego konta , a
skrypt nie będzie próbował aktualizować danego mikrobloga.

.. code-block:: ruby

    #!/usr/bin/env ruby
    # @author:  Nicholas Pike - npike@npike.net
    #blip-mod: Harv - http://harv.pl 

    require 'net/http'
    require 'rexml/document'

    # Dane dla Twittera
    TW_USER = ''
    TW_PASS = ''
    # Dane dla Blipa
    BL_USER = ''
    BL_PASS = ''

    # Nazwa użytkownika w Last.fm
    LF_USER = ""

    # DO NOT CHANGE BELOW THIS
    TW_URL  = 'http://twitter.com/statuses/update.xml'
    BL_URL  = 'http://api.blip.pl/updates'
    LAST_FM_URL = "http://ws.audioscrobbler.com/1.0/user/#{LF_USER}/recentlovedtracks.xml"

    # temp variables
    last_url = ""
    first_run = 1

    def postToTwitter(message)
      begin
        url = URI.parse(TW_URL)
        req = Net::HTTP::Post.new(url.path)
        req.basic_auth TW_USER, TW_PASS
        req.set_form_data({'status' => message})
        begin
          res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }
          case res
            when Net::HTTPSuccess, Net::HTTPRedirection
              if res.body.empty?
                puts "Twitter nie odpowiada"

              else
                puts 'Twitter zaktualizowany'

              end
            else
              puts 'Aktualizacja sie nie powiodla'
              # res.error!

            end
        rescue
          puts $!

        end
      rescue SocketError
        puts "Twitter jest niedostepny"

      end
    end

    def postToBlip(message)
      begin
        url = URI.parse(BL_URL)
        req = Net::HTTP::Post.new(url.path)
        req.basic_auth BL_USER, BL_PASS
        req.set_form_data({'body' => message})
        begin
          res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }
          case res
            when Net::HTTPSuccess, Net::HTTPRedirection
              if res.body.empty?
                puts "Blip nie odpowiada"

              else
                puts 'Blip zaktualizowany'

              end
            else
              puts 'Aktualizacja sie nie powiodla'
              # res.error!

            end
        rescue
          #puts $!
         

        end
      rescue SocketError
        puts "Blip jest niedostepny"

      end
    end

    while true

    # get the XML data as a string
    xml_data = Net::HTTP.get_response(URI.parse(LAST_FM_URL)).body
    doc = REXML::Document.new(xml_data)

    if ( doc.elements["recentlovedtracks/track[1]/url"].text != last_url)
       puts "No match"

       last_url = doc.elements["recentlovedtracks/track[1]/url"].text
       last_artist = doc.elements["recentlovedtracks/track[1]/artist"].text
       last_name = doc.elements["recentlovedtracks/track[1]/name"].text 

       short_url = Net::HTTP.get_response(URI.parse('http://is.gd/api.php?longurl='+last_url)).body
     
       message = "Last.FM: #{last_name} - #{last_artist} \n\n#{short_url}"

      # Dont send a twitter message on first run of script
       if (first_run != 1)
          if (TW_USER != '')
            postToTwitter(message)
           end
          if (BL_USER != '')
            postToBlip(message)
          end
       end
       first_run = 0
    else
      puts "Brak zmian"
    end
    sleep 200
    end

Czekam na komentarze, jeśli będzie zapotrzebowanie mogę w wolnej chwili
przepisać to do php.
