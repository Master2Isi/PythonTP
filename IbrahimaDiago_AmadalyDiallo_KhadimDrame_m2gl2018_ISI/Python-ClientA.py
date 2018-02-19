from classpackage.PythonClasseEmploye import *
from classpackage.PythonClasseService import *
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
        
        cpt=1; 
        for x in sys.argv:     
            if x=="-s":
                findRep=sys.argv[cpt]
                print(findRep)
                nomf=os.path.basename(findRep)
                print(nomf)
                if(os.path.exists(findRep)==True):
            #         #f=open(findRep,'r')
            #         s=Service()
            #         #l=f.readlines()

            #         with open(findRep, "r") as f :
     
            #         fichier_entier = f.read()
            #         files = fichier_entier.split("\n")
 
            #         for fichier in files :
     
            #         with open(fichier, 'r') :
  
            # # CONDITIONS
                f=open(findRep,'r')
                s=Service()
                lignes=f.readlines()
                lfs="Service#"
                for ligne in lignes :
              
                    for attr in ligne.split(";"):
                    if attr.split(":")[0]=="id":
                         s.setId(attr.split(":")[1])
                    if attr.split(":")[0]=="date_creation":
                         s.setDate(att.split(":")[1])
                    if attr.split(":")[0]=="res_matri":
                         s.setMat(att.split(":")[1])
                lfs=lfs+ligne
               
           soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           soc.connect((SERVER,PORT))
           lflignes=lfs.encode()
           soc.send(lflignes)  
           
            
            
        else if x=="-p":
             findRep=sys.argv[cpt]
                print(findRep)
                nomf=os.path.basename(findRep)
                print(nomf)
                if(os.path.exists(findRep)==True):
                f=open(findRep,'r')
                lignes=f.readlines()
                p=Employe() 

                lfp="Employe#"
                for ligne in lignes :
                    for attr in ligne.split(";"):
                        if attr.split(":")[0]=="num_matri":
                            p.setMat( attr.split(":")[1])
                        if attr.split(":")[0]=="nom":
                            p.setNom( attr.split(":")[1])
                        if attr.split(":")[0]=="prenom":
                            p.setPrenom( attr.split(":")[1])
                        if attr.split(":")[0]=="email":
                            p.setAdresse( attr.split(":")[1])
                        if attr.split(":")[0]=="adresse":
                            p.setEmail( attr.split(":")[1])
                        if attr.split(":")[0]=="service":
                            p.setService( attr.split(":")[1])
                lfp=lfp+ligne
               
           soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           soc.connect((SERVER,PORT))
           lflignesp=lfp.encode()
           soc.send(lflignesp)  
        else:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            soc.connect((SERVER,PORT))
            soc.send(b"ce fichier employe ou service n'a pas etait trouvé")
                  
      
    cpt=cpt+1    
  
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


