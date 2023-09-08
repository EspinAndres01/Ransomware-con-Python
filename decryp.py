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

def decryp(items, key):
    f=Fernet(key)
    for x in items:
        with open(x,"rb") as file:
            fileData=file.read()
        data=f.decrypt(fileData)
        with open(x,"wb")as file:
            file.write(data)

if __name__=="__main__":
    myData='C:\\Users\\kibok\\OneDrive\\Desktop\\Liss\\Ransomware2\\Archivos'
    os.remove(myData+"\\"+"readme.txt")
    items=os.listdir(myData)
    myDataSave=[myData+"\\"+x for x in items]


    key=returnKey()
    decryp(myDataSave,key)