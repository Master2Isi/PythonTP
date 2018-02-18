 
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
            x = ' bleu, rouge , vert ' 
            x.split ( ",")
            confirmSms = "Ok bien recu /Entrer bye to quit"
            confirmSms = "Ok bien recu /Entrer bye to quit"
            okclient = "Connected to server"
            okservice = "chargement  dans service avec succes !"
            okemploye = "chargement  dans emplo avec succes !"
            if msg=='bye':
              break
            print ("from",clientAddress,":" , msg)
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
