import socket, threading

class server(threading.Thread):
    def __init__(self,arg): 
        threading.Thread.__init__(self)
        self.arg = arg#indice de connexion
        
    def run(self):
        global dictio #stocker les clients connectés   
        nom = self.getName() #nom du thread
        continuer = True
        while(continuer):
            try:
                message = self.arg.recv(1024).decode('utf-8')#le serveur recois un message 
            except socket.error:
                continuer = False
                break
            else:
                for cle in dictio:
                    if cle != nom:
                        dictio[cle].sendall(message.encode('utf8'))#on recupere la connecxion du client dans dictio[cle] et envoyer le msg 
            
        del(dictio[nom])#si le client se deconnecte on le supprime
        for cle in dictio:
            dictio[cle].sendall(("cleint {0} deconnecter").format(nom).encode('utf8'))
                    
host = 'localhost'
port = 6000
dictio = {}

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    mysocket.bind((host, port))
except socket.error:
    print("le serveur nest pas lancer ")
    exit()
    
mysocket.listen(9)
print("le serveur est mis en route ")


continuer = True

while(continuer):
    connexion , adresse = mysocket.accept()
    print("une personne est connecter avec ip {0} et pour port {1}".format(adresse[0], adresse[1]))
    launch = server(connexion)# instanciation de la class server 
    launch.start()#méthode pour demarrer le thread
    
    dictio[launch.getName()] = connexion
