#Projeto, Ler um arquivo de texto que contem dados de uma corrida e ordenar os dados de
#forma em que sai a colocação e o tempo de cada piloto.

Arquivo = open('EntradaDados.txt', 'r') #Abrindo o arquivo com os dados.

#Criando os array de entrada e tambem de saida dos dados
ArrayArquivo = []
ArrayPiloto = []
ArrayCorrida = []
contador = 0
for linha in Arquivo:
    ArrayArquivo = linha.split()
    if ArrayArquivo[4] == '1':
        ArrayPiloto.append(ArrayArquivo)
        nTempo = ArrayPiloto[contador][5].replace(':','')
        nTemp = nTempo.replace('.','')
        nMedio = ArrayPiloto[contador][6].replace(',','')
        ArrayPiloto[contador].append(nTemp)
        ArrayPiloto[contador].append(float(nMedio))
        contador += 1
    else:
        ArrayCorrida.append(ArrayArquivo)
Arquivo.close()
for Corrida in ArrayCorrida:
    for Piloto in ArrayPiloto:
        if Piloto[1] == Corrida[1]:
            if int(Piloto[4]) < int(Corrida[4]):
                Piloto[4] = Corrida[4] #Atribuindo o valor da volta no Piloto
            nPiloto = Piloto[5].replace(':', '')
            nCorrida = Corrida[5].replace(':', '')
            nPil = nPiloto.replace('.', '')
            nCor = nCorrida.replace('.', '')
            Piloto[7] = int(Piloto[7]) + int(nCor)
            nMedio = Piloto[6].replace(',', '')
            Piloto[8] += float(nMedio)
            if int(nCor) < int(nPil):
                Piloto[5] = Corrida[5]
            if Piloto[4] == '4':
                Piloto[8] = Piloto[8] / int(Piloto[4])
                break

def ordenador(elem):
    return elem[7]

ArrayPiloto.sort(key=ordenador)
# Variavel Contador
print("Colocação na prova / Codigo Piloto / Nome Piloto / Qtd Volta / Melhor Tempo Piloto / Total Volta / Velocidade Media")
cont = int = 0 #Iniciando o contador pois com a ordenação eles ja etão na ordem de chegado da corrida
for array in ArrayPiloto:
    cont += 1
    array.pop(6)#Removendo o tempo médio da primeira volta do participante
    array.pop(0)
    array.insert(0,cont) #Inserindo no array a colocação do Piloto
    print(array) # Mostrando a colocação e os pilotos


