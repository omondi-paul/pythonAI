import os
import pickle
import cv2
import face_recognition as FR
print(cv2.__version__)
imageDir='C:\\Users\HP\Documents\PYTHON\demoImages\known'
names=[]
knownEncodings=[]
for root,dirs,files in os.walk(imageDir): 
    for file in files:
       # print('Your guy is: ', file)
        fullFilePath=os.path.join(root,file)
        #print(fullFilePath)
        name=os.path.splitext(file)[0]
        print(name)

        names.append(name)

        nameFace=FR.load_image_file(fullFilePath)
        faceloc=FR.face_locations(nameFace)[0]
        nameFaceEncode=FR.face_encodings(nameFace)[0]
        knownEncodings.append(nameFaceEncode)
    
print(knownEncodings[1])
print(names)



with open('faceEncodings.pkl', 'wb') as f:  #open as write binary(wb)
    pickle.dump(names, f)
    pickle.dump(knownEncodings,f)
