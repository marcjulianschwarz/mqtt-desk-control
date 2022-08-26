# MQTT Desk Control

These scripts allow you to control a desk with [MQTT](https://mqtt.org) an efficient bi-directional messaging protocol for IoT devices.

## Get started

Install the [Python MQTT](https://pypi.org/project/paho-mqtt/) package like this:

```
pip install paho-mqtt
```

The files `move_down.py` and `move_up.py` show the simplest way to move the desk. Use the `auto_move.py` file to automatically raise and lower the table for specified time intervals.

The script `controller_subscription.py` has to be run on the controller which is connected to the desk buttons via a relay. Make sure to have the [Python MQTT](https://pypi.org/project/paho-mqtt/) package installed before running the script.

### Raycast Scripts

The folder `raycast_scripts` contains two scripts that can be used as [Script Commands](https://www.raycast.com/blog/getting-started-with-script-commands) in [Raycast](https://www.raycast.com).
