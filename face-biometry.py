import os
import cv2
import numpy as np
import face_recognition
import faces
import capture
import register

print('MINISTÉRIO DO MEIO AMBIENTE\n')
print('Acessando o banco de dados...')
try:
    print('\nIniciando o processo de biometria facial...')
    names, knownEncodings = faces.getEncodings('funcionarios')
    print(len(knownEncodings), ' registro(s).')
    img = capture.video()
    id = faces.identify(img, names, knownEncodings)
    print('Biometria realizada com sucesso!')
    print(f'\nBem vindo, {register.getName(id)}.')
    print(f'Seu registro:\n\tID: {id}\n\tCargo: {register.getCargoNome(id)}\n\tNivel de Acesso: {register.getNivelSeg(id)}')
    print('\nQual documento você deseja acessar?')
    
    register.printInformacoes(register.getNivelSeg(id))
    
    
    info = input('Digite o ID do documento que deseja acessar: ')
    print(f'O documento \"{register.getTituloInfo(info)}\" será aberto em outra janela.')
    pass
except RuntimeError as err:
    print(err)
    pass