import faces

with open('registros/encodings.csv', 'r+') as encodings:
    # Lê as linhas do arquivo e retira a primeira, que guarda apenas os rótulos
    lista = encodings.readlines()
    lista.pop(0)
    idsRegistrados = []
    # Guarda os ids já registrados
    for linha in lista:
        entrada = linha.split(',')
        idsRegistrados.append(entrada[0])
    id, knownEncodings = faces.getEncodings('funcionarios') # Calcula as codificações das faces do diretório passado
    # Caso a face ainda não tenha sido registrada, insere o registro com a codificação
    for id, knownEncodings in zip(id, knownEncodings):
        if id not in idsRegistrados:
            linha = f'\n{id},'
            for encoding in knownEncodings:
                linha+=f'{encoding},'
            encodings.writelines(linha[:-1])