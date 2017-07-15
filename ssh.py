import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.2.110', port=22, username='csrv', password='cisco1234')
#Start an interactive shell session on the router
        connection = session.invoke_shell()	
        
        #Setting terminal length for entire output - disable pagination
        connection.send("terminal length 0\n")
        time.sleep(1)
        
        #Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

#stdin, stdout, stderr = ssh.exec_command('show ip int brief')
#output = stdout.readlines()
#type(output)
#print '\n'.join(output)

