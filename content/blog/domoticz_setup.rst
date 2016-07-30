Raspbian + Domoticz + MQTT = Home Automation
############################################
:date: 2015-12-18 18:20
:author: Hrv
:tags: DIY, domoticz, raspberry, mqtt
:slug: raspbian-domoticz-nodered-mqtt

Odkąd przeprowadziłem się do nowego mieszkania, zabawiam się w monitoring i "home automation". Sercem całego systemu jest oczywiście nic innego jak Raspberry Pi. 

Poniżej zestaw softu, który napędza to wszytko: 

- Raspbian Minimal,
- Domoticz_ - głównie jako interface,
- NodeRED_ - interface pomiędzy różnymi podzespołami, 
- Mosquitto_ <3 MQTT - transport :) , 
- Biblioteka Adafruit-DHT_, 
- Biblioteka BMC2835_ - głównie do kompilacji powyższej biblioteki,
- plus trochę skryptów w bashu, pythonie i lua w przypadku nodów esp8266, ale o tym przy innej okazji. 

.. _Domoticz: https://domoticz.com/
.. _NodeRed: http://nodered.org/docs/
.. _Mosquitto: http://mosquitto.org/
.. _Adafruit-DHT: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
.. _BMC2835: http://www.airspayce.com/mikem/bcm2835/

Dlaczego Domoticz, a nie openHAB_? OpenHAB na pewno jest najbardziej popularnym OpenSource-owym rozwiązaniem tego typu, z wyjątkowo brzydkim i nieintuicyjnym (moim zdaniem) interfacem. 
Domoticz o wiele bardziej przypadł mi do gustu. Spore znczenie pewnie ma fakt, że poszukiwałem tylko ładnego interface z aplikcją mobilną i zapisywaniem danych historycznych na wykresach.

.. _openHAB: http://www.openhab.org/features/introduction.html


