import paho.mqtt.client as mqtt
import time

# Callback function when client is connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribe to a topic when connected
    client.subscribe("demo/one")

# Callback function when client receives a message
def on_message(client, userdata, msg):
    print("Received message: "+msg.payload.decode())

# Create a client instance
client = mqtt.Client()

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker (replace with your broker address and port)
client.connect("demo-0dklna.a01.euc1.aws.hivemq.cloud:8884/mqtt", 8884, 60)

# Start the MQTT loop
client.loop_start()

# Publish a message to a topic
client.publish("demo/one", "Hello, MQTT!")

# Keep the program running to receive messages
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    # Disconnect from the broker
    client.disconnect()
    # Stop the MQTT loop
    client.loop_stop()
