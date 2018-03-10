import cv2
import numpy as np
import pickle
import socket
import json

def get_frame_step(frameCount):
    return frameCount/4;

cap = cv2.VideoCapture('bashLecture.webm')

data = ''


frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_step = get_frame_step(frameCount)
print frame_step

#buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True
np.set_printoptions(threshold='nan')
print frameCount
frame_no = 0
while (ret and frame_no<frameCount):
    cap.set(1,frame_no);
    ret, buff = cap.read()
    if len((str(buff))) > 0:
      js=json.dumps(buff.tolist())
      js = str(js)
      #print js.encode()
      print "NEXT ITERATION"
    if cv2.waitKey(1) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break
    print fc
    frame_no+=frame_step;
    fc += 1

cap.release()
cv2.namedWindow('frame 10')
cv2.imshow('frame 10', buff)

cv2.waitKey(0)
