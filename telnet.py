import getpass
import sys
import telnetlib

HOST = "192.168.2.110"
user = raw_input("Enter telnet username:")
password =getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
 tn.read_until("Password: ")
 tn.write(password + "\n")
 
 tn.write("ls\n")
  tn.write("exit\n")
