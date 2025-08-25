import re

def extract_dates(text):
    """Extrai todas as datas no formato dd/mm/aaaa"""
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(date_pattern, text)
    return dates

def extract_values(text):
    """Extrai valores em reais no formato R$ 1.234,56"""
    value_pattern = r'R\$\s?[\d\.,]+'
    values = re.findall(value_pattern, text)
    return values

def extract_parties_regex(text):
    """Extrai todas as partes do contrato (CONTRATANTE e CONTRATADA) ignorando CNPJ e endereço"""
    # Limpar quebras de linha e múltiplos espaços
    text_clean = re.sub(r'\s+', ' ', text)

    # Regex para pegar nomes das empresas antes de "inscrita no CNPJ" ou "doravante denominada"
    pattern = r'a empresa\s+(.+?)(?:, inscrita no CNPJ|, doravante denominada (?:CONTRATANTE|CONTRATADA))'

    # Encontrar todas as ocorrências
    parties = re.findall(pattern, text_clean, re.IGNORECASE)

    # Remover espaços extras
    parties = [p.strip() for p in parties]

    return parties


def extract_contract_data(text):
    """Função principal que retorna os dados extraídos em JSON"""
    data = {
        "partes": extract_parties_regex(text),
        "datas": extract_dates(text),
        "valores": extract_values(text)
    }
    return data

# Teste rápido
if __name__ == "__main__":
    with open("samples/contrato1.txt", "r", encoding="utf-8") as f:
        text = f.read()

    result = extract_contract_data(text)
    print(result)
