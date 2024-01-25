import getpass
import sys
import telnetlib

HOST = "10.10.10.6"
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
tn.write(b"ip address 200.20.20.1 255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"int fa 0/1\n")
tn.write(b"no shut\n")
tn.write(b"int fa 0/1.10\n")
tn.write(b"encapsulation dot1Q 10\n")
tn.write(b"ip address 192.168.10.1 255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"ip access-group 150 in\n")
tn.write(b"ip dhcp pool CCNA\n")
tn.write(b"network 192.168.10.0 255.255.255.0\n")
tn.write(b"default-router 192.168.10.1\n")
tn.write(b"dns-server 8.8.8.8\n")
tn.write(b"router ospf 10\n")
tn.write(b"network 200.20.20.0 0.0.0.255 area 0\n")
tn.write(b"network 192.168.10.0 0.0.0.255 area 0\n")
tn.write(b"access-list 150 permit tcp host 192.168.10.2 host 200.20.20.2 eq 80\n")
tn.write(b"access-list 150 deny icmp host 192.168.10.2 host 200.20.20.2\n")
tn.write(b"access-list 150 permit ip any any\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))