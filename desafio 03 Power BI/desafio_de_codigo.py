def identificar_termo_bi(termo):
    if termo == "ETL":
        return "Processo de extrair, transformar e carregar dados de diversas fontes."
    elif termo == "Data Warehousing":
        return "Armazenamento centralizado de dados para análise e relatórios."
    elif termo == "Dashboard":
        return "Ferramenta visual para monitoramento e análise de métricas."
    elif termo == "Data Mining":
        return "Descoberta de padrões e insights em grandes conjuntos de dados."
    else:
        return "Termo não reconhecido"

entrada = input()

print(identificar_termo_bi(entrada))

# Função responsável por receber um conceito de ETL e retornar sua descrição.
def identificar_conceito_etl(conceito):
    if conceito == "Extract":
        return "Processo de coletar dados de diversas fontes."
    elif conceito == "Transform":
        return "Processo de converter dados para um formato adequado."
    elif conceito == "Load":
        return "Carregamento de dados transformados em banco de dados ou warehouse."
    elif conceito == "Data Integration":
        return "Unificação de dados provenientes de múltiplas fontes."
    else:
        return "Conceito não reconhecido"

entrada = input()

print(identificar_conceito_etl(entrada))