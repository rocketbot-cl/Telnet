# Telnet
  
Module to work with telnet protocol  

*Read this in other languages: [English](Manual_Telnet.md), [Español](Manual_Telnet.es.md).*
  
![banner](imgs/Banner_telnet.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### configuration
  
Setup telnet
|Parameters|Description|example|
| --- | --- | --- |
|Server|IP address or domain name|test.ftp.com|
|Port|Connection port|0|
|Assign result to variable|Variable name where the connection result will be stored|Variable|
|User|Connection user|user@test.com|
|Password|Connection password|******|

### Read data
  
Read all data until connection closed
|Parameters|Description|example|
| --- | --- | --- |
|Store result in variable|Variable name where the read information will be stored|Variable|

### Write
  
Write data to the socket
|Parameters|Description|example|
| --- | --- | --- |
|Data to write|Data to write in the socket|ls|
