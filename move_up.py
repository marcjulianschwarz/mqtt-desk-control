import paho.mqtt.publish as publish

# Publishing a message to the topic "desk" which is being subscribed to by the controller (see controller_subscription.py)
publish.single("desk", "up", hostname="homeassistant",
               auth={"username": "<your-username>", "password": "<your-password>"})
