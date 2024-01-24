Python version: 3.12.1
    -Python Libraries
    Netmiko is a multi-vendor library that simplifies the process of connecting to network devices and executing commands. 
    It supports a variety of devices, including Cisco, Juniper, and others.
    Paramiko is a dependancy of Netmiko and automatically installed with netmiko.
    Name: netmiko
Version: 4.3.0
Summary: Multi-vendor library to simplify legacy CLI connections to network devices
Home-page: https://github.com/ktbyers/netmiko
Author: Kirk Byers
Author-email: ktbyers@twb-tech.com
License: MIT
    Name: paramiko
Version: 3.4.0
Summary: SSH2 protocol library
Home-page: https://paramiko.org
Author: Jeff Forcier
Author-email: jeff@bitprophet.org
License: LGPL

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
------------------------------------------------------------------------------------------------------------------------------------------
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE5, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Fri 25-Oct-13 13:34 by prod_rel_team

ROM: Bootstrap program is C2960 boot loader
BOOTLDR: C2960 Boot Loader (C2960-HBOOT-M) Version 15.0(2r)EZ, RELEASE SOFTWARE (fc2)
------------------------------------------------------------------------------------------------------------------------------------------
*Keeping your console cable connected, connect your switch to your router to obtain an IP adress.
*    You will need the IP address of your cisco device, keep in mind that if you are using DHCP you will need to update your configuration
*    to static for SSH connections or lookup the Ip if your IP address changes. From (privileged EXEC) you run the command "show ip interface brief"
*    and do not see an IP address listed you will need to configure the device IP first.

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
6) Configuration Templates.
    I) Create configuration templates for the Cisco switch settings you want to apply. Use placeholders for dynamic values.
7) Parameterization.
    I) Modify Python script to read from configuration templates and replace placeholders with actual values.
8) Testing and Debugging.
    I) Ensure you have a factory reset baseline before starting.
    II) Run the Python scripts and then confirm the results in the Cisco switch.
9) Security Considerations.
    I) Ensure secure handling of credentials in your script, i.e. make a config file for credential configuration & file management.
   II) Implement necessary security measures to protect against unauthorized access.
10) Troubleshooting
        I) Enable secret
       II) 
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 1 
Setup: You can connect to the Cisco switch using the following method.
*********************************************************************************************************************************************

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
----------------------------------------------------------------------
Obtain the IP address of the switch
1) open PuTTY
2) type:
   
----------------------------------------------------------------------
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 2 
Enable SSH on the Cisco Switch using the following commands.
*********************************************************************************************************************************************
switch> enable
switch# configure terminal
switch(config)# crypto key generate rsa
----------------------------------------------------------------------
!!!!!!RSA key size needs to be atleast 768 bits for ssh version 2!!!!!
----------------------------------------------------------------------
The name for the keys will be: Switch.YourDomainNameYouMadeIsHere
Choose the size of the key modulus in the range of 360 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 768
----------------------------------------------------------------------

switch(config)# ip ssh version 2
switch(config)# username <your_username> privilege 15 secret <your_password>
switch(config)# line vty 0 15
switch(config-line)# transport input ssh
switch(config-line)# login local

*    You will need the IP address of your cisco device, keep in mind that if you are using DHCP you will need to update your configuration
*    to static for SSH connections or lookup the Ip if your IP address changes. From (privileged EXEC) you run the command "show ip interface brief"
*    and do not see an IP address listed you will need to configure the device IP first.
*    !!!!!SEE SECTION!!!!! "Toubleshooting-configure your Cisco switch to obtain an IP address dynamically using DHCP"
*********************************************************************************************************************************************
*********************************************************************************************************************************************
Python Scripting.
1) Install dependancies.
Netmiko Documentation: https://pypi.org/project/netmiko/
2) create a script
   I) import paramiko

def create_vlan(switch_ip, username, password, vlan_id, vlan_name):
    # Connect to the switch
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(switch_ip, username=username, password=password)

    # Send commands to create VLAN
    commands = [
        'configure terminal',
        f'vlan {vlan_id}',
        f'name {vlan_name}',
        'exit'
    ]

    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())

    # Close the SSH connection
    ssh_client.close()

