import paho.mqtt.publish as publish
import time as t

TOPIC = "desk"
BROKER = "homeassistant"
USERNAME = "<your-username>"
PASSWORD = "<your-password>"
auth = {"username": USERNAME, "password": PASSWORD}

TIME_IN_DOWN_POSITION = 15*60  # seconds
TIME_IN_UP_POSITION = 5*60  # seconds


def move_desk(position):
    print("Moving desk {}...".format(position))

    # Publishing a message to the topic "desk" which is being subscribed to by the controller (see controller_subscription.py)
    publish.single(
        TOPIC,
        position,
        hostname=BROKER,
        auth=auth,
    )


while True:
    t.sleep(TIME_IN_DOWN_POSITION)
    move_desk("up")
    t.sleep(TIME_IN_UP_POSITION)
    move_desk("down")
