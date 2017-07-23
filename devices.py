from getpass import getpass

csrv = {    
    'device_type': 'cisco_ios',
    'ip': '192.168.2.11',
    'username': 'csrv',
    'password': getpass()
    'port': 22,
}

csrv2 = { 
    'device_type': 'cisco_ios',
    'ip': '192.168.2.12',
    'username': 'csrv2',
    'password': 'telnet',
    'port': 9722,
}

csrv3 = {     
    'device_type': 'cisco_ios',
    'ip': '192.168.2.13',
    'username': 'csrv3',
    'password': 'telnet',
    'port': 8622,
}
