from Crypto.Util.number import  getPrime
from Crypto.Util.number import inverse
import hashlib
import socket 
from threading import Thread



host = 'localhost'
port = 6000

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try :
    mysocket.connect((host, port))

except socket.error :
    print("connexion echouer avec le serveur ")
    exit()
    
print("connexion etablie avec le serveur")


def gen_rsa_keypair (bits):
    p=getPrime(bits//2)
    q=getPrime(bits//2)
    n=p*q
    e=655337
    d=inverse(e, (p-1)*(q-1))
    return((e,n), (d,n)) #cle pub et cle priv

key  = gen_rsa_keypair(256)

def rsa(m,key):
    return pow(m,key[0],key[1])

def rsa_enc(msg, key):
    m = int.from_bytes(msg.encode('utf-8'),'big')
    c = rsa(m, key)
    return c
    


def rsa_dec(msg, key):
    txt_clair = rsa(msg, key)
    return txt_clair.to_bytes((txt_clair.bit_length()+7) // 8,'big').decode('utf-8')


class Send(Thread):
   
    def __init__(self,arg):
        Thread.__init__(self)
        #super(Send, self).__init__()
        self.arg = arg
        
    def run(self):
        continuer = True
        
        while(continuer):
            
            message = input()
            
            message1 = self.arg.sendall(repr(key[0]).encode('utf8'))#cle

            try:    
                enchifrer = rsa_enc(message, key[0])
                
                #print("enchiffreeer = ",enchifrer)
                
                #self.arg.send(repr(enchifrer).encode('utf-8'))
                dechiffrer = rsa_dec(enchifrer, key[1])
                #print("dechiffrer ", dechiffrer)
                self.arg.send(dechiffrer.encode('utf-8'))

            except socket.error:
                continuer = False
                break
    
        self.arg.close()
    

class receive(Thread):
    
    def __init__(self,arg):
        Thread.__init__(self)
       # super(receive, self).__init__()
        self.arg = arg


    def run(self):
        
        continuer = True

        while(continuer):
            try:
                
                message = self.arg.recv(1024).decode('utf-8')
            except socket.error:
                    continuer = False
                    break
                
            else :
                print(">>>>>> {0}".format(message))
            
        self.arg.close()


if __name__ == "__main__":
    
    sn = Send(mysocket)
    sn.start()

    rv = receive(mysocket)
    rv.start()