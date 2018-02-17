# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:13:24 2018

@author: AmaDaly
"""

import time
import datetime
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
class Service:
    liste=[]
    
    def __init__(self):
        self.id=""
        self.date_creation=""
        self.res_matri=""
        
        Service.liste.append(self)
     
     # Pour l'id
    def getId(self):
        return self.id
    def setId(self, id):
        self.id=id   
        # Pour le matricule
    def getResp(self):
        return self.res_matri
    def setResp(self, res_matri):
        self.res_matri=res_matri
        
    # Pour la date
    def getDate(self):
        return self.date_creation
    def setDate(self, date_creation):
        self.date_creation=date_creation
        
   
    
    
    @staticmethod    
    def create_table_Serv():
        cursor.execute ("DROP TABLE IF EXISTS service")
        sql_command = """
        CREATE TABLE service ( 
        date_creation DATE,
        res_matri VARCHAR(20) 
        
        );"""

        cursor.execute(sql_command)
        print("create")

    
   

    @staticmethod      
    def data_entry_Serv():
        unix= time.time()
        date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        service= Service()
        service.setResp(input("matricule responsable : "))
        service.setDate(date)
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        
        cursor.execute("""INSERT INTO service (date_creation,res_matri) VALUES ('%s' ,'%s')""",
                  service)
        connection.commit()
        print("Une service  a été ajouté ")
                
    @staticmethod     
    def read_from_db_Serv():
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
        cursor = connection.cursor()
        cursor.execute('select  * from service')
        for row in cursor.fetchall():
                print("matricule responsable: "+row[1],"date creation: "+row[2]) 
    @staticmethod
    def AffichageServ() :
        print("***************Affichage de la liste du  des Service*****************")
        service=Service()
        service.read_from_db_Serv()        
            
while True:
    print("0 -> Ajouter un service a la base")
    print("1 -> creer la table service")
    print("2 -> Afficher les servicew dans la base")
    print("3 -> Modification d'un services")
    print("4 -> Quitter")
    try:
            choix=int(input('Faites votre choix: '))
    except Exception:
            print("Choix érroné")
            continue
    if(choix in range (0,5)) :
    
        if(choix==0) :
            service=Service()
            service.data_entry_Serv()       
                
        elif(choix ==1):
            service=Service()
            service.create_table_Serv()
        elif(choix ==2):
            service=Service()
            service.AffichageServ()     
        else:
            print("Au revoir")
            break