# Replace these values with your switch's information
switch_ip = '<switch_ip>'
username = '<your_username>'
password = '<your_password>'
vlan_id = '10'  # Replace with your desired VLAN ID
vlan_name = 'MYVLAN'  # Replace with your desired VLAN name

# Call the function to create VLAN
create_vlan(switch_ip, username, password, vlan_id, vlan_name)


*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 3 
Shell Script Integration.
*********************************************************************************************************************************************

*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 4 
Configuration Templates
*********************************************************************************************************************************************

*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 5
Parameterization
*********************************************************************************************************************************************

*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 6 
Testing and Debugging
*********************************************************************************************************************************************

*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 7
Security Considerations
*********************************************************************************************************************************************

*********************************************************************************************************************************************
*********************************************************************************************************************************************
Section 8
Troubleshooting
*********************************************************************************************************************************************

------------------------------------------------------------------------------------------------------------------------------------------------------
Toubleshooting-Enable secret
------------------------------------------------------------------------------------------------------------------------------------------------------

After factory restting your switch you may need get a warning message "Enable secret warning". Follow these steps to configure the secret.
1) Enter Privileged EXEC Mode:

Enter Privileged EXEC mode by typing:

Switch> enable

2) Enter Global Configuration Mode:

Enter Global Configuration Mode by typing:

Switch# configure terminal

3) Set the Enable Secret Password:

Set the enable secret password using the following command:

Switch(config)# enable secret <enter your password>
Replace <enter your password> with your desired enable secret password.

Alternatively, you can use a more secure method by using the following command to set the enable secret in encrypted form:

Switch(config)# enable secret <encrypted_password>
Replace <encrypted_password> with the encrypted form of your desired password. You can generate the encrypted form using tools or online resources.

4) Exit Configuration Mode:

Exit Configuration Mode by typing:

Switch(config)# end or Ctrl+Z 
5) Save the Configuration:

Save the configuration to the startup configuration file to make the changes permanent:

Switch# write memory
------------------------------------------------------------------------------------------------------------------------------------------------------
Toubleshooting-Please define a domain-name first
------------------------------------------------------------------------------------------------------------------------------------------------------
 When you arrive at the 2) Enable SSH on the Cisco Switch. step and get an error message "please define domain name" you can follow these steps to do so
 and allow you to complete SSH enable.
 1) type:
    Switch>enable
 3) enter password you created during "enable secret process".
 4) type:
    Switch# configure terminal
5) type:
    Switch(config)# ip domain-name <a name for your device>
6) To exit configure terminal type:
    Switch(config)# end
7) Switch# write memory
8) continue from Enable SSH on the Cisco Switch
------------------------------------------------------------------------------------------------------------------------------------------------------
Toubleshooting-configure your Cisco switch to obtain an IP address dynamically using DHCP
------------------------------------------------------------------------------------------------------------------------------------------------------   
configure your Cisco switch to obtain an IP address dynamically using DHCP:
1) Enter Global Configuration Mode:

Switch# configure terminal
2) Enter Interface Configuration Mode for VLAN 1 (or your management VLAN):

Switch(config)# interface vlan 1
3) Configure the Interface to Obtain an IP Address via DHCP:

Switch(config-if)# ip address dhcp
4) Enable the Interface:

Switch(config-if)# no shutdown
5) Exit Configuration Mode:

Switch(config-if)# exit
6) Save the Configuration:

Switch# write memory
These commands configure the VLAN 1 interface (or your management VLAN) to obtain an IP address dynamically using DHCP. The ip address dhcp command instructs the switch to request an IP address from a DHCP server.
After configuring the switch, it will send a DHCP request to the DHCP server on the network. Make sure that you have a DHCP server in your network that can provide IP addresses to devices.
You can verify the configuration and check if the switch has obtained an IP address by using the following command:

7) Show Cisco device IP address
  Switch# show ip interface brief
Look for the VLAN 1 interface in the output, and ensure that it has an IP address assigned by DHCP.
*********************************************************************************************************************************************
*********************************************************************************************************************************************
