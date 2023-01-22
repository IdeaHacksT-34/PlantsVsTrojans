# Plants vs Trojans - IdeaHacks 2023

## Inspiration
A Bruin-spirited twist on the popular franchise Plants vs. Zombies, Plants vs. Trojans seeks to help anyone who has trouble keeping their plant friends alive by gamifying the processing of plant care.

## What it does
Plants vs. Trojans helps users take care of their plants by rewarding them through a game we made that is integrated with our sensors. Points from good plant care such as providing adequate water and sunlight allows users to unlock new, playable characters!

## How we built it
We built this by making the circuit with a soil moisture sensor and UV light sensor that monitor the plant's environment. We then connected a Wi-Fi module that sent the data to a web server that we developed. This data from the web server is then used by our game to determine points.

## Challenges we ran into
Setting up a web server, communicating that data over Wi-Fi, and integrating all of our parts together proved to be great challenges.

## Accomplishments that we're proud of
We're especially proud of the seamless integration of electronics and software that make our product possible and the fun pixel art style that is layered throughout the game.

## What we learned
We learned that integrating many independent parts together takes a lot of time and documentation reading. This can be done more efficiently by creating and assigning tasks together beforehand.

## What's next for Plants vs. Trojans
We already have a couple of ideas to make the game more engaging and helpful by adding power-ups that are exchangeable by points and plant care tips based on the environment data from our sensors.

# Getting Started

## Hardware
* ESP32
* Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor
* Adafruit VEML6070 UV Index Sensor

## Dependencies
* Python 3.10
* pygame 2.1.2
* selenium 4.7.2

# Author
* [@Philip Do](https://github.com/philipdoucla)
* [@Jun Sang Lee](https://github.com/junlee9320)
* [@Vinh Nguyen](https://github.com/DangDingDongDog)
* [@Harshin Shah](https://github.com/HersheysCB)
* [@Dhaval Vora](https://github.com/dhavalvoraa)
