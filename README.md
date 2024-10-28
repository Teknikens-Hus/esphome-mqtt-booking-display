# esphome-mqtt-booking-display
This is a project linked to [calendar-to-mqtt](https://github.com/Teknikens-Hus/calendar-to-mqtt) that takes the events published and displays them on a screen

# Substitutions
This project uses substitutions to make it easier to install the same code on multiple devices. The following substitutions are used:
- name: The name of the device, this will show in the top left corner of the display and used in the mDNS name "name-display.local"
- eventsTopic: The topic that the events are published on

## To install run:
Cd into the ESPHome directory and run:
For the small oled display:
```bash
esphome -s name your-room-name -s eventsTopic calendar-to-mqtt/your-calendar-name/today/upcoming/events run small-oled-display.yaml
```
For the 7.5 inch e-paper display:
```bash
esphome -s name your-room-name -s eventsTopic calendar-to-mqtt/your-calendar-name/today/upcoming/events run e-paper-display.yaml
```