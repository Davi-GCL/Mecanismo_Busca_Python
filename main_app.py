# -*- coding: iso-8859-1 -*-
from flask import Flask, render_template, request, redirect, url_for, session
from funcoes.funcoes import*

dados_entrada = None
listaTexto = lerArquivos("textos/texto",".txt",0,20)
indicesTextos = []

resumos = gerarResumos(listaTexto,27)


#poe o texto todo em maiusculo
#textoMaiusculo = [i.upper() for i in listaTextos]

#Remove as palavras lixo do texto
textoLimpo = list()

#Remove as pontuacoes e as palavras lixos e cria um texto sem pontua��o e todo em minusculo
for i in listaTexto:
    textoLimpo.append(cleanText(i.lower()))


rankTexto = rankingWords(textoLimpo) #Fun�a� que ordena e ranqueia




#Comando exigido na documentacao do framework flask 
app = Flask(__name__)

#Criando uma pagina como o flask
#route => endere�o da sua pagina(dominio da pagina): '/' para home page
#funcao => o que sera exibido naquela pagina
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#url_for: vai para aonde o redirect indica



# -------------------------------- Funcao da Pagina Principal de Pesquisa -------------------------------------------------
@app.route("/", methods = ["GET","POST"]) #decorator: '@' serve para atribuir uma nova funcionalidade a funcao que esta logo abaixo (configuração da rota para index.)
def indexpage():

  global indicesTextos
  global dados_entrada
  dados_entrada = request.form.get("pesquisa") 

  #Quando o formulario for preenchido,executa o ranqueamento e redireciona para outra pagina(funcao)
  if dados_entrada != None and dados_entrada != " ":
    #Funcao que realiza a pesquisa e organiza a lista 'rankTexto' de acordo com a relavancia relativa a frase digitada pelo usuario 'dados entrada' e retorna uma colecao com os indices relativos dos textos ranqueados
    indicesTextos = pesquisa(dados_entrada, rankTexto)
    
    return redirect(url_for('resultados'))

  return render_template("index.html", entrada = dados_entrada)
#  


# -------------------------------- Funcao da primeira tela com os resultados da pesquisa -------------------------------------------------
@app.route("/resultados/1", defaults={"pagina_num":1}, methods = ["GET","POST"]) #decorator: '@' com a rota da pagina resultados
@app.route("/resultados/<int:pagina_num>", methods = ["GET","POST"]) #decorator: '@' com o link da pagina resultados #decorator: '@' com o link da pagina resultados
def resultados(pagina_num):
  
  global dados_entrada
  global resumos
  global indicesTextos
  gruposIndices = [1,2]

  #Separa 50% dos textos para cada pagina a ser exibida
  if len(indicesTextos) > 5:
    j = int(len(indicesTextos) * 0.5)
    gruposIndices[0] = indicesTextos[:j]
    gruposIndices[1] = indicesTextos[j:]


  if dados_entrada != None:

    return render_template("resultados.html", resumos = resumos, pagina_num= pagina_num , gruposIndices = gruposIndices)

  else:
    return render_template("resultadoInvalido.html")
#


# -------------------------------- Funcao que gera a pagina de cada texto -------------------------------------------------
@app.route("/textos/<texto_link>") #O que sera escrito no link dinamico serve como parametro para a funcao
def pagina_texto(texto_link):
  global listaTexto
  aux = int(texto_link[5:])


  try:
    return listaTexto[aux]
  except:
    return "PAGINA NAO ENCONTRADA"
#

#Coloca o site no ar
if __name__ == "__main__": #Importante para evitar erros durante a hospedagem do site
  app.run(debug=True)

