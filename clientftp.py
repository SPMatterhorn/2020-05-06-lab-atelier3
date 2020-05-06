#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Contributeurs : Guillaume, Anais, Aurelie, Geraldine, Stephane
# Lab GNS3 client FTP, Server FTP, Atelier Python du 2020-05-06

from ftplib import FTP

# serverName = input("Nom du serveur ou adresse IPv4: ");
# utilisateur = input("Utilisateur: ");
# motdepasse = input("Mot de passe: ");

ftpObjet = FTP('pc2'); # connexion au serveur ftp pc2, port par défaut, ftpObjet est une instance de la classe FTP
# ftpObjet = FTP(serverName);
ftpReponse = ftpObjet.login(user='user',passwd='testtest'); # identifiant, mot de passe
print("Etat de l'identification: ", ftpReponse);
# ftpObjet.login(utilisateur, motdepasse);
ftpObjet.cwd('/home/user'); # changer de répertoire, se trouver dans le répertoire user

etat=ftpObjet.getwelcome();
print("Etat de la connexion:", etat); # état de la connexion

rep=ftpObjet.dir(); 
print(rep); # affichage du répertoire courant

choix=input("que souhaitez vous faire ? (entrez le num puis enter) \n 1:créer un repertoire \n 2:supprimer un repertoire \n 3:renommer un fichier ou dossier \n 4:arrêter la connexion");
if choix=="1":
   dirname1 = input('taper le nom du repertoire à créer: ') # saisie du répertoire à créer
   newrep= ftpObjet.mkd(dirname1) # création du nouveau répertoire
if choix=="2":
   dirname2 = input('taper le nom du repertoire à supprimer: ') # saisie du répertoire à supprimer
   delrep= ftpObjet.rmd(dirname2) # suppression du répertoire
if choix=="3":
   filename_before = input('taper le nom du fichier ou repertoire à renommer: ') # saisie du fichier ou répertoire à renommer
   filename_after = input('le renommer en: ') # saisie du nouveau nom de fichier ou répertoire
   rename= ftpObjet.rename(filename_before,filename_after) # renommage du fichier ou répertoire
if choix=="4":
   goodbye=ftpObjet.quit(); # arrêt de la connexion
   print(goodbye);


