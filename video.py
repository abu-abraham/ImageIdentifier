import cv2
import numpy as np
import pickle
import socket
import json
cap = cv2.VideoCapture('small.m4v')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ='ec2-18-221-176-185.us-east-2.compute.amazonaws.com'
port =8088

data = ''
try:
  s.connect((host,port))
  s.send('connecting'.encode())
  data = s.recv(1024).decode()
except: 
  print "No connection"

sendData = False
if 'connected' in data:
  sendData = True; 
  print "WORKS"
else:
  print data

frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True
np.set_printoptions(threshold='nan')

while (fc < frameCount  and ret):
    ret, buf[fc] = cap.read()
    if len((str(buf[fc]))) > 0:
      s.send("START".encode())
      js=json.dumps(buf[fc].tolist())
      js = str(js)
      print js.encode()
      s.send(js.encode())
      s.send("END".encode())
    if cv2.waitKey(25) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
    fc += 1

cap.release()

cv2.namedWindow('frame 10')
cv2.imshow('frame 10', buf[9])

cv2.waitKey(0)
