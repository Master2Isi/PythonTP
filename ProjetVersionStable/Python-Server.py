 
import socket, threading

#importation des classe service et employe qui se trouvent dans le dossier classpackage
from classpackage.PythonClasseEmploye import *
from classpackage.PythonClasseService import *

#Création de la classe client thread
class ClientThread(threading.Thread):

    #Initialisation de la classe
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

    #Définition de la methode run
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            #reception de la donnee string  venant du client
            data = self.csocket.recv(2048)

            #decodage de la donnee recu
            msg = data.decode()

            #recuperation du service qui represente les trois premiers caracteres de la donnee recu
            invok = msg[:3]
            
            #si invok est egale a service on fait le traitement suivant_______________
            if(invok=="ser"):
                print("Client appel table service")

                #recuperation du reste de la donnee envoyé par le client
                msg2 = msg[3:]

                #les donnee recu sont séparer par un retour a la ligne, on fait une splite et on recupre le resultat dans une list (result)
                result = msg2.split("\n")

                #la derniere donnee de la liste est vide(on sait pas pourquoui) donc on l'élimine de la liste
                del result[-1]
                
                #On declare un objet service de la classe service déja importé plus haut
                service=Service()

                #On parcour la liste des donnees recuillit et traité cette action nous renvois pour chaque ligne une chaine Exemple :'compta,5'
                for resp in result:
                    #On fait un split de chaque ligne pour recuperer les infos dans une liste (a) Exemple : a['compta','5']
                    a = resp.split(",")

                    #On fait appel a la methode data_entry_serv de la classe service pour inserer les donnees dans la table service de la base 
                    service.data_entry_Serv(a[0],a[1])

            #Si invok est egale a employe on fait le traitement suivant__________________
            elif(invok=="emp"):
                print("Client appel table employe")

                #recuperation du reste de la donnee envoyé par le client
                msg2 = msg[3:]

                #les donnee recu sont séparer par un retour a la ligne, on fait une splite et on recupre le resultat dans une list (result)
                result = msg2.split("\n")

                #Ici nous n'avons pas eu besoin de supprimer le dernier element de la liste car il n'est pas vide
                #del result[-1]

                #On declare un objet employe de la classe Employe déja importé plus haut
                employe=Employe()

                #On parcour la liste des donnees recuillit et traité. Cette action nous renvoi pour chaque ligne une chaine Exemple :'134,diago,ibou,dakar,elibrahima@gmail.com,5'
                for resp in result:

                    #On fait un split de chaque ligne pour recuperer les infos dans une liste (a) Exemple : a['134','diago','ibou','dakar','elibrahima@gmail.com','5']
                    a = resp.split(",")

                    #On fait appel a la methode data_entry_Emp de la classe Employe pour inserer les donnees dans la table employe de la base 
                    employe.data_entry_Emp(a[0],a[1],a[2],a[3],a[4],a[5])

            #On initialise le message (confirmSms) a envoyé au client pour lui demandé de continuer ou pas
            confirmSms = "Ok bien recu /Entrer bye to quit"

            #Si le message envoyé par le client est égale a bye donc on quitte le programme
            if msg=='bye':
              break

            #Envoi du message au client
            self.csocket.send(bytes(confirmSms,'UTF-8'))

        #Message apres avoir quitté le programme
        print ("Client at ", clientAddress , " disconnected...")

#parametre du server
LOCALHOST = "127.0.0.1"
PORT = 8080

#Creation de la socket server qui attend les client
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
