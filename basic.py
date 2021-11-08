import cv2
import numpy as np
import face_recognition

# Carrega imagem principal
img_ye = face_recognition.load_image_file("imagesTest/Kanye West.jpg")
img_ye = cv2.cvtColor(img_ye, cv2.COLOR_BGR2RGB)

# Carrega imagem a ser testada
img_test = face_recognition.load_image_file("imagesTest/Jay Z.jpg")
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

# Localiza as faces da imagem principal e extrai sua codificação
faceLocYe = face_recognition.face_locations(img_ye)[0]
encodeYe = face_recognition.face_encodings(img_ye)[0]
cv2.rectangle(img_ye, (faceLocYe[3], faceLocYe[0]), (faceLocYe[1], faceLocYe[2]), (0,255,0), 2)

# Localiza as faces da imagem de teste e extrai sua codificação
faceLocTest = face_recognition.face_locations(img_test)[0]
encodeTest = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_test, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0,255,0), 2)

# Compara as duas faces
faceDist = face_recognition.face_distance([encodeTest],encodeYe)
faceComp = face_recognition.compare_faces([encodeTest],encodeYe, tolerance=0.55)
print(faceComp, faceDist)

# Mostra as imagens
# cv2.imshow('Ye',img_ye)
# cv2.imshow('Who?',img_test)
cv2.waitKey(0)