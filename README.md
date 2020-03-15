# TCPOptionsDataExfil
Experimental scripts using Python 3.x and Scapy to transmit data to closed (or open) ports between hosts using only TCP Options

## README/USAGE:
Ensure you have Python 3.x installed and Scapy. This was tested on different Windows 10 x64 hosts running the 64 bit versions of Python and default scapy pip installations as of March 2020. Scapy should be the only real dependency as the other imports are part of a core installation. These scripts are INTERACTIVE and so you run them as a standard python <filename.py> script and follow the prompts. Remember, in windows if you set a valid path for a dump file you have to use 'double' backslashes to escape the meta character python natively interprets. An open TCP port is not needed, though it is best to have one open to reduce the number TCP resets being sent from your listening host. Administrative rights are not needed as the script will natively tell Scapy to use random > 1024 source port numbers upon each 'data exfil' message iteration being sent.

## TCP Options and RFC7413 (TCP Fast Open)
This was really a fun experiment for myself to see how different network cards, drivers, and OS's respond to TCP Options on varying reserved, experimental, or uncommon settings. What does not seem to immediately trigger any native Windows 10.x stack rejections and sometimes a NIDS depending on what kind of pre-processor rules you have enabled. Best of all, if you're transmitting data in terms of 'options' whether you decide to encode it or not-- that a destination 'port' need not be open (again, at least on Windows 10 at the time of this testing). This does trigger a signficant amount of TCP resets which may create warning IOC's. 

*This software provides no expressed warranty or liability for use and is licensed under GPLv2
Dennis Chow dchow[AT]xtecsystems.com
www.scissecurity.com*

![example1]
(https://github.com/dc401/TCPOptionsDataExfil/raw/master/TCPOptions%20Data%20Exfil%20Usage%201.png)

![example2]
(https://github.com/dc401/TCPOptionsDataExfil/raw/master/TCPOptions%20Data%20Exfil%20Example%20Dump%20Log%20and%20Runtime.PNG)
