import streamlit as st
import pytesseract
from pdf2image import convert_from_path
import tempfile
import json
import pandas as pd
import plotly.express as px
from datetime import datetime

from utils.extract import extract_contract_data

# Configuração da página
st.set_page_config(page_title="Contract Analyzer", layout="wide")
st.title("📄 Contract Analyzer")

# Criação de abas
tabs = st.tabs(["📤 Upload", "📑 Texto Extraído", "🗂 Dados Extraídos", "⬇️ Download"])

# --- Aba 1: Upload ---
with tabs[0]:
    st.header("📤 Upload de Contratos")
    uploaded_files = st.file_uploader(
        "Faça upload de um ou mais contratos em PDF ou TXT",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

all_texts = {}
all_data = {}

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        file_type = file_name.split('.')[-1].lower()
        full_text = ""

        if file_type == "pdf":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

            st.info(f"Processando PDF: {file_name}")
            images = convert_from_path(tmp_path)
            for i, img in enumerate(images):
                st.image(img, caption=f"Página {i+1}", use_container_width=True)
                text = pytesseract.image_to_string(img, lang="por")
                full_text += f"\n\n--- Página {i+1} ---\n{text}"

        elif file_type == "txt":
            st.info(f"Lendo TXT: {file_name}")
            full_text = uploaded_file.read().decode("utf-8")

        # Armazenar texto completo
        all_texts[file_name] = full_text
        # Extrair dados
        all_data[file_name] = extract_contract_data(full_text)

# --- Aba 2: Texto Extraído ---
with tabs[1]:
    st.header("📑 Textos dos Contratos")
    if all_texts:
        for file_name, text in all_texts.items():
            st.subheader(f"📄 {file_name}")
            st.text_area("Texto completo", text, height=200)
            st.markdown("---")
    else:
        st.info("Faça upload de arquivos para ver o texto aqui.")

# --- Aba 3: Dados Extraídos com Indicadores ---
with tabs[2]:
    st.header("🗂 Resumo dos Dados Extraídos")

    if all_data:
        # --- Indicadores ---
        total_contracts = len(all_data)
        total_values = 0
        upcoming_contracts = 0
        today = datetime.today()

        value_list = []
        contract_names = []

        for file_name, data in all_data.items():
            contract_names.append(file_name)
            # Somar valores
            valores = data.get("valores", [])
            for v in valores:
                try:
                    clean_v = float(v.replace("R$", "").replace(".", "").replace(",", "."))
                except:
                    clean_v = 0.0
                total_values += clean_v
                value_list.append(clean_v)

            # Checar datas próximas de vencimento
            datas = data.get("datas", [])
            for d in datas:
                try:
                    dt = datetime.strptime(d, "%d/%m/%Y")
                    if 0 <= (dt - today).days <= 30:
                        upcoming_contracts += 1
                except:
                    continue

        col1, col2, col3 = st.columns(3)
        col1.metric("📄 Contratos processados", total_contracts)
        col2.metric("💰 Total de valores (R$)", f"{total_values:,.2f}")
        col3.metric("⏰ Vencimento próximos 30 dias", upcoming_contracts)

        st.markdown("---")

        # --- Gráfico de barras: valores por contrato ---
        df_chart = pd.DataFrame({
            "Contrato": contract_names,
            "Valor": value_list[:len(contract_names)]  # Considerando 1 valor principal por contrato
        })
        fig = px.bar(df_chart, x="Contrato", y="Valor", text="Valor", labels={"Valor": "Valor (R$)"})
        st.plotly_chart(fig, use_container_width=True)

        # --- Cards individuais ---
        for file_name, data in all_data.items():
            st.markdown(f"""
            <div style="
                display:block;
                background-color:#f0f4f8;
                padding:20px;
                border-radius:10px;
                margin-bottom:15px;
                color:#000000;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            ">
                <h4>📄 {file_name}</h4>
                <p><strong>👥 Partes:</strong> {', '.join(data.get('partes', []))}</p>
                <p><strong>🗓 Datas:</strong> {', '.join(data.get('datas', []))}</p>
                <p><strong>💰 Valores:</strong> {', '.join(data.get('valores', []))}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Os dados extraídos aparecerão aqui após o upload e processamento.")

# --- Aba 4: Download ---
with tabs[3]:
    st.header("⬇️ Download dos Relatórios")
    if all_texts and all_data:
        for file_name in all_texts.keys():
            report_content = f"TEXTO DO CONTRATO:\n{all_texts[file_name]}\n\nDADOS EXTRAÍDOS:\n{json.dumps(all_data[file_name], ensure_ascii=False, indent=2)}"
            st.download_button(
                f"⬇️ Baixar relatório: {file_name}",
                report_content,
                file_name=f"relatorio_{file_name}.txt"
            )

        # Relatório consolidado
        consolidated = ""
        for file_name in all_texts.keys():
            consolidated += f"--- {file_name} ---\n"
            consolidated += f"{all_texts[file_name]}\n\nDADOS EXTRAÍDOS:\n"
            consolidated += f"{json.dumps(all_data[file_name], ensure_ascii=False, indent=2)}\n\n"

        st.download_button(
            "⬇️ Baixar relatório consolidado de todos os contratos",
            consolidated,
            file_name="relatorio_consolidado.txt"
        )
    else:
        st.info("O relatório estará disponível após o upload e processamento dos contratos.")
