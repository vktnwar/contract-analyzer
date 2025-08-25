# Contrato-Analyzer

Uma aplicação web profissional para **análise inteligente de contratos**, utilizando OCR e NLP para extrair automaticamente **partes, datas e valores** de contratos em PDF e TXT.

## ✨ Características

* 📄 Processamento de contratos em **PDF e TXT**
* 🤖 **Extração automática de dados** (partes, datas, valores)
* 📊 Indicadores e gráficos automáticos para rápida análise
* 💾 **Download individual ou consolidado** dos relatórios
* 🌐 Interface web simples e intuitiva com **Streamlit**
* ⚡ Leve e rápido, sem necessidade de infraestrutura complexa

## 🚀 Instalação

### Opção 1: Clonar e executar localmente

```bash
git clone https://github.com/seu-usuario/contract-analyzer
cd contract-analyzer
pip install -r requirements.txt
streamlit run app.py
```

### Opção 2: Executar diretamente no Codespaces ou outro ambiente

```bash
git clone https://github.com/seu-usuario/contract-analyzer
cd contract-analyzer
pip install -r requirements.txt
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## 📖 Uso

1. Acesse a aba **📤 Upload** e faça upload dos seus contratos (PDF ou TXT)
2. Confira o **texto extraído** na aba **📑 Texto Extraído**
3. Veja **resumos, indicadores e gráficos** na aba **🗂 Dados Extraídos**
4. Baixe os **relatórios individuais ou consolidados** na aba **⬇️ Download**

## ⚙️ Funcionalidades principais

| Funcionalidade  | Descrição                                                |
| --------------- | -------------------------------------------------------- |
| Upload múltiplo | Suporte para múltiplos contratos de uma vez              |
| OCR inteligente | Extrai texto de PDFs de forma confiável                  |
| NLP             | Identifica partes, datas e valores automaticamente       |
| Indicadores     | Total de contratos, valores totais, vencimentos próximos |
| Gráficos        | Valores por contrato em gráfico de barras                |
| Download        | Relatórios individuais ou consolidados em TXT            |

## 💡 Exemplos de uso

### Upload de contratos

* PDF com contrato de prestação de serviços
* TXT com contrato de fornecimento

### Visualização

* Indicadores no topo: total de contratos, valores totais, vencimentos próximos
* Gráficos de barras com valores por contrato
* Cards individuais mostrando dados extraídos

### Download

* Relatório individual: `relatorio_contrato1.txt`
* Relatório consolidado: `relatorio_consolidado.txt`

## 🧪 Teste

```bash
# Teste básico
streamlit run app.py

# Teste avançado
# Faça upload de múltiplos contratos e veja os gráficos e indicadores

# Teste de integridade
# Baixe os relatórios e confira se os dados extraídos estão corretos
```

## 📋 Requisitos

* Python 3.10 ou superior
* Streamlit
* pytesseract
* pdf2image
* spacy (`pt_core_news_sm`)
* plotly
* fpdf

## 🛠️ Desenvolvimento

```bash
# Clonar repositório
git clone https://github.com/seu-usuario/contract-analyzer
cd contract-analyzer

# Executar em modo desenvolvimento
streamlit run app.py

# Testar o extract.py isoladamente
python utils/extract.py
```

## 📄 Licença

MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

## 🚧 Próximas Funcionalidades

* [ ] Extração de cláusulas específicas (rescisão, multa, prazo)
* [ ] Exportar relatórios em PDF com layout profissional
* [ ] Dashboard com filtros por data, valor ou partes
* [ ] Integração com bases externas de contratos para validação automática
* [ ] Alertas automáticos de vencimento por e-mail

