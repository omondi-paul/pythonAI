import cv2
print(cv2.__version__)
import numpy as np
row=400  #int(input('Boss how big do you want your checkers board '))
while True:
    frame=np.zeros([row,row,3],dtype=np.uint8)  
    for i in range(0,row,int(row/4)):
        for j in range(0,row,int(row/4)):
            frame[i:i+int(row/8),j:j+int(row/8)]=(0,75,150)
            frame[i+int(row/8):i+int(row/4),j+int(row/8):j+int(row/4)]=(0,75,150)    
    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff== ord('q'):
        break