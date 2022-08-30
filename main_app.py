# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session
from funcoes.funcoes import*

textos_bruto = lerArquivos("textos/texto",".txt",4)
textos_palavras = []

resumos = gerarResumos(textos_bruto,27)


#Comando exigido na documentacao do framework flask 
app = Flask(__name__)

#Criando uma pagina como o flask
#route => endereço da sua pagina(dominio da pagina): '/' para home page
#funcao => o que sera exibido naquela pagina



# -------------------------------- Funcao da Pagina Principal de Pesquisa -------------------------------------------------
@app.route("/", methods = ["GET","POST"]) #decorator: '@' serve para atribuir uma nova funcionalidade a funcao que esta logo abaixo (exibir conteudo da funcao na pagina do link informado)
def indexpage():
  entrada = None
  entrada = request.form.get("pesquisa") 
  #session["pesquisa"] = request.form["pesquisa"]
  try:
    with open("pesquisa.txt","w+",encoding="UTF-8") as escritor:
      escritor.writelines(entrada)
      escritor.seek(0)
  except:  
    entrada = "placeholder"

  #Quando o formulario for preenchido, redireciona para outra pagina(funcao)
  if entrada != None and entrada != "placeholder":
    return redirect(url_for('resultados1'))

  return render_template("index.html", entrada = entrada)
#  


# -------------------------------- Funcao da primeira tela com os resultados da pesquisa -------------------------------------------------
@app.route("/resultados1") #decorator: '@' com o link da pagina resultados
def resultados1():
  
  with open("pesquisa.txt","r",encoding="UTF-8") as leitura:
    dados = leitura.readline()
    leitura.seek(0)

  return render_template("resultados1.html", resultados = dados)
#


# -------------------------------- Funcao que gera a pagina de cada texto -------------------------------------------------
@app.route("/resultados1/<texto_link>") #O que sera escrito no link dinamico serve como parametro para a funcao
def pagina_texto(texto_link):
  try:
    return texto_link
  except:
    return "PAGINA NAO ENCONTRADA"

#Coloca o site no ar
if __name__ == "__main__": #Importante para evitar erros durante a hospedagem do site
  app.run(debug=True)

