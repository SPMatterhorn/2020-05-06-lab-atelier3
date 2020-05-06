# 2020-05-06-lab-atelier3
Atelier Python Client FTP

1- Mise en place d’un client FTP avec Python.
Préparation d’une deuxième machine Debian, cette machine devra être sur le même réseau que la première.
Une machine aura pour rôle le serveur FTP, tandis que la deuxième sera le client ftp.
Réaliser un script python qui jouera le rôle de client ftp.
• Pouvoir se connecter, donc :
o Entrer le nom d’hôte
o Le nom d’utilisateur
o Et le mot de passe, très important !
• Pouvoir envoyer une commande (nous les listerons un peu plus bas)
• Pouvoir taper une commande, mais avec des arguments ! (Petite nuance)
On doit pouvoir :
• Créer
• Renommer
• Déplacer
• Supprimer
Des fichiers / dossiers.
On doit aussi pouvoir :
• Se déplacer entre les répertoires
• Lister leur contenu
• Envoyer un fichier sur notre serveur
En voici donc la liste (seulement celles que nous implémenterons) :
• CWD (change current directory) pour changer de répertoire de travail
• DELE (delete) pour supprimer un fichier / dossier
• LIST pour lister les fichiers et dossiers d’un répertoire (si vous n’en spécifiez pas,
alors ce sera le répertoire courant qui sera listé)
• MKD (make directory) pour créer un répertoire
• RMD (remove directory) pour supprimer un répertoire
• RNFR (rename a file from (name …)) pour renommer un répertoire X en …
• STOR (store a file) pour envoyer un fichier sur le serveur.

2- Autre atelier en bonus
Comment via python envoyer des ordres, (installer des packages , lister des fichiers…)
sur la machine serveur.
A partir de la machine cliente.
Les scripts devons être déposer sur un dépôt GitHub en accès publique 
