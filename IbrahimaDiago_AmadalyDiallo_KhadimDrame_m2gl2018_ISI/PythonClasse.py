# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:13:24 2018

@author: AmaDaly
"""
import sqlite3

import datetime
import random
import pymysql
conn=sqlite3.connect('Personne.db')
#conn =pymysql.connect(host="localhost",user="root",passwd="",db="my_python")
c=conn.cursor()
class Employe:
    liste=[]
    
    def __init__(self):
        self.id=""
        self.nom=""
        self.prenom=""
        self.adresse=""
        self.email=""
        Personne.liste.append(self)
        
        # Pour l'id
    def getId(self):
        return self.id
    def setId(self, id):
        self.id=id
        
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
        
        
    def AffichagePer() :
        print("***************Affichage de la liste du  des Employe*****************")
        read_from_db_Pers()
        
    def create_table_Pers():
        c.execute('CREATE TABLE IF NOT EXISTS Personne( id int primary key,nom TEXT, prenom TEXT ,adresse TEXT ,email TEXT)')
        print("create")

    
    def dynamic_data_entry_Pers():
        nom= self.Nom
        prenom=self.Prenom
        
        date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        keyword='Python'
        value=random.randrange(0,10)
        c.execute("INSERT INTO Personne (nom,prenom,adresse,email,adresse) VALUES (?,?,?,?)",
                  (nom,prenom,email,adresse))
        conn.commit()
        
    def read_from_db_Pers():
        c.execute('select  * from Personne')
        #data = c.fetchall()
        #print(data)
        for row in c.fetchall():
            print(row[2])  
            
    while True:
        print("0 -> Ajouter une personne dans une base")
        print("1 -> Affichage des personne")
        print("2 -> Ajouter un service dans la base")
        print("3 -> Affichage des services")
        print("4 -> Quitter")
        try:
            choix=int(input('Faites votre choix: '))
        except Exception:
            print("Choix érroné")
            continue
        if(choix in range (0,5)) :
    
            if(choix==0) :
                print("Entrez les Informations sur la personne:")
                employe= Employe()
                #id=personne.setId(int(input("id : ")))
                nom   =employe.setNom(input("Nom : "))
                prenom=employe.setPrenom(input("Prenom : "))
                email =employe.setEmail(input("Email : "))
                adresse= employe.setAdresse(input("Adresse : "))
               
                c.execute("INSERT INTO Personne (nom,prenom,adresse,email,adresse) VALUES (?,?,?,?)",
                  (nom,prenom,email,adresse))
                conn.commit()
                print("Une employe  a été ajouté ")
                #personne.dynamic_data_entry_Pers()
            elif(choix ==1):
                personne.AffichagePer()
            else:
                print("Au revoir")
                break