 
import socket
SERVER = "127.0.0.1"
PORT = 8080
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect((SERVER, PORT))
client2.sendall(bytes("Client_A",'UTF-8'))

print("===========================================================")
print("____________________APPLICATION GESTION____________________")
print("===========================================================")
print("\n")
print("_____MENU__________________________________________________")

print("0 -> Chargez donnees dans les services du server")
print("1 -> Chargez donnees dans les employes du server")
print("2 -> Faites un chargement mixte dans le server")
print("3 -> Quitter")
print("___________________________________________________________")
try:
		choix=int(input('Faites votre choix: '))
except Exception:
		print("Choix érroné")
if(choix==0) :
	#employe=Employe()
    #employe.data_entry_Emp()
    print("_____CHARGEMENT DES SERVICES_________________________")
    while True:
    	repertoire= input('Donnez le chemin du repertoire des fichiers: ')
    	fichiers= input('Donnez le ou les noms des fichiers séparer par (,): ')
    	client2.sendall(bytes(fichiers,'UTF-8'))
    	in_data =  client2.recv(1024)
    	print("From Server :" ,in_data.decode())
    	out_data = input()
    	service="chargementServices"
    	client2.sendall(bytes(service,'UTF-8'))
    client2.close()
    print("...........................................")
    print("Donnees chargées avec succes !")                    
elif(choix ==1):
    #employe=Employe()
    #employe.create_table_Pers()
    print("_____CHARGEMENT DES EMPLOYESS_________________________")
    repertoire = input('Donnez le chemin du repertoire des fichiers: ')
    fichiers= input('Donnez le ou les noms des fichiers séparer par (,): ')
elif(choix==2):
	print("_____CHARGEMENT MIXTE_________________________________")
	repertoire= input('Donnez le chemin du repertoire des fichiers: ')
	print("NB FORMAT : Nomfichierservice -s, Nomfichieremploye-p etcc")
	fichiers= input('Donnez le ou les noms des fichiers séparer par (,): ')
	print("Donnees mixtes chargées avec succes !") 
else:
    print("Au revoir")

# client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client2.connect((SERVER, PORT))
# client2.sendall(bytes("Client_A",'UTF-8'))
# while True:
#   in_data =  client2.recv(1024)
#   print("From Server :" ,in_data.decode())
#   out_data = input()
#   client2.sendall(bytes(out_data,'UTF-8'))
#   if out_data=='bye':
#   	break
# client2.close()


