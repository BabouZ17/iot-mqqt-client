#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MQTT Simple Client connection to a topic

import paho.mqtt.client as mqtt

def on_connect(client, user_data, flags, rc):
	print("Connected with result code : {}".format(str(rc)))

	# subscribe to the top $SYS
	client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from server
def on_message(client, user_data, msg):
	print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

client.loop_forever()