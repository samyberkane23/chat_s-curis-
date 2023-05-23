Nom : BERKANE 
Prénom : Samy
N°Etudiant : 20009760
L3 Informatique

Projet : Réaliser un chat (entre deux clients) et chiffrement et déchiffement des messages (RSA).

-Il faut d'abord  compiler et excuter le fichier "serveur.py" : pyhton3 serveur.py 

une fois le serveur lancer il faut compiler et excuter le fichier "client.py" : pyhton3 client.py (deux clients).

-Explications:
Pour le client et le serveur je me suis aidé de cette vidéo : https://www.youtube.com/watch?v=3lOO65PPFqU
   
    -serveur.py :(on a utiliser les thread pour gerer toutes les connections des clients) on a crée la class "Server"  qui contient la méthode "__init__" pour initialisere le thread et la méthode "run" pour executer le thread. 

    -client.py :(on a utiliser les thread pour gerer l'envoi et la reception des messages) on a crée deux class "Send" qui contient la méthode "__init__" et la méthode "run" 
                pour executer le thread et gérer l'envoi des messages et la class "receive"   qui contient la méthode "__init__" et la méthode "run" 
                pour executer le thread et gérer la reception des messages .                                             
    
