import netmiko

router_ip = '192.168.56.103'
username = 'cisco'
password = 'cisco123!'
device_type = 'cisco_ios'

commands = [
    'show ip interface brief',
    'show running-config',
    'show version'
]

with netmiko.ConnectHandler(ip=router_ip, device_type=device_type, username=username, password=password) as net_connect:
    for command in commands:
        output = net_connect.send_command(command)
        print(f'{command}:')
        print(output)
        print()
