def getName(id):
    with open('registros/funcionarios.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
            if(entrada[0]==id):
                return entrada[1]
            
def getCargoId(id):
    with open('registros/funcionarios.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
            if(entrada[0]==id):
                return entrada[2].strip()
                break

def getCargoNome(id):
    with open('registros/cargos.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
            if(entrada[0]==getCargoId(id)):
                return entrada[1]

def getNivelSeg(id):
    with open('registros/cargos.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
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
            entrada = linha.split(';')
            id.append(entrada[0])
            titulo.append(entrada[1])
            nivelSeg.append(entrada[2].strip())
        return id, titulo, nivelSeg

def printInformacoes(nivelSeg):
    for id, titulo, nivel in zip(getInformacoes()[0], getInformacoes()[1], getInformacoes()[2]):
        if(nivel==1 or nivelSeg>=nivel):
            print(f'\nID: {id}\t{titulo} - Nível de Acesso: {nivel}')
            
def getTituloInfo(idInfo):
    for id, titulo, nivel in zip(getInformacoes()[0], getInformacoes()[1], getInformacoes()[2]):
        if(id==idInfo):
            return titulo