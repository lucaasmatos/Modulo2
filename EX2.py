from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

mascara = "-----------------------------------------\nId: {0}\n\n Nome: {1}\n\n Sexo: {2}\n\n"

for dep in list_dep.deputados():    
    id   = dep['id']
    nome = dep['nome']

    infodep = list_dep.deputado_id(id)  

    if(infodep['sexo'] =="F"):
      print(mascara.format(id, nome, infodep['sexo']))

