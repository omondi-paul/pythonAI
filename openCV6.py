#This program uses numpy to create a cheakers board by defining some parameters and using for loops 

import cv2
print(cv2.__version__)
import numpy as np

boardSize=1000#int(input('What Size is your Board,Boss? '))
numSquare=100#int(input('And Sir, How many squares? '))
squareSize=int(boardSize/numSquare)
darkColor=(0,0,0)
lightColor=(175,175,175)
nowColor=darkColor

while True:
    x=np.zeros([boardSize,boardSize,3],dtype=np.uint8)

    for row in range(0,numSquare):
        for column in range(0,numSquare):
            x[squareSize*row:squareSize*(row+1),squareSize*column:squareSize*(column+1)]=nowColor
            if nowColor==darkColor:
                nowColor=lightColor
            else:
                nowColor=darkColor
        if nowColor==darkColor:
            nowColor=lightColor
        else:
            nowColor=darkColor

    cv2.imshow('My Cheaker Board',x)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
