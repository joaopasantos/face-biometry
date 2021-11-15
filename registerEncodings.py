import faces

with open('registros/encodings.csv', 'r+') as encodings:
    lista = encodings.readlines()
    lista.pop(0)
    idsRegistrados = []
    for linha in lista:
        entrada = linha.split(',')
        idsRegistrados.append(entrada[0])
    id, knownEncodings = faces.getEncodings('funcionarios')
    for id, knownEncodings in zip(id, knownEncodings):
        if id not in idsRegistrados:
            linha = f'\n{id},'
            for encoding in knownEncodings:
                linha+=f'{encoding},'
            encodings.writelines(linha[:-1])