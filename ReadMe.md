Python version: 3.12.1
    -Python Libraries
    Netmiko is a multi-vendor library that simplifies the process of connecting to network devices and executing commands. 
    It supports a variety of devices, including Cisco, Juniper, and others.
*********************************************************************************************************************************************    
Cisco Catalyst 2960 plus series 48 Port

64K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address       : "your MAC Address here"
Motherboard assembly number     : 73-15619-01
Power supply part number        : 341-0097-03
Motherboard serial number       : "number goes here"
Power supply serial number      : ALD1735B3D4
Model revision number           : A0
Motherboard revision number     : A0
Model number                    : WS-C2960+48TC-L
System serial number            : "number goes here"
Top Assembly Part Number        : 800-40260-01
Top Assembly Revision Number    : A0
Version ID                      : "version"
CLEI Code Number                : "code goes here"
Hardware Board Revision Number  : 0x0C


Switch Ports Model              SW Version            SW Image
------ ----- -----              ----------            ----------
*    1 50    WS-C2960+48TC-L    15.0(2)SE5            C2960-LANBASEK9-M

*********************************************************************************************************************************************
This is a project that intends to configure a Cisco Catalyst 2960 plus switch using a combination of Python,  shell scripts and  IOS commands.
I will outline the process as well as any debugging that I encounter in the process. See Index below.
*********************************************************************************************************************************************
INDEX:
*********************************************************************************************************************************************
1) Setup-Connecting to Cisco switch.
2) Enable SSH on the Cisco Switch.
3) Python Scripting.
    I) Install dependancies.
   II) Write a Python script to interact with the switch using the Netmiko library (SSH client for Python).
4) Use Netmiko to establish an SSH connection, send commands, and receive output.
5) Shell Script Integration.
    I)  Use shell scripts to automate certain tasks on your computer before or after interacting with the Cisco switch.
7) Configuration Templates.
    I) Create configuration templates for the Cisco switch settings you want to apply. Use placeholders for dynamic values.
9) Parameterization.
    I) Modify Python script to read from configuration templates and replace placeholders with actual values.
11) Testing and Debugging.
    I) Ensure you have a factory reset baseline before starting.
    II) Run the Python scripts and then confirm the results in the Cisco switch.
13) Security Considerations.
    I) Ensure secure handling of credentials in your script, i.e. make a config file for credential configuration & file management.
   II) Implement necessary security measures to protect against unauthorized access.
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Setup: You can connect to the Cisco switch using the following method.


Use a console cable (usually provided with the Cisco device) to connect the console port on the Cisco switch to the serial port on your PC.
Install PuTTY: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://apps.microsoft.com/detail/XPFNZKSKLBP7RJ?hl=en-us&gl=US)
PuTTY Documentation: https://documentation.help/PuTTY/

Launch PuTTY on your PC.
Configure the serial connection:

In PuTTY, select the "Serial" connection type.
Specify the serial line to which your console cable is connected (e.g., COM1, COM2).
 You can see what com port your PC is using by going to...
 1) Computer management
 2) Device Manager
 3) Expand "Ports" menu
 4) You will see your USB Serial Port "COM" listed in my00 case it is COM3


Set the speed/baud rate to the standard value, often 9600 bits per second.
Click "Open" to establish the connection:

Click the "Open" button in PuTTY to establish the console connection to the Cisco switch.
Log in to the Cisco switch:

Once the connection is established, you should see the console output from the Cisco switch.
Log in using the switch's credentials.
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Enable SSH on the Cisco Switch.

switch> enable
switch# configure terminal
switch(config)# crypto key generate rsa
switch(config)# ip ssh version 2
switch(config)# username <your_username> privilege 15 secret <your_password>
switch(config)# line vty 0 15
switch(config-line)# transport input ssh
switch(config-line)# login local
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Python Scripting.
I) Install dependancies.
Netmiko Documentation: https://pypi.org/project/netmiko/
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Shell Script Integration.


*********************************************************************************************************************************************
*********************************************************************************************************************************************
Configuration Templates


*********************************************************************************************************************************************
*********************************************************************************************************************************************
Parameterization


*********************************************************************************************************************************************
*********************************************************************************************************************************************
Testing and Debugging


*********************************************************************************************************************************************
*********************************************************************************************************************************************
Security Considerations


*********************************************************************************************************************************************
*********************************************************************************************************************************************

*********************************************************************************************************************************************
*********************************************************************************************************************************************
