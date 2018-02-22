 
import socket
import sys,os;
import json

argument1 = sys.argv[0]
lienrepertoire = sys.argv[2]
option = sys.argv[1]
nonfichier = sys.argv[3]

print(option)
print(nonfichier)
print(lienrepertoire)

if(option=="-p"):
	print("Insertion employe")
elif(option=="-s"):
	print("Insertion service")