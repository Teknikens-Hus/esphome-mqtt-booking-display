# esphome-mqtt-booking-display
This is a project linked to [calendar-to-mqtt](https://github.com/Teknikens-Hus/calendar-to-mqtt) that takes the events published and displays them on a screen

## To install/setup/update:
- Make sure you've installed Python and [ESPHome CLI](https://esphome.io/guides/installing_esphome)
- Run the main.py file using Python.

The main.py file will:
 - Help you install new ESP32 devices
 - OTA update existing devices
 - Create or modify the configuration file needed for installing/updating the devices
 - List COM ports to help you find the correct ESP32 device connected to your computer 

## Configuration file
The project requires a config.json file that contains an array of devices. An example config looks like this:
```json
{
    "devices": [
        {
            "name": "room-name-in-lowercase",
            "eventsTopic": "calendar-to-mqtt/calendar-name/today/upcoming/events",
            "type": "small-oled-display.yaml"
        },
        {
            "name": "room-name-in-lowercase-2",
            "eventsTopic": "calendar-to-mqtt/calendar-name-2/today/upcoming/events",
            "type": "e-paper-display.yaml"
        }
    ]
}
```
The python program helps you create this interactively if you prefer, so you dont have to write it yourself.


## ESPHome version
This project is built using ESPHome version 2024.10.2

## Substitutions
This project uses substitutions to make it easier to install the same code on multiple devices. The following substitutions are used:
- name: The name of the device, this will show in the top left corner of the display and used in the mDNS name "name-display.local"
- eventsTopic: The topic that the events are published on


## Running manually
To run it manually without the python program, you can use the following command:
```bash
esphome -s name your-name-in-lowercase -s eventsTopic calendar-to-mqtt/calendar-name/today/upcoming/events run ESPHOME/e-paper-display.yaml
```
or for the small OLED display:
```bash
esphome -s name your-name-in-lowercase -s eventsTopic calendar-to-mqtt/calendar-name/today/upcoming/events run ESPHOME/small-oled-display.yaml
```
