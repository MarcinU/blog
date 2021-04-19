Title: Monitorowanie zużycia gazu
Date: 2016-10-29 20:10
Author: Hrv
Tags: DIY, domoticz, node-red, raspberry
Slug: monitorowanie-zuzycia-gazu

Pewnie mógłbym przytoczyć dziesiątki pragmatycznych powodów dla których można chcieć monitorować zużycie gazu w domu. Smutna prawda jest taka, że zrobiłem to, bo tak. Dla zabawy. Cała reszta to tylko wartość dodana. Odziedziczyłem dość stary gazomierz, ale jak się okazało bardzo wdzięczny w opomiarowaniu:

![Gasmeter - zdjęcie]({filename}/images/Gasmeter-photo.jpg)

Pomysły jak zliczać impulsy miałem dwa:

- optyczny - odbite światło z "błyszczącej" 6tki
- magnetyczny - magnes umieszczony pomiędzy 9 a 0

Wybrałem metodę najprostszą - magnetyczną. 

## Co potrzebujemy?

Hardware:

- kontaktron np.: [taki ze wszystkim co potrzebujemy](https://botland.com.pl/czujniki-magnetyczne/3104-czujnik-magnetyczny-otwarcia-drzwiokien-kontaktron-cmd14-srubki.html)
- raspberry pi

Software:

- node red - logika
- Domoticz - interface 


## Jak to jest zbudowane?

Sposób implementacji jest banalnie prosty. Kontaktron w momencie kiedy licznik przeskakuje z 9 na 0 zostaje zwarty. To przesyła stan wysoki do Raspberry Pi. Ten impuls przechwytuje NodeRed. Inkrementuje licznik, zapisuje bieżący stan na dysku oraz wysyła nowy odczyt za pomocą MQTT do Domoticza. 

Sposób podłączenia do Raspberry PI:

![Podłączenie]({filename}/images/Gasmeter-RPI-podlaczenie.png)

Rezystor jaki potrzebujemy to np.: 10kOhm.

Oto jak wygląda workflow w Node-Red:

![Nodered-Gasmeter]({filename}/images/NodeRed-Gasmeter.png)


Eksport tego flowu:
 
``` node-red
[{"id":"40eb2f32.7f7ad8","type":"debug","z":"359a63ea.f3b344","name":"","active":false,"console":"false","complete":"true","x":669.0000305175781,"y":829,"wires":[]},{"id":"168d419c.57d44e","type":"rpi-gpio in","z":"359a63ea.f3b344","name":"Gaz_meter","pin":"31","intype":"tri","debounce":"","read":false,"x":100.00003051757812,"y":890,"wires":[["126afed6.25f841"]]},{"id":"557fb10.d5b195","type":"file","z":"359a63ea.f3b344","name":"","filename":"/mnt/logs/gasmeter","appendNewline":true,"createDir":false,"overwriteFile":"false","x":670.0000610351562,"y":1012,"wires":[]},{"id":"126afed6.25f841","type":"rbe","z":"359a63ea.f3b344","name":"","func":"rbe","gap":"","x":240.00003051757812,"y":891,"wires":[["b36499a5.bad9f"]]},{"id":"b36499a5.bad9f","type":"function","z":"359a63ea.f3b344","name":"Gas_meter_parse","func":"node.status({fill:\"yellow\",shape:\"dot\",text: context.global.gasmeter.toString() });\n\nif ( context.global.gasmeter > 0 && msg.payload == \"1\") {\n    \n    context.global.gasmeter = context.global.gasmeter + 1; \n    msg.payload = context.global.gasmeter;\n\n    msg_out = {};\n    \n    msg_out.payload = {};\n    msg_out.payload.idx = 37;\n    msg_out.payload.svalue = \"\" + msg.payload;\n    return [msg, msg_out];\n    \n}\n\n","outputs":"2","noerr":0,"x":411.0000305175781,"y":887,"wires":[["557fb10.d5b195","40eb2f32.7f7ad8"],["40eb2f32.7f7ad8","c7a112e9.b7ee88"]]},{"id":"c7a112e9.b7ee88","type":"mqtt out","z":"359a63ea.f3b344","name":"","topic":"domoticz/in","qos":"","retain":"","broker":"99849ffa.4c579","x":699.0000305175781,"y":927,"wires":[]},{"id":"99849ffa.4c579","type":"mqtt-broker","z":"","broker":"mqtt.lan","port":"1883","clientid":"NodeRed-domoticz","usetls":false,"verifyservercert":true,"compatmode":true,"keepalive":"30","cleansession":true,"willTopic":"","willQos":"0","willRetain":null,"willPayload":"","birthTopic":"","birthQos":"0","birthRetain":null,"birthPayload":""}]
```

I w zasadzie koniec magii. Oczywiście dokładność nie jest idealna. Czasami bywa, że zgubi jakiś impuls, albo pięć. Jednak, jak na rozwiązanie za 7 zł myślę, że działa nadzwyczaj dobrze. 

![Gasmeter pomiar]({filename}/images/Gasmeter-chart.png)
