 
import socket
SERVER = "127.0.0.1"
PORT = 8080
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((SERVER, PORT))
client2.sendall(bytes("Client_A",'UTF-8'))
while True:
  in_data =  client2.recv(1024)
  print("From Server :" ,in_data.decode())
  out_data = input()
  client2.sendall(bytes(out_data,'UTF-8'))
  if out_data=='bye':
  	break
client2.close()
