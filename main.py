# This is a sample Python script.
import mqttOperator
import deviceOperator

address = 'bemfa.com'
port = 9501
topic = "com002"
client_id = '*******'

mqttClinet = mqttOperator.MqttOperator(address, port, client_id, topic)
dev = deviceOperator.DeviceOpreator()
def processMsg(topic,message):
    if message.find('#') ==-1:
        if message=='off':
            dev.shut_down()
            return
    else:
        x = message.split('#',1)
        dev.set_volume(int(x[1]))
if __name__ == '__main__':
    mqttClinet.setMessageProcess(processMsg)
    mqttClinet.connect()


