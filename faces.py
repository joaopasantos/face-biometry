import os
import cv2
import numpy as np
import face_recognition

def getEncodings(path):
    # path = 'users' # Caminho até a pasta de imagens
    images = []
    names = []
    list = os.listdir(path) # Guarda o nome de todos os arquivos na pasta de imagens
    
    # Lê todas as imagens e guarda seu conteúdo e nome nas listas
    for funcionario in list:
        currentImg = cv2.imread(f'{path}/{funcionario}')
        images.append(currentImg)
        names.append(os.path.splitext(funcionario)[0])
    
    encodingsKnowFaces = findEncoding(images)
    
    return names, encodingsKnowFaces

def findEncoding(images):
    encodings = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        currentImgEncoding = face_recognition.face_encodings(img)[0]
        encodings.append(currentImgEncoding)
    return encodings

def identify(img, names, knownEncodings):
    faceLoc = face_recognition.face_locations(img)
    if(len(faceLoc)>1):
        print('Múltiplas faces detectadas, cancelando operação.')
        return False, None
    elif(len(faceLoc)==0):
        print('Nenhuma face detectada.')
        return False, None
    encoding = face_recognition.face_encodings(img, faceLoc)
    
    for encoding, location in zip(encoding, faceLoc):
        comparisons = face_recognition.compare_faces(knownEncodings, encoding, tolerance=0.55)
        distances = face_recognition.face_distance(knownEncodings, encoding)
        matchIndex = np.argmin(distances)
        
        if(comparisons[matchIndex]):
            name = names[matchIndex]
            # y1, x2, y2, x1 = location
            # cv2.rectangle(img, (x1,y1),(x2,y2), (0,255,0),2)
            # cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0),cv2.FILLED)
            # cv2.putText(img, f'{name}', (x1+6,y2-6), cv2.FONT_HERSHEY_DUPLEX, 0.75, (255,255,255),1)
            # cv2.imshow('Identified Face', img)
            # cv2.waitKey(0)
            return True, name
        else:
            return False, None