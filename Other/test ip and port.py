import os
import socket
a=input("enter the address : ")
b=int(input("port : "))
HOST_UP  = True if os.system("ping -n 1 "+ a) is 0 else False
print(HOST_UP)
if HOST_UP != 1:
	print("Not Found")

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
location = (a, b)
result_of_check = a_socket.connect_ex(location)
if result_of_check != 0:
   print("Port is not open")
   
a_socket.close()