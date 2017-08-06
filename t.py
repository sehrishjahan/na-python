import paramiko

ssh = paramiko.SSHClient()
ssh.connect( 'hostname', username = 'cisco', password = 'cisco1234' )
ssh.exec_command( 'ls -al' )
