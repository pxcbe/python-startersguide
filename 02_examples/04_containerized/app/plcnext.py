import sys
sys.path.insert(0, "..")
import time
import logging

from opcua import Client
from opcua import ua


class SubHandler(object):

    """
    Client to subscription. It will receive events from server
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)


if __name__ == "__main__":
    #from IPython import embed
    #logging.basicConfig(level=logging.DEBUG)
    
    client = Client("opc.tcp://192.168.10.10:4840/")
    client.set_user('admin')
    client.set_password('ca895987')
    
    client.set_security_string("Basic256Sha256,SignAndEncrypt,opcua_client.der,opcua_client.pem")
    client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"

    i = 0

    try:

        client.connect()

        while i < 5 :
            
            ua_LevelMaximum = client.get_node("ns=5;s=Arp.Plc.Eclr/LevelMaximum")
            ua_LevelMinimum = client.get_node("ns=5;s=Arp.Plc.Eclr/LevelMinimum")
            ua_robot_test   = client.get_node("ns=5;s=Arp.Plc.Eclr/Robot.Test_Var")

            print(ua_LevelMaximum.get_value())
            print(ua_LevelMinimum.get_value())
            print(ua_robot_test.get_value())

            # make sure you are comparing the right datatypes!

            if int(ua_LevelMinimum.get_value()) == 300 :
                vLow = 500
                vHigh = 800
            else :
                vLow = 300
                vHigh = 500    

            # Definiton of variables, the OPC UA server doesn't 
            LevelMaximum = ua.DataValue(ua.Variant(vHigh,ua.VariantType.Int16))
            LevelMinimum = ua.DataValue(ua.Variant(vLow,ua.VariantType.Int16))

            LevelMaximum.ServerTimestamp = None
            LevelMaximum.SourceTimestamp = None

            LevelMinimum.ServerTimestamp = None
            LevelMinimum.SourceTimestamp = None


            ua_LevelMaximum.set_value(LevelMaximum)
            ua_LevelMinimum.set_value(LevelMinimum)

            #embed()
            time.sleep(3) 
            #client.close_session()

            i += 1

    finally:
        client.disconnect()