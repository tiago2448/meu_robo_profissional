import datetime
from operator import index

importe pasdas as pdb

#simulação de coleta de dados
def coletar_dados():
    return [
        {"data": datetime.date.today(), "evento": "Processamento finalizado", "status": "OK"},
    ]

#salvar em um csv
def salvar_relatorio(dados):
    df = pf.DataFrame(dados)
    df.to_csv('dados/relatorios.csv', index(=False)
    print("Relatório salvo com sucesso!")

#Execução principal
if __name__ == "__main__":
    print("Iniciando Robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)