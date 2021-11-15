import faces
import capture
import register

print('MINISTÉRIO DO MEIO AMBIENTE\n')
print('Acessando o banco de dados...')
try:
    print('\nIniciando o processo de biometria facial...')
    ids, knownEncodings = register.getKnownEncodings()
    print('Focalize a janela de vídeo, e pressione ESPAÇO quando desejar capturar sua imagem de identificação.')
    img = capture.video()
    id = faces.identify(img, ids, knownEncodings)
    print('Biometria realizada com sucesso!')
    print(f'\nBem vindo, {register.getNome(id)}.')
    print(f'Seu registro:\n\tID: {id}\n\tCargo: {register.getCargoNome(id)}\n\tNivel de Acesso: {register.getNivelSeg(id)}')
    print('\nQual documento você deseja acessar?')
    
    register.printInformacoes(register.getNivelSeg(id))
    
    
    info = input('Digite o ID do documento que deseja acessar: ')
    print(f'O documento \"{register.getTituloInfo(info)}\" será aberto em outra janela.')
    pass
except RuntimeError as err:
    print(err)
    pass