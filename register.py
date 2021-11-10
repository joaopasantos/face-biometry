def getName(id):
    with open('registros/funcionarios.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
            if(entrada[0]==id):
                return entrada[1]
            
def getCargo(id):
    with open('registros/funcionarios.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
            if(entrada[0]==id):
                cargo = str(entrada[2])
                break
    with open('registros/cargos.csv', 'r') as registro:
        lista = registro.readlines()
        for linha in lista:
            entrada = linha.split(';')
            if(entrada[0]==cargo.strip()):
                return entrada[1]
            
print(getName('N4279D8'))
print(getCargo('N4279D8'))