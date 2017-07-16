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
 
 tn.write("enable\n")
 tn.write("cisco1234\n")
 tn.write("conf t\n")
 #tn.write("show ip interface brief\n")
 #tn.write("end\n")
 #tn.write("exit\n")

 
 print tn.read_all()
