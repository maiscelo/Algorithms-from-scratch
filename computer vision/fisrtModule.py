'''
Created on 25 de fev de 2020
Marcelo Queiroz de Lima Brilhante
@author: lab
'''
from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse


#backSub = cv.createBackgroundSubtractorMOG2()
backSub = cv.createBackgroundSubtractorKNN(history = 9000,dist2Threshold = 5000.0,detectShadows = False)


out = cv.VideoWriter('outpy.avi',cv.VideoWriter_fourcc('M','J','P','G'), 10, (720,576))
capture = cv.VideoCapture('c:/sea.avi')
retteste, frameteste=capture.read()
#print(frameteste)
#print(retteste)
#backgroundImage=cv.BackgroundSubtractor.getBackgroundImage(capture)
print(type(capture.read))
print(type(retteste))
fgMaskteste = backSub.apply(frameteste)   
print(fgMaskteste)
M=cv.moments(fgMaskteste)
cY=int(M["m10"]/M["m00"])
cX=int(M["m01"]/M["m00"])
i=0
area=1
maior_area=1
maior_area_index=0
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    fgMask = backSub.apply(frame)    
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    #print(np.size(fgMask))
    #print(np.count_nonzero(fgMask))
    nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(fgMask, None, None, None, 8, cv.CV_32S)
    areas = stats[1:,cv.CC_STAT_AREA]
    result = np.zeros((labels.shape), np.uint8)
    
    for i in range(0, nlabels - 1):
        if areas[i] >= 250:   #keep
            result[labels == i + 1] = 255
    
    
    if np.count_nonzero(result)>1500:
        contours,hierarchy = cv.findContours(result, 1, 2)
        cnt = contours
        #print(contours[0])
        #im2,contorno= cv.findContours(fgMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        #print(type(contours))
        #cnt = cnt[0] if len(cnt) == 2 else cnt[1]
        #cnt = sorted(cnt, key=cv.contourArea, reverse=True)
        for i,c in enumerate(cnt):
            #cv.drawContours(frame, [c], -1, (36,255,12), 3)
            area = cv.contourArea(c)
            print(i,area)
            #if area>maior_area:
             #   maior_area=area
              #  maior_area_index=i
               # print(maior_area,'ok')
        R= cv.boundingRect(c);
        cv.rectangle(frame, R,(0,255,0));
        #cv.drawContours(fgMask, contorno, -1, (255,255,255), 3)
        #for c in contours:
        M=cv.moments(result)
        #print(c)
        if M["m00"]!=0:
            cY=int(M["m10"]/M["m00"])
            cX=int(M["m01"]/M["m00"])
        else:
            cX,cY = 0,0
        #cv.drawContours(frame,(cY,cX),5,(255,255,255),10)
        

        cv.circle(frame,(cY,cX),1,(255,205,255),3,cv.LINE_AA)
        #retval=cv.boundingRect(cY,cX)
        out.write(frame)
        cv.imshow('Frame', frame)
        cv.imshow('FG Mask',result)
        i=1+i
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
out.release()
cv.destroyAllWindows() 
