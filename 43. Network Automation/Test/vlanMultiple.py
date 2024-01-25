import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

for j in range(8, 10):
    print ('Telnet to host' + str(j))
    HOST = "10.10.10." + str(j)
    tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"1234\n") #password of your remote device
tn.write(b"conf t\n")

for n in range(2, 15):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Auto_VLAN_" + str(n).encode('ascii') + b"\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))