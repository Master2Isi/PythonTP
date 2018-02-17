# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:13:24 2018

@author: AmaDaly
"""

import datetime
import random
import sys
import mysql.connector as mc

try:
    connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()
class Employe:
    liste=[]
    
    def __init__(self):
        self.id=""
        self.num_matri=""
        self.nom=""
        self.prenom=""
        self.adresse=""
        self.email=""
        self.service=""
        Employe.liste.append(self)
     
     # Pour l'id
    def getId(self):
        return self.id
    def setId(self, id):
        self.id=id   
        # Pour le matricule
    def getMat(self):
        return self.num_matri
    def setMat(self, num_matri):
        self.num_matri=num_matri
        
    # Pour le nom
    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom=nom
        
    # Pour le prenom
    def getPrenom(self):
        return self.prenom
    def setPrenom(self, prenom):
        self.prenom=prenom
        
    # Pour l'email
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email=email
        
    # Pour l'adresse
    def getAdresse(self):
        return self.adresse
    def setAdresse(self, adresse):
        self.adresse=adresse
     # Pour le service
    def getService(self):
        return self.service
    def setService(self, service):
        self.service=service   
        
    
    @staticmethod    
    def create_table_Emp():
        
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

        cursor = connection.cursor()
        
        cursor.execute ("DROP TABLE IF EXISTS employee")
        sql_command = """
        CREATE TABLE employee ( 
        id INTEGER PRIMARY KEY , 
        num_matri VARCHAR(20), 
        nom VARCHAR(30),
        prenom VARCHAR(30),
        email VARCHAR(30),
        adresse VARCHAR(60),
        service INTEGER 
        );"""

        cursor.execute(sql_command)
        print("create")
    
    
    @staticmethod
    def data_entry_Emp():
        employe= Employe()
        employe.setMat(input("mat : "))
        employe.setNom(input("Nom : "))
        employe.setPrenom(input("Prenom : "))
        employe.setEmail(input("Email : "))
        employe.setAdresse(input("Adresse : "))
        employe.setService(int(input("Service : ")))
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

        cursor = connection.cursor()
        cursor.execute("INSERT INTO employe (id,num_matri,nom,prenom,email,adresse,service) VALUES ('%d','%s','%s','%s','%s','%s','%d')",
                  employe)
        connection.commit()
        print("Une employe  a été ajouté ")

        
    
    @staticmethod   
    def read_from_db_Emp():
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

        cursor = connection.cursor()
        cursor.execute('select  * from employe')
        #data = cursor.fetchall()
        #print(data)
        for row in cursor.fetchall():
            print("matricule: "+row[1],"nom: "+row[2], "prenom: "+row[3]) 
    @staticmethod
    def AffichageEmp() :
        print("***************Affichage de la liste du  des Employe*****************")
        employe=Employe()
        employe.read_from_db_Emp()        
            
while True:
    print("0 -> Ajouter un employer dans la base")
    print("1 -> creer la table employe")
    print("2 -> Affichage de la liste des employe")
    print("3 -> Modification d'un employe ")
    print("4 -> Supression")
    print("5 -> Quitter")
    try:
            choix=int(input('Faites votre choix: '))
    except Exception:
            print("Choix érroné")
            continue
    if(choix in range (0,6)) :
    
        if(choix==0) :
            employe=Employe()
            employe.data_entry_Emp()       
                
        elif(choix ==1):
            employe=Employe()
            employe.create_table_Pers()
        elif(choix ==2):
            employe=Employe()
            employe.AffichageEmp()    
        else:
            print("Au revoir")
            break