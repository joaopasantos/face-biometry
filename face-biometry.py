import os
import cv2
import numpy as np
import face_recognition
import faces
import capture

print('Iniciando o processo de biometria facial...')
names, knownEncodings = faces.getEncodings('funcionarios')
print(len(knownEncodings), 'funcionários registrados.')
success, img = capture.video()
if not success:
    print('Falha ao tentar capturar a imagem.')
    print('Encerrando...')
else:
    # cv2.imshow('Captured Image', img)
    # cv2.waitKey(0)
    success, id = faces.identify(img, names, knownEncodings)
    if not success:
        print('Não foi possível identificar a face.')
    else:
        print(f'Bem vindo, {id}!')
    
    