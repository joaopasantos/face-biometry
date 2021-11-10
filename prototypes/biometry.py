import os
import cv2
import numpy as np
import face_recognition

path = 'users' # Caminho até a pasta de imagens
images = []
names = []
list = os.listdir(path) # Guarda o nome de todos os arquivos na pasta de imagens

# Lê todas as imagens e guarda seu conteúdo e nome nas listas
for user in list:
    currentImg = cv2.imread(f'{path}/{user}')
    images.append(currentImg)
    names.append(os.path.splitext(user)[0])

def findEncoding(images):
    encodings = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        currentImgEncoding = face_recognition.face_encodings(img)[0]
        encodings.append(currentImgEncoding)
    return encodings

encodingsKnowFaces = findEncoding(images)

# Informa quantas codificações de faces foram reconhecidas
print(len(encodingsKnowFaces), 'faces found!')

# Inicia a captura de vídeo da Webcam
cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    if not sucess:
        print('Falha ao tentar capturar o vídeo.')
        break
    frames = cv2.resize(img, (0,0),None, 0.25,0.25)
    frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    
    facesCurrFrame = face_recognition.face_locations(frames)
    encodingsCurrFrame = face_recognition.face_encodings(frames, facesCurrFrame)
    print(len(facesCurrFrame))
    for encoding, location in zip(encodingsCurrFrame, facesCurrFrame):
        comparisons = face_recognition.compare_faces(encodingsKnowFaces, encoding, tolerance=0.55)
        distances = face_recognition.face_distance(encodingsKnowFaces, encoding)
        print(distances)
        matchIndex = np.argmin(distances)
        
        if(comparisons[matchIndex]):
            name = names[matchIndex]
            print(name)
            y1, x2, y2, x1 = map(lambda v: v*4, location)
            cv2.rectangle(img, (x1,y1),(x2,y2), (0,255,0),2)
            cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0),cv2.FILLED)
            cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_DUPLEX, 0.75, (255,255,255),1)
            
    cv2.imshow('Webcam', img)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressionado
        print("Escape pressionado, fechando janelas...")
        break

cap.release()

cv2.destroyAllWindows()