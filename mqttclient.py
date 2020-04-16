
import paho.mqtt.client as mqtt #import the client1
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import json
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
broker_address="51.136.13.51" 

def on_message(client, userdata, message):
    print("m: ", message)
    print("message received " ,(str(message.payload.decode("utf-8"))))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    handle_message(message)

def handle_message(message):
    if "sensors/mohammed/sensor1" in message.topic :
	print("sensor1")
        if json.loads(message.payload)["value"]:
            print("LED1 TURN ON")
            GPIO.output(8, GPIO.HIGH) # Turn on
        else:
            GPIO.output(8, GPIO.LOW) # Turn off 
    elif "sensors/mohammed/sensor2" in message.topic :
        print("sensor2") 
        if json.loads(message.payload)["value"]:
            print("LED2 TURN ON")
            GPIO.output(10, GPIO.HIGH) # Turn on
        else:
            GPIO.output(10, GPIO.LOW) # Turn off

client = mqtt.Client(client_id="P1") #create new instance
client.connect(broker_address) #connect to broker
client.on_message=on_message
client.subscribe("sensors/mohammed/#")
client.loop_start()    #start the loop
time.sleep(400)
 
