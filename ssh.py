import paramiko

ip = '192.168.2.110'
port = '22'
username = 'csrv'
password = 'cisco1234'

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port, username=username, password=password, look_for_keys=False, allow_agent=False)

