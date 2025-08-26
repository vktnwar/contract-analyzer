FROM python:3.10-slim

# Instalar dependências do sistema para OCR
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-por \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baixar modelo spaCy
RUN python -m spacy download pt_core_news_sm

# Copiar código da aplicação
COPY . .

# Expor porta do Streamlit
EXPOSE 8501

# Comando para iniciar
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]