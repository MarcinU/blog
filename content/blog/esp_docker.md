Title: Bajecznie prosta kompilacja NodeMCU
Date: 2016-01-13 20:31
Author: Hrv
Tags: docker, nodeMCU, esp8266
Slug: kompilacja-nodemcu


Docker sprawił, że praktycznie wszystko może być bajczenie proste, przeglądając dokumentację nodeMCU przez przypadek wpadłem na to [repozytorium](https://hub.docker.com/r/marcelstoer/nodemcu-build/).

Kontener ten zawiera komplente środowisko do kompilacji nodemcu.

Nam pozostaje pobranie źródeł, wybranie modułów, które mają być wkompilowane:

```c
vi app/include/user_modules.h

#ifdef LUA_USE_MODULES
#define LUA_USE_MODULES_NODE
#define LUA_USE_MODULES_FILE
#define LUA_USE_MODULES_GPIO
#define LUA_USE_MODULES_WIFI
#define LUA_USE_MODULES_NET
#define LUA_USE_MODULES_PWM
#define LUA_USE_MODULES_I2C
#define LUA_USE_MODULES_SPI
#define LUA_USE_MODULES_TMR
#define LUA_USE_MODULES_ADC
#define LUA_USE_MODULES_UART
#define LUA_USE_MODULES_OW
#define LUA_USE_MODULES_BIT
#define LUA_USE_MODULES_MQTT
// #define LUA_USE_MODULES_COAP
// #define LUA_USE_MODULES_U8G
// #define LUA_USE_MODULES_WS2801
// #define LUA_USE_MODULES_WS2812
// #define LUA_USE_MODULES_CJSON
#define LUA_USE_MODULES_CRYPTO
#define LUA_USE_MODULES_RC
#define LUA_USE_MODULES_DHT
#define LUA_USE_MODULES_RTCMEM
#define LUA_USE_MODULES_RTCTIME
#define LUA_USE_MODULES_RTCFIFO
#define LUA_USE_MODULES_SNTP
// #define LUA_USE_MODULES_BMP085
#define LUA_USE_MODULES_TSL2561
// #define LUA_USE_MODULES_HX711

#endif /* LUA_USE_MODULES */
```

A następnie wydanie jednej komendy:

```bash
docker run --rm -ti -v `pwd`:/opt/nodemcu-firmware marcelstoer/nodemcu-build
```
Ostatecznie pozostaje tylko flashowanie nowego firmware'u:

```bash
./esptool.py --port /dev/tty.usbserial-AI02N250 write_flash 0x00000 nodemcu.bin
```

Od czasu do czasu warto zupdatować obraz kontenera, który przy pierwszym uruchomieniu pobraliśmy:

```bash
docker pull marcelstoer/nodemcu-build
```
