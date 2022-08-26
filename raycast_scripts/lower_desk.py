#!/path/to/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Lower Desk
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ⬇️
# @raycast.packageName Desk

# Documentation:
# @raycast.description Lowers the desk.
# @raycast.author Marc Julian Schwarz
# @raycast.authorURL https://www.github.com/marcjulianschwarz

import paho.mqtt.publish as publish

publish.single("desk", "down", hostname="homeassistant",
               auth={"username": "<your-username>", "password": "<your-password>"})

print("Lowering the desk...")
