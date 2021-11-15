import os
import cv2
import numpy as np
import face_recognition

def getEncodings(path):
    images = []
    ids = []
    list = os.listdir(path) # Guarda o nome de todos os arquivos na pasta de imagens
    
    # Lê todas as imagens e guarda seu conteúdo e nome nas listas
    for funcionario in list:
        currentImg = cv2.imread(f'{path}/{funcionario}')
        images.append(currentImg)
        ids.append(os.path.splitext(funcionario)[0])
    
    encodingsKnowFaces = evaluateEncoding(images) # Codificações das faces nas imagens
    
    return ids, encodingsKnowFaces

def evaluateEncoding(images):
    encodings = []
    # Calcula as codificações das faces na lista de imagens passada
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        currentImgEncoding = face_recognition.face_encodings(img)[0]
        encodings.append(currentImgEncoding)
    return encodings

def identify(img, ids, knownEncodings):
    faceLoc = face_recognition.face_locations(img) # Localização das faces da imagem
    if(len(faceLoc)>1):
        raise RuntimeError('Múltiplas faces detectadas, cancelando operação.')
    elif(len(faceLoc)==0):
        raise RuntimeError('Nenhuma face detectada.')
        
    encoding = face_recognition.face_encodings(img, faceLoc) # Calcula a codificação da face detectada
    
    # Compara a codificação da face detectada com as codificações das faces registradas
    for encoding, location in zip(encoding, faceLoc):
        comparisons = face_recognition.compare_faces(knownEncodings, encoding, tolerance=0.55)
        distances = face_recognition.face_distance(knownEncodings, encoding)
        matchIndex = np.argmin(distances) # Face com a 'distância' menor à detectada
        
        if(comparisons[matchIndex]): # Caso esteja dentro do intervalo de tolerância, retorna a combinação
            id = ids[matchIndex]
            return id
        else:
            raise RuntimeError('Nenhuma combinação encontrada.')