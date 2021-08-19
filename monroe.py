
from colorama import Cursor, init, Fore

abc = "abcdefghijklmnopqrstuvwxyz  1234567890 %#@![]{}()?¿+-*/"


class UtilCrypto:
    def __init__(self,key):
        self.key = key
        self.limitKey = len(abc) #si la key es mayor a la lontyiud de abc entonces error

    def containerblock(self):
        self.FILENAMES  = input("[!] Write your FILENAME ")
        #self.BODY_FILE = input("[*] >>> ")  #in this part , you will be write

    def cryptoKey(self,key,text):
        n_text = len(text) #si la key es 3 entonces tiene que recorrer tres posiciones por ejemplo 
        self.cryptoChildArray = []
        #a = c

        for new_text in text:  #desarmarmos new_text 
            if new_text in abc: #detect letter si existe en abc
                location = list(abc)
                longIV = len(abc)

                for k in range(len(abc)):
                #donde k es la posicion
                    y = k,abc[k]
                    #print(y)
                    if new_text == abc[k]: #si a = a entonces
                        #print("LETRA = " + new_text + abc[k])
                        #recorrer letras por medio de tuplas
                        #primero saber en donde estamos si estamos en a entonces es 0 si la llave es tres entonces 0 +3 = 3 y la llave 3  = d
                        self.cryptoChild = abc[k+key]
                        #tenemos que leer las qie si existen
                        print(Fore.GREEN + "Cipher successfully!: "+ self.cryptoChild)
                        #como van saliendo crear un array e irlos agregando 
                        self.cryptoChildArray.append(self.cryptoChild)

                        self.cryptoChild = ' '.join(map(str,self.cryptoChildArray))
                        print(self.cryptoChild)

                    else:
                        pass
                        #print("NO se encontro ina igulacion a a la  LETRA")
                
            else:
                return "symbol not exists"
                    
        #return n_text

    
    def DecryptMsg(self,key,text):
        pass
    
    def WriteInFileName(self):
        if len(self.FILENAMES)>0:
            with open(self.FILENAMES+'.txt',"wb") as ManagerFile:
                ManagerFile.write(self.cryptoChild.encode())
                return Fore.YELLOW + "[*] FILE CREATED SUCCESSFULLY"
        else:
            return "PUT ANYTHING IN FILENAME"


UtilC = UtilCrypto(True)
print(UtilC.cryptoKey(5,'atacar el lunes en mexico'))
UtilC.containerblock()
print(UtilC.WriteInFileName())
#print(Cipher())

#tambirne qeuermos un metodo para escribirlo en un arcivh
#atmbine quiero un metodo para enviarlo en email

