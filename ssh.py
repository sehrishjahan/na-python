import paramiko

ip = '192.168.2.110'
username = 'csrv'
password = 'cisco1234'

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print output

