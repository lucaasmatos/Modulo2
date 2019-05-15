from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

mascara = "\nId: {0}\n\nURI: {1}\n\nSigla: {2}\n\nNome: {3}\n\nApelido: {4}\n\nCodigo Orgão: {5}\n\nTipo Orgão: {6}\n\n"   
for comissao in list_dep.orgaos(): 
  if(comissao['sigla'] == "PEC57402"):  
     print(mascara.format(comissao['id'], comissao['uri'], comissao['sigla'], comissao['nome'], comissao['apelido'], comissao['codTipoOrgao'], comissao['tipoOrgao']))