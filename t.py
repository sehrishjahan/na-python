import paramiko
 
ip = '192.168.2.12'
username = 'cisco'
password = 'cisco1234'
 
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre

 
remote_conn_pre.set_missing_host_key_policy(
   paramiko.AutoAddPolicy())
 
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)
print output
remote_conn.send("show ip int brief\n")
output = remote_conn.recv(5000)
print output
