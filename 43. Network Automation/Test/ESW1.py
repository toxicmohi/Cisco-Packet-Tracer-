import getpass
import sys
import telnetlib

HOST = "10.10.10.9"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"1234\n")
tn.write(b"conf t\n")
tn.write(b"hostname CCNA\n")
tn.write(b"int fa 1/0\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"switchport trunk allowed vlan 10\n")
tn.write(b"int fa 1/1\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"switchport trunk allowed vlan 10\n")
tn.write(b"int fa 1/2\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 10\n")
tn.write(b"exit\n")
tn.write(b"exit\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))