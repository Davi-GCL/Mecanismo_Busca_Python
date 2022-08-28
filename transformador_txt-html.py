textos = []
textos_palavras = []

#Algoritmo para ler os textos presentes no arquivo, e armazena cada texto(arquivo) em uma posicao da lista
for i in range (1,5):   
    arqNome = "textos/texto" + str(i) + ".txt" #Concatena com o numero indice para formar o caminho com nome de cada arquivo de texto
    novoArqNome = "textos/texto" + str(i) + ".html"

    with open(arqNome, "r", encoding="UTF-8") as arquivo:
        #Algoritmo para criar arquivos .html
        aux = open(novoArqNome, "w+", encoding="utf-8") #A funcao open retorna um objeto do tipo manipulador de arquivo, atribuindo ao 'aux'
        #Recebe como parametro o caminho e nome do arquivo(se nao for encontrado, sera criado um).
        #'w+' = Permite leitura, atualizacao e criacao do arquivo

        aux.writelines(arquivo) #Escreve o texto do documento lido(atribuido a 'arquivo') na nova pagina criada    

