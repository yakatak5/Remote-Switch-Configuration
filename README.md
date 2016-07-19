# Remote-Switch-Configuration
This can be saved as a header file for easy SSH access and configuration to a switch

Must have Paramiko library installed

Usage: <object name> = device(<ip address>, <username>, <password>)
Login to check credentials: <object name>.login()
To configure ospf: <object name>.ospf(<interface>, <instance>, <ip address>, <area>)
To configure eigrp: <object name>.eigrp(<interface>,<AS number>, <ip address>)
To send a command and see the output: <object name>.cmd("<command to be sent to switch>")


Current configuration for NX-OS only. IOS configurations can be added. Methods for other protocols can be added as well.



Yusuf Khan
