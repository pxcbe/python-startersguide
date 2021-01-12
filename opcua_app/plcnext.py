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
    
    #client = Client("opc.tcp://olivier:olivierpass@localhost:53530/OPCUclearA/SimulationServer/")
    client.set_security_string("Basic256Sha256,SignAndEncrypt,opcua_client.der,opcua_client.pem")
    client.application_uri = "urn:example.org:FreeOpcUa:python-opcua"

    try:
        client.connect()
        root = client.get_root_node()
        print("Root is", root)
        print("childs of root are: ", root.get_children())
        print("name of root is", root.get_browse_name())
        objects = client.get_objects_node()
        print("childs og objects are: ", objects.get_children())
        

        #embed()
        time.sleep(3)
        #client.close_session()
    finally:
        client.disconnect()