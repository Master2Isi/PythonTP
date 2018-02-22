 
import socket, threading
from classpackage.PythonClasseEmploye import *
from classpackage.PythonClasseService import *


class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            #print(msg)
            invok = msg[:3]
            #print(invok)
            if(invok=="ser"):
                print("Client appel table service")
                msg2 = msg[3:]
                #print(msg2)

                #print(msg.split ( ","))
                result = msg2.split("\n")
                del result[-1]
                #print(len(result))
                service=Service()
                #print(result)
                for resp in result:
                    a = resp.split(",")
                    #print(a[0])
                    service.data_entry_Serv(a[0],a[1])
            elif(invok=="emp"):
                print("Client appel table employe")
                msg2 = msg[3:]
                #print(msg2)

                #print(msg.split ( ","))
                result = msg2.split("\n")
                #del result[-1]
                #print(len(result))
                employe=Employe()
                #print(result)
                for resp in result:
                    a = resp.split(",")
                    #print(a[0])
                    employe.data_entry_Emp(a[0],a[1],a[2],a[3],a[4],a[5])


            confirmSms = "Ok bien recu /Entrer bye to quit"
            if msg=='bye':
              break
            #print ("from",clientAddress,":" , result)
            self.csocket.send(bytes(confirmSms,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
