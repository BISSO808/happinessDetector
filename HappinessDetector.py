# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:35:03 2020

@author: bisso
"""
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#doing work with webcam if external video source 1

def detect(gray, frame):
     count=0;
     faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
     #the for loop goe on until the x,y,w h is detected
     for(x,y,w,h) in faces:
         cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
         #cv2.rectangle(areatodraw,xcoordinate, ycoordinate,color of rectangle, thickness)
         roi_gray =gray[y:y+h, x:x+w]
         roi_color= frame[y:y+h, x:x+w]
         smile=smile_cascade.detectMultiScale(gray, 1.7 , 22)
         for(ex, ey, ew, eh) in smile:
              cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255),2) 
              cv2.imwrite("frame%d.jpg" % count, frame)
              count = count + 1
     return frame
video_capture = cv2.VideoCapture(0)       
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame) 
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break        
        
video_capture.release()
cv2.destroyAllWindows()