import paramiko
ssh = paramiko.SSHClient()

ssh.connect('192.168.2.110', port=22, username='csrv', password='cisco1234')

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.2.110', port=22, username='csrv', password='cisco1234')
stdin, stdout, stderr = ssh.exec_command('show ip int brief')
output = stdout.readlines()
type(output)
type(output)
print '\n'.join(output)

