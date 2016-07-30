RSS na Blipie i Twitterze
#########################
:date: 2008-11-11 20:13
:author: Hrv
:tags: Blip,  Twitter, how-to
:slug: rss-na-blipie-i-twitterze

Idąc za ciosem, skoro `udostępniłem skrypt łączący profil z last.fm z
Blipem </blog/lastfm-na-twitterze-i-blipie.html>`_,
pomyślałem, że mógłbym napisać jeszcze jeden, bardziej uniwersalny,
który będzie czerpał informacje po prostu z kanału RSS. W ten sposób
możecie zautomatyzować promocję swoich treści, informować znajomych o
aktualizacjach na innych swoich blogach itp, możliwości są wręcz
nieograniczone.

Tak jak w poprzednim skrypcie, zmiany są monitorowane w odstępach
pięciominutowych, jeśli nastąpi jakaś aktualizacja kanału RSS generuje
on wiadomość o następującej składni :

.. code ::

    Nazwa Kanału  Tytuł wiadomości - link do wiadomości

A następnie wysyła na nasze konto Twittera lub/i Blipa.

W tej wersji skrypt po prostu działa, w kolejnych wersjach będę dodawał
funkcjonalności wg Waszego, swojego uznania.

.. code-block:: ruby

    #!/usr/bin/env ruby
    #By Harv - http://harv.pl
    # based on a script by  Nicholas Pike - npike@npike.net

    require 'rss/1.0'
    require 'rss/2.0'
    require 'open-uri'

    # Dane dla Blipa
    BL_USER = ''
    BL_PASS = ''
    # Dane dla Twittera
    TW_USER = ''
    TW_PASS = ''

    #Zrodlo RSS
    source = "" 

    BL_URL  = 'http://api.blip.pl/updates'

    content = ""
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
          #puts $!

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

    open(source) do |s| content = s.read end
    rss = RSS::Parser.parse(content, false)

    if ( rss.items[0].link != last_url)
       puts "No match"

       last_url = rss.items[0].link
       short_url = Net::HTTP.get_response(URI.parse('http://is.gd/api.php?longurl='+last_url)).body
        
        message = rss.channel.title," ",rss.items[0].title," - #{short_url}"

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

