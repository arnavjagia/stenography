import cv2
import os

img = cv2.imread("./mypic.jpg")

msg = input("Secret message for encryption: ")

password = input("Passcode for encryption: ")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i] = chr(i)

m=0
n=0
z=0

for i in range(len(msg)):
    img[n,m,z] = d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("Encryptedmsg.jpg",img)

# os.system("start Encryptedmsg.jpg")


message =""

n=0
m=0
z=0

pas = input("Passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decrypted message is",message)
else:
    print("Not valid key")
