#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time
import socket

#set up pins
def gpioSetup():
    #set pin numbering
    gpio.setmode(gpio.BCM)
    #Set output pin
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)


#only exe if connect sucessfull

def connectionStatus(client, userdata, flags, rc):
    mqttClient.subscribe("rpi/gpio")

def messageDecoder(client, userdata, msg):
    message = msg.payload.decode(encoding='UTF-8')

# decode what is being sent:

#door 1/4

    if message == "op 23":
        gpio.output(23, gpio.LOW)
        time.sleep(.2)
        gpio.output(23, gpio.HIGH)
        print("door #1 is opened/closed")

            
# door 2/4
    elif message == "op 24":
        gpio.output(24, gpio.LOW)
        time.sleep(.2)
        gpio.output(24, gpio.HIGH)
        print("door #2 is opened/closed")


# door 3/4            

    elif message == "op 27":
        gpio.output(27, gpio.LOW)
        time.sleep(.2)
        gpio.output(27, gpio.HIGH)
        print("door #3 is opened/closed")
    
    # door 4/4            

    elif message == "op 22":
        gpio.output(22, gpio.LOW)
        time.sleep(.2)
        gpio.output(22, gpio.HIGH)
        print("door #4 is opened/closed")

            

    else:
            print("Major Error!!!")


    
#set up RPI GPIO pins
gpioSetup()

#client name
clientName = "RPI3B"

#set mqtt sever addr
#serverAddress = "10.0.0.50"

#automatically get IP of device (not my code)
#source: https://stackoverflow.com/questions/166506
#/finding-local-ip-addresses-using-pythons-stdlib

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
serverAddress = (s.getsockname()[0])
s.close()



#Instantiateeclipse paho as mqttclient
mqttClient = mqtt.Client(clientName)

#calling functions
mqttClient.on_connect = connectionStatus
mqttClient.on_message = messageDecoder


#connect client to server
mqttClient.connect(serverAddress)

#monitor forever
mqttClient.loop_forever()
