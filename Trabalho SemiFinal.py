# -*- coding: utf-8 -*-
#Funcao para ler os textos presentes no arquivo, e armazena cada texto(arquivo) em uma posicao da lista
def lerArquivos(caminho: str, formato: str, qntArq: int):
    textos = []
    for i in range (1,qntArq+1):   
        arqNome = str(caminho) + str(i) + str(formato) #Concatena com o numero indice para formar o caminho com nome de cada arquivo de texto: "texto1.txt"

        with open(arqNome, "r", encoding="UTF-8") as arquivo: #A funcao open retorna um objeto do tipo manipulador de arquivo, atribuindo ao 'arquivo'
                                                            #Recebe como parametro o caminho e nome do arquivo(se nao for encontrado, sera criado um).
                                                            #'r' = Permite leitura do arquivo
            textos.append(str(arquivo.readlines()))
    for i in range(0,len(textos)):
        #if textos[i][:2] == "['" and textos[i][:-2] == "']":
        textos[i] = textos[i][2:]
        textos[i] = textos[i][:-2]
        
    return textos #Retorna os textos brutos (sem nenhuma filtrar)
#

# ------------------------------------- FUNÇÃO DE ORDENAÇÃO e RANQUEAMENTO ------------------------------------------------------

#Funçao que gera o rank de palavras em ordem alfabetica e na ordem da maior quantidade de letras para menor
def rankingWords(vetorTexto):
    textoAlfabetico = list() #Variavel que armazena o texto organizado em ordem alfabetica
    auxVetTexto = list() #Variavel que salva as palavras para não serem excluidas da memoria

    #Sessão responsav~el por verifica se a variavel é vetor ou string
    for i in range(0,len(vetorTexto)):
        if type(vetorTexto[i])== type(str()): #Se for string transforma em vetor
            vetorTexto[i] = vetorTexto[i].split()
   
   #---------------------------------- FUNÇÕES DE ORDENAÇÃO -----------------------------------------------------------------
    def ordenacaoAlfabetica(vetTexto):
        listaAlfabeto = list()#cria uma lista que vai retornar o alfabeto organizado
        dicionario = dict()#cria um dict que vai armazenar o alfabeto
        
        for i in range(0,len(vetTexto)): #iterador
            dicionario = {} #reinicia o dicionario
            
            for letra in "abcdefghijklmnopqrstuvwxyz": #iterador que gera uma letra do alfabeto em sequencia
                auxVet = list(filter(lambda palavra: palavra[0] == letra, vetTexto[i]))#Funçao que filtra as palavras que atendem a condição de iniciarem pela letra do iterador
                if len(auxVet) == 0: #se o vetor auxiliar estiver vazio, não gera o dicionario
                    #É importante para não criar um dicionario vazio e otimizar mais o processo
                    pass 
                else: #se não estiver vazio, gera o dicionario com as palavras correspondente a letra do alfabeto
                    dicionario[letra] = auxVet #A Chave do dicionario recebe a letra do alfabeto e o "auxVet" é a palavra recebida pelo dicionairo
                    
                    for palavra in auxVet: #Remove as palavras do vetor de texto original para poder acelerar mais o processo
                        #Essa sessão é importante já que evita que o iterador repita as palavras e deixe o processo mais lento
                        vetTexto[i].remove(palavra)
                        try:
                            #o vetor auxiliar vai receber a palavra removida, conforme a ordem de cada texto
                            #obs: o iterador não itera sobre essa variavel
                            auxVetTexto
                            auxVetTexto[i].append(palavra)
                            
                        except IndexError:
                            #Vai concertar o error se caso não encontrar o indice do vetor
                            auxVetTexto.append([palavra])

            #Vai adiciona o dicionario de cada texto a um vetor                
            listaAlfabeto.append(dicionario)
        return listaAlfabeto
    
    def ordemNumerico(texto):
        vetAux = list() #variavel auxiliar que cria a lista de palavras
        vetRetorno = dict()#dicionário a ser retornado
        
        if type(texto) == type(str()):
            texto = texto.split()#transforma o texto em vetor
        texto.sort(key=len)#ordena o vetor com base na quantidade de letras de cada palavra
        
        #iterador
        for index in range(0,len(texto)):
            try: #Estrutura de Correção de Erro
                
                #Verifica se o tamanho da palavra atual é diferente do tamanho da ultima palavra do vetor
                if len(texto[index])!= len(vetAux[len(vetAux)-1]):
                    #Se Verdadeiro, adiciona o vetor (sem a palavra atual) ao dicionário 
                    vetRetorno[len(vetAux[0])] = vetAux
                    #Dicionário <numero de letras><vetor de palavras>
                    vetAux = list() #resetar o vetor
                    vetAux.append(texto[index]) #adiciona a palavra atual ao vetor
                    
                    
                else:
                    #Se Falso, adiciona a palavra atual ao vetor que possui as palavras do mesmo tamanho
                    vetAux.append(texto[index])
                
                    
            except IndexError: #Se caso o vetor esteja vazio inicia o vetor adicionando um valor
                vetAux.append(texto[index])
                
                
            try:
                #Condicional para gerar um erro proposital
                if len(texto[index]) != len(texto[index+1]):
                    
                    pass
                    
            #Erro proposital para corrigir o problema se caso o vetor com as palavras não tenha sido adicionado ao dicionário 
            except IndexError:
                vetRetorno[len(vetAux[0])] = vetAux
                vetAux = list()
                vetAux.append(texto[index])
                aux = 1
                
        return vetRetorno

    #---------------------------------- FUNÇÃO DE RANQUEAMENTO -----------------------------------------------------------------
    #Função de rankeamento das palavras
    def ranking(listaOrdenada, listaLimpa):
        
        rank = dict() #Variavel que armazena o rank de cada texto
        num = 0
        #estrutura que apenas gera um vetor se caso a variavel que contem as palavras for string
        if type(listaLimpa)== type(str()):
            listaLimpa = listaLimpa.split()
        
        #Iterador sobre a lista de palavras
        for i in listaLimpa:
            
            #Gera o rank de palavras de cada texto
            try:
                #Estrutura do ranking: <Palavras> : <Quantidade no texto>
                rank[i] = listaOrdenada[i[0]][len(i)].count(i)
                
            #Se caso não existir a palavra, não faz nada e evita o Erro   
            except KeyError:
                pass
            
        
        
        return rank 
    
    

    #Ordena texto em ordem alfabetica e armazena em forma de vetor
    textoAlfabetico = ordenacaoAlfabetica(vetorTexto)
    
    
    auxDict = dict()

    #Sessão que ordena cada palavra do vetor que está em ordem alfabetica tambem em ordem numerica
    textoOrganizado = list()
    #Iterador padrão que gera indices
    for indice in range(0,len(textoAlfabetico)):
        auxDict = dict() #reinicia a variavel auxiliar
        #Iterador que gera um letra do alfabeto
        for letra in "abcdefghijklmnopqrstuvwxyz":

            #Gera uma dicionario alfabetico de palavras em ordem numerica
            try:
                auxDict[letra] = ordemNumerico(textoAlfabetico[indice][letra])
                #Estrutura { <Letra do Alfabeto> : {<Numero de caracteres> : [<Vetor de palavras>]} }
                
            except KeyError:
                pass
        try:
            textoOrganizado[indice].append(auxDict)
            
        except IndexError:
            textoOrganizado.append(auxDict)
            
    textoRank = dict()
    i = int()
    for indice in range(0,len(vetorTexto)):
                   
        textoRank[indice+1] = ranking(textoOrganizado[indice], auxVetTexto[indice])
    return textoRank

