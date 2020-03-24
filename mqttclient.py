import paho.mqtt.client as mqtt #import the client1
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
broker_address="52.157.91.193" 

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#def handle_message(message):
 #   if message:
  #       GPIO.output(8, GPIO.HIGH) # Turn off
   # else
    #     GPIO.output(8, GPIO.LOW) # Turn off

client = mqtt.Client(client_id="P1") #create new instance
client.connect(broker_address) #connect to broker
client.on_message=on_message
client.publish("test","kevin from docker")#publish
print("Subscribing to topic","test")
client.subscribe("test")
client.loop_start()    #start the loop
time.sleep(400)