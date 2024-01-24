import paramiko

def create_vlan(switch_ip, username, password, vlan_id, vlan_name):
    try:
        # Connect to the switch
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # If using password authentication, uncomment the line below and update the password variable
        ssh_client.connect(switch_ip, username=username, password=password)
        
        # If using key-based authentication, uncomment the line below and update the ssh_key variable
        # ssh_key = paramiko.RSAKey(filename='/path/to/id_rsa')
        # ssh_client.connect(switch_ip, username=username, pkey=ssh_key)

        # Send commands to create VLAN
        commands = [
            'configure terminal',
            f'vlan {vlan_id}',  # Use variable instead of constant 'VLAN_ID'
            f'name {vlan_name}',  # Use variable instead of constant 'VLAN_NAME'
            'exit'
        ]

        for command in commands:
            stdin, stdout, stderr = ssh_client.exec_command(command)
            print(f"Command: {command}")
            print(stdout.read().decode())

    except paramiko.AuthenticationException:
        print("Authentication failed. Check your credentials.")
    except paramiko.SSHException as e:
        print(f"Unable to establish SSH connection: {str(e)}")
    finally:
        # Close the SSH connection in the 'finally' block to ensure it's always closed
        ssh_client.close()

# Replace these values with your switch's information
switch_ip = ''  # Use lowercase variable names
username = ''  # Use lowercase variable names
password = ''  # Use lowercase variable names
vlan_id = ''
vlan_name = ''

# Call the function to create VLAN
create_vlan(switch_ip, username, password, vlan_id, vlan_name)