#------------------------------ FUNÇÃO QUE LIMPA O TEXTO -------------------------------------------------------------
#Funcao que remove todas as pontuações e palavras inuteis e substiui
def cleanText(frase):
    #As Palavras inuteis que vão ser retiradas
    palavrasInuteis = (" tão a à agora ainda alguém algum alguma algumas alguns ampla amplas amplo amplos ante antes ao aos após aquela aquelas aquele aqueles aquilo as até através cada coisa coisas com como contra contudo da daquele daqueles das de dela delas dele deles depois dessa dessas desse desses desta destas deste deste destes deve devem devendo dever deverá deverão deveria deveriam devia deviam disse disso disto dito diz dizem do dos e é ela elas ele eles em enquanto entre era essa essas esse esses esta está estamos estão estas estava estavam estávamos este estes estou eu fazendo fazer feita feitas feito feitos foi for foram fosse fossem grande grandes há isso isto já la lá lhe lhes lo mas me mesma mesmas mesmo mesmos meu meus minha minhas muita muitas muito muitos na não nas nem nenhum nessa nessas nesta nestas ninguém no nos nós nossa nossas nosso nossos num numa nunca o os ou outra outras outro outros para pela pelas pelo pelos pequena pequenas pequeno pequenos per perante pode pude podendo poder poderia poderiam podia podiam pois por porém porque posso pouca poucas pouco poucos primeiro primeiros própria próprias próprio próprios quais qual quando quanto quantos que quem são se seja sejam sem sempre sendo será serão seu seus si sido só sob sobre sua suas talvez também tampouco te tem tendo tenha ter teu teus ti tido tinha tinham toda todas todavia todo todos tu tua tuas tudo última últimas último últimos um uma umas uns vendo ver vez vindo vir vos vós").split()
    fraseSemPoint = str()
    fraseLimpa = str()
    fraseNova = str()
    for i in frase:
        #Remoção das pontuações
        if i not in '"@#$%&*!,/.;:<>-_[]{()})+=-?':
            fraseSemPoint += i
        
    for palavra in fraseSemPoint.split():
        if palavra not in palavrasInuteis:
            fraseLimpa += palavra + " "
        
    for palavra in fraseLimpa:
        for letra in palavra:
            if letra in "ôõóò":
                letra = "o"
            if letra in "áàãâ":
                letra = "a"
            if letra in "úùû":
                letra = "u"
            if letra in "íìî":
                letra = "i"
            if letra in "éèê":
                letra = "e"
            if letra in "ç":
                letra = "c"
            fraseNova += letra
    return fraseNova.lower()       

