from  lib.scrapy_dadosAbertos import DadosAbertos

list_dep = DadosAbertos()

mascara = "-----------------------------------------\n Id: {0}\n\n Nome: {1}\n\n Total de Despesa: {2}\n\n"

valorTotal = 0

for dep in list_dep.deputados()[1:2]:    
    id   = dep['id']
    nome = dep['nome']
    
    for infdep in list_dep.deputado_despesas(id):  
      valorTotal = valorTotal + infdep['valorDocumento']

    print(mascara.format(id, nome,round(valorTotal,2)))