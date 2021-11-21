import paho.mqtt.client as mqtt

class MqttOperator:
    def __init__(self,address,port,client_id,topic):
        self.address = address
        self.port = port
        self.topic = topic
        self.client_id = client_id

        self.client = mqtt.Client(self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

    def on_connect(self,client,userdata,flags,rc):
        print("Connected with result code " + str(rc))
        client.subscribe("data/receive")
    def on_message(self,client, userdata, msg):
        print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))
        self.fn(msg.topic,str(msg.payload.decode('utf-8')))

    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("On Subscribed: qos = %d" % granted_qos)

    def on_disconnect(self,client, userdata, rc):
        if rc != 0: print("Unexpected disconnection %s" % rc)

    def connect(self):
        self.client.connect(self.address,self.port)
        self.client.subscribe(self.topic, 0)
        self.client.loop_forever()
    def setMessageProcess(self,fn):
        self.fn = fn
if __name__ == '__main__':
    address = 'bemfa.com'
    port = 9501
    topic = "com002"
    client_id = '*******'
    mqtt = MqttOperator(address,port,client_id,topic)
    mqtt.connect()
