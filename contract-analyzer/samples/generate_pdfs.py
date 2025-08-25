from fpdf import FPDF

# Dados dos contratos
contracts = {
    "contrato2": """
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

Pelo presente instrumento particular, de um lado, a empresa
GammaTech Soluções Ltda, inscrita no CNPJ 22.333.444/0001-66,
com sede na Rua das Acácias, 789, Belo Horizonte/MG, doravante denominada CONTRATANTE,
e de outro lado, a empresa
DeltaSoft Tecnologia Ltda, inscrita no CNPJ 77.888.999/0001-11,
com sede na Avenida Paulista, 1234, São Paulo/SP, doravante denominada CONTRATADA,
resolvem celebrar o presente Contrato de Prestação de Serviços.

Cláusula 1 – Objeto
Prestação de serviços de consultoria em tecnologia da informação.

Cláusula 2 – Prazo
O contrato terá início em 15/10/2025 e término em 15/04/2026.

Cláusula 3 – Valor e forma de pagamento
O valor total do contrato é de R$ 80.000,00, pagos em 4 parcelas mensais de R$ 20.000,00 cada.

Cláusula 4 – Rescisão
Em caso de descumprimento, a parte prejudicada poderá rescindir o contrato mediante aviso prévio de 30 dias.

Cláusula 5 – Foro
Foro da Comarca de Belo Horizonte/MG.

Belo Horizonte, 15 de outubro de 2025.

_________________________           _________________________
GammaTech Soluções Ltda              DeltaSoft Tecnologia Ltda
""",
    "contrato3": """
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

Pelo presente instrumento particular, de um lado, a empresa
Epsilon Serviços Ltda, inscrita no CNPJ 33.444.555/0001-77,
com sede na Rua das Palmeiras, 456, Curitiba/PR, doravante denominada CONTRATANTE,
e de outro lado, a empresa
Zeta Solutions Ltda, inscrita no CNPJ 88.999.000/0001-22,
com sede na Avenida Central, 321, Porto Alegre/RS, doravante denominada CONTRATADA,
resolvem celebrar o presente Contrato de Prestação de Serviços.

Cláusula 1 – Objeto
Serviços de manutenção e atualização de sistemas de software.

Cláusula 2 – Prazo
O contrato terá início em 01/11/2025 e término em 30/06/2026.

Cláusula 3 – Valor e forma de pagamento
O valor total do contrato é de R$ 120.000,00, pagos em 6 parcelas mensais de R$ 20.000,00 cada.

Cláusula 4 – Rescisão
Rescisão mediante descumprimento com aviso prévio de 30 dias.

Cláusula 5 – Foro
Foro da Comarca de Curitiba/PR.

Curitiba, 01 de novembro de 2025.

_________________________           _________________________
Epsilon Serviços Ltda              Zeta Solutions Ltda
"""
}

# Função para limpar caracteres Unicode problemáticos
def clean_text(text):
    replacements = {
        "–": "-",  # travessão
        "—": "-",  # travessão longo
        "“": '"',  # aspas curvas
        "”": '"',
        "‘": "'",
        "’": "'"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

# Função para gerar PDF
def create_pdf(text, filename):
    text = clean_text(text)  # Limpeza Unicode
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.strip().split("\n"):
        pdf.multi_cell(0, 8, line)
    pdf.output(filename)
    print(f"PDF gerado: {filename}")

# Gerar PDFs
for name, text in contracts.items():
    create_pdf(text, f"{name}.pdf")
