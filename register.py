import numpy as np

def getNome(id):
    with open('registros/funcionarios.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(',')
            if(entrada[0]==id):
                return entrada[1]
            
def getCargoId(id):
    with open('registros/funcionarios.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(',')
            if(entrada[0]==id):
                return entrada[2].strip()
                break

def getCargoNome(id):
    with open('registros/cargos.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(',')
            if(entrada[0]==getCargoId(id)):
                return entrada[1]

def getNivelSeg(id):
    with open('registros/cargos.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(',')
            if(entrada[0]==getCargoId(id)):
                return entrada[2].strip()

def getInformacoes():
    with open('registros/informacoes.csv', 'r') as registro:
        lista = registro.readlines()
        lista.pop(0)
        id = []
        titulo = []
        nivelSeg = []
        for linha in lista:
            entrada = linha.split(',')
            id.append(entrada[0])
            titulo.append(entrada[1])
            nivelSeg.append(entrada[2].strip())
        return id, titulo, nivelSeg

def printInformacoes(nivelSeg):
    id, titulo, nivel = getInformacoes()
    for id, titulo, nivel in zip(id, titulo, nivel):
        if(nivel==1 or nivelSeg>=nivel):
            print(f'\nID: {id}\t{titulo} - Nível de Acesso: {nivel}')
            
def getTituloInfo(idInfo):
    id, titulo, _ = getInformacoes()
    for id, titulo in zip(id, titulo):
        if(id==idInfo):
            return titulo
        
def getKnownEncodings():
    with open('registros/encodings.csv', 'r+') as encodings:
        lista = encodings.readlines()
        lista.pop(0)
        ids = []
        knownEncodings = []
        for linha in lista:
            entrada = linha.split(',')
            ids.append(entrada[0])
            enc = []
            for encodingStr in entrada[1:]:
                enc.append(float(encodingStr))
            knownEncodings.append(enc)
        return ids, list(np.array(knownEncodings))