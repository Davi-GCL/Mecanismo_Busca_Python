# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session

#Funcao para retirar toda as pontucoes de cada texto armazenado em 'textos'
def limparTextos(textos,ponts):
  auxiliar = str()
  
  for k in range(0,len(textos)):
    for i in ponts:
        for j in textos[k]:
            if j != i:
                auxiliar += j
        
        textos[k] = auxiliar
        auxiliar = ""

  return textos

#Funcao para ler os textos presentes no arquivo, e armazena cada texto(arquivo) em uma posicao da lista
def lerArquivos(caminho: str, formato: str, qntArq: int):
  textos = []
  for i in range (1,qntArq+1):   
      arqNome = str(caminho) + str(i) + str(formato) #Concatena com o numero indice para formar o caminho com nome de cada arquivo de texto: "texto1.txt"

      with open(arqNome, "r", encoding="UTF-8") as arquivo: #A funcao open retorna um objeto do tipo manipulador de arquivo, atribuindo ao 'arquivo'
                                                            #Recebe como parametro o caminho e nome do arquivo(se nao for encontrado, sera criado um).
                                                            #'r' = Permite leitura do arquivo
          textos.append(str(arquivo.readlines()))

  return textos #Retorna os textos brutos (sem nenhuma filtrar)
#

#Funcao para gerar o resumo de cada texto (previa que sera exibida em baixo do link no front end)
def gerarResumos(textos:list,tamanho:int):
  ponts = [",",".","!","?","(",")","[","]","{","}","-",":",";","'","\"","\n"]
  textos = limparTextos(textos, ponts)
  aux = str()
  resumos = []
  for i in range (0, len(textos)):
    palavras = textos[i].split()
    for j in range(0,tamanho):
      aux += " " + palavras[j]
    
    resumos.append(aux + "...")
    aux = ""

  return resumos
  
textos_bruto = lerArquivos("textos/texto",".txt",4)
textos_palavras = []

resumos = gerarResumos(textos_bruto,27)

"""#Armazena em cada posicao uma lista, com as palavras separadas, de cada texto 
for i in range(len(textos_bruto)):
    textos_palavras.append(textos_bruto[i].split())

print(textos_palavras[0])"""

#Comando exigido na documentacao do framework flask 
app = Flask(__name__)

#Criando uma pagina como o flask
#route => endereço da sua pagina(dominio da pagina): '/' para home page
#funcao => o que sera exibido naquela pagina

#necessario definir uma chave secreta para permitir a comunicao entre paginas
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods = ["GET","POST"]) #decorator: '@' serve para atribuir uma nova funcionalidade a funcao que esta logo abaixo (exibir conteudo da funcao na pagina do link informado)
def indexpage():
  entrada = None
  entrada = request.form.get("pesquisa") 
  session["pesquisa"] = request.form["pesquisa"]

  #Quando o formulario for preenchido, redireciona para outra pagina(funcao)
  if entrada != None:
    return redirect(url_for('resultados1'))

  return render_template("index.html", entrada = entrada)
  

@app.route("/resultados1") #decorator: '@' com o link da pagina resultados
def resultados1():
  
  return render_template("resultados1.html", resultados = session["pesquisa"])

#Coloca o site no ar
if __name__ == "__main__": #Importante para evitar erros durante a hospedagem do site
  app.run(debug=True)

