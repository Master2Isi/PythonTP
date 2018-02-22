 
import socket
import sys,os;
import pickle

SERVER = "127.0.0.1"
PORT = 8080
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((SERVER, PORT))

argument1 = sys.argv[0]
option = sys.argv[2]
lienrepertoire = sys.argv[1]
nonfichier = sys.argv[3]
print("option :"+option)
print("nomfic :"+nonfichier)
print("Lien rep :"+lienrepertoire)

if (option=="-p"):
	print("Insertion dans employe")
	print("Repertoire :" +lienrepertoire)
	print("Option :" +option)
	print("Nom fichier :" +nonfichier)
	rep = lienrepertoire+nonfichier
	print(rep)
	#Verification de lexistence du fichier
	if os.path.exists(rep): 
		print("le fichier existe")

		#Ouverture du fichier en lecture
		mesdata = []
		with open(rep) as fp:  
			for line in fp:
				#formatade de la liste de donnees
				mesdata.append(line.replace('Numero','').replace('nom','').replace('prenom','').replace('adresse','').replace('email','').replace('service','').replace(':','').replace(';',','))

		#print(mesdata)
		data_to_send = ''.join(mesdata)
		#data_to_send = pickle.dumps(mesdata)

		print(data_to_send)
		dataS = "emp"+data_to_send
	
		while True:
			#in_data = client1.recv(1024)
			#print("From server :", in_data.decode())
			client1.send(bytes(dataS,'UTF-8'))
			out_data = input("Voulez vous continuer /bye to quit :")
			if(out_data=="bye"):
				break
			client1.close()

		print("element envoyés")
		#___________________________________________________________________________________________

elif(option=="-s"):
	print("Insertion dans service")
	print("Repertoire :" +lienrepertoire)
	print("Option :" +option)
	print("Nom fichier :" +nonfichier)
	rep = lienrepertoire+nonfichier
	print(rep)
	#Verification de lexistence du fichier
	if os.path.exists(rep): 
		print("le fichier existe")

		#Ouverture du fichier en lecture
		mesdata = []
		with open(rep) as fp:  
			for line in fp:
				#formatade de la liste de donnees
				mesdata.append(line.replace('Nomser','').replace('Resp','').replace(':','').replace(';',','))

		#print(mesdata)
		data_to_send = ''.join(mesdata)
		#data_to_send = pickle.dumps(mesdata)

		print(data_to_send)
		dataS = "ser"+data_to_send
	
		while True:
			#in_data = client1.recv(1024)
			#print("From server :", in_data.decode())
			#client1.send(bytes(ser,'UTF-8'))
			client1.send(bytes(dataS,'UTF-8'))
			out_data = input("Voulez vous continuer /bye to quit :")
			if(out_data=="bye"):
				break
			client1.close()

		print("element envoyés")
	else:
		print("le fichier nexiste pas")


# client1.sendall(bytes("Client_B",'UTF-8'))
# while True:
#   in_data =  client1.recv(1024)
#   print("From Server :" ,in_data.decode())
#   out_data = data_to_send
#   client1.sendall(bytes(out_data,'UTF-8'))
#   if out_data=='bye':
#   	break
# client1.close()