# -------------------------------- Função de Pesquisa e Resultado -------------------------------------------------
def pesquisa(rankTexto):
    global listaTexto
    def somatorio(rankPalavraTxt, vetorRank):
        for palavra in rankPalavraTxt:
            vetorSoma = list()
            auxSoma = 0

            
            for i in range(0,len(vetorRank)):
                try:
                    auxSoma += ((vetorRank[i][palavra] * 100) / len(rankTexto[palavra].keys()))  
                except KeyError:
                    auxSoma += 0
               
                
                        
         
        return auxSoma
        
    def ordenacaoSoma(vetorSoma, auxInd):
    #Ordenação da soma
        
        
        for j in range(0,len(vetorSoma)):
            for i in range(0,len(vetorSoma)):
                if vetorSoma[j] <= vetorSoma[i]:
                    pass
                else:
                    auxOrg = vetorSoma[j]
                    vetorSoma[j] = vetorSoma[i]
                    vetorSoma[i] = auxOrg
                    auxOrg = auxInd[j]
                    auxInd[j] = auxInd[i]
                    auxInd[i] = auxOrg
        return auxInd
   
       
    vetorRank = list()#armazena a a quantidade de cada palavra em cada texto e os indices de cada texto
    varPesquisa = str(input("Deseja pesquisar que tema? "))
    varPalavra = cleanText(varPesquisa)
    if " " in varPalavra: #verifica se a palavra e composta e explita, gerando uma lista
        varPalavra = varPalavra.split()
    
    #iterador de indice de cada palavra da lista
    for num in range(0,len(varPalavra)):
        auxVet = list() #auxiliar que armazena a quantidade da palavra em cada texto
        auxIndex = list()#auxiliar que armazena os indices dos texto
        auxRank = dict() #auxiliar que armazena a quantidade dessa palavra em relação aos indices do texto
        rankPalavraTxt = list()
        #estrutura que separa os indices do texto 
        for i in range(1,len(rankTexto)+1):
            try:
                auxIndex.append(i) #adiciona os indices do texto no vetor
                auxVet.append(rankTexto[i][varPalavra[num]]) #adiciona a quantidade das palavras no vetor
                
            except KeyError:
                auxVet.append(0) 
            
                    
        #sessão para organizar as palavras, fazer a media de palavras em relação aos texto e imprimir a tabela
                
            
        

        #Cria um dicionario contendo, de forma organizada, cada palavra digitada pelo usuario e sua quantidade no texto
        for i in range(0,len(auxVet)):
            auxRank[auxIndex[i]] = auxVet[i]
        vetorRank.append(auxRank)
    for i in range(1,len(rankTexto)+1):
            
            
        #-------------- SESSÃO A SER TRABALHADA---------------
        vetorIndice = list()
        vetorSoma = list()
        rankPalavraTxt.append(list(i for i in rankTexto[i].keys() if i in varPalavra))
        
    
            
    for num in range(len(varPalavra), 0,-1):
        vetorSoma = []
        auxIndice = []
        
        for i in range(0,len(rankPalavraTxt)):
            if len(rankPalavraTxt[i]) == num:
                vetorSoma.append(somatorio(rankPalavraTxt[i], vetorRank))
                auxIndice.append(auxIndex[i])
        auxIndice = ordenacaoSoma(vetorSoma, auxIndice)
        for indice in auxIndice:
            vetorIndice.append(indice) 
              
    
        
                

            

    print("\n\n\nResultado da Busca de:", varPesquisa)
    for i in range(0, len(vetorIndice)):
        #print(listaTexto[i][:40])       
        print("Texto {}: {}...\n" .format(vetorIndice[i],listaTexto[i][:300]))



#Criar uma func\o que ordena os valores e chaves de dicionarios
listaTexto = lerArquivos("textos/texto",".txt",4)



#poe o texto todo em maiusculo
#textoMaiusculo = [i.upper() for i in listaTexto]

#Remove as palavras lixo do texto
textoLimpo = list()
#Remove as pontuacoes e as palavras lixos e cria um texto sem pontuação e todo em minusculo
for i in listaTexto:
    textoLimpo.append(cleanText(i.lower()))


rankTexto = rankingWords(textoLimpo) #Funçaõ que ordena e rankea






#Sessao de pesquisa das palavras
cond = str(input("Deseja pesquisar textos? (sim/não)\n"))
cond.lower()

while(cond == "sim"):
    
    pesquisa(rankTexto)

    cond = str(input("\nDeseja continuar pesquisando textos? (sim/não)\n"))
