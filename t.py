import paramiko

ip = '192.168.2.12'
username = 'cisco'
password = 'cisco1234'
 
ssh=paramiko.SSHClient()



 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('show ip int br')

output = stdout.readlines()
print \n.joinoutput()
