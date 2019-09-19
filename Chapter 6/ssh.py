import paramiko
from getpass import getpass
import time

ip = input("Please enter your IP address: ")
# ip = "192.168.80.160"
username = input("Please enter your username: ")
# username = "johnkenn"
password = getpass()

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print(output)

print("**************************************** IP **************************")
remote_conn.send("show ip int brief\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print(output)


print("**************************************** enable **************************")
remote_conn.send("enable\n")
time.sleep(.5)
remote_conn.send("cisco\n")
output = remote_conn.recv(65535)
print(output)

print("************************************ Conf T **************************")
remote_conn.send("conf t\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print(output)


remote_conn.send("int loop 1\n")
time.sleep(.5)
remote_conn.send("ip address 3.3.3.3 255.255.255.255\n")
time.sleep(.5)

output = remote_conn.recv(65535)
print(output)

print("**************************************** END **************************")

remote_conn.send("end\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print(output)
