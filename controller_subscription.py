# This script runs on the controller (e.g. Raspberry Pi, micro controllers)

import RPi.GPIO as GPIO
import time as t
from auto_move import TIME_IN_DOWN_POSITION
import paho.mqtt.subscribe as subscribe

TOPIC = "desk"
BROKER = "homeassistant"
PORT = 1883
QOS = 1

USERNAME = "<your-username>"
PASSWORD = "<your-password>"
auth = {"username": USERNAME, "password": PASSWORD}

# These times have to be adjusted to the actual time needed to raise/lower the desk to the desired position
TIME_LOWERING_DESK = 11  # seconds
TIME_RAISING_DESK = 11  # seconds

PIN_RELAY_1 = 21
PIN_RELAY_2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RELAY_1, GPIO.OUT)
GPIO.setup(PIN_RELAY_2, GPIO.OUT)

# The initial output values has to be changed depending on active low / active high relays
GPIO.output(PIN_RELAY_1, GPIO.LOW)
GPIO.output(PIN_RELAY_2, GPIO.LOW)


def lower_desk():
    GPIO.output(PIN_RELAY_1, GPIO.HIGH)
    t.sleep(11)
    GPIO.output(PIN_RELAY_1, GPIO.LOW)


def raise_desk():
    GPIO.output(PIN_RELAY_2, GPIO.HIGH)
    t.sleep(11)
    GPIO.output(PIN_RELAY_2, GPIO.LOW)


def callback(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("There was a message posted to " +
          msg.topic + " with the payload " + payload)

    if payload == "up":
        print("Raising desk")
        raise_desk()
    elif payload == "down":
        print("Lowering desk")
        lower_desk()


subscribe.callback(callback, TOPIC, hostname=BROKER,
                   port=PORT, auth=auth, qos=QOS)
