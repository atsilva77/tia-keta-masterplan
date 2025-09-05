import streamlit as st
import pandas as pd

# Nome do ficheiro Excel
excel_file = "Plano_Recolha_Dados_Master_Plan_Luanda_v5a.xlsx"

# Carregar todas as folhas do Excel
sheets = pd.read_excel(excel_file, sheet_name=None, engine='openpyxl')

# Título da aplicação
st.set_page_config(page_title="Plano de Recolha de Dados - Luanda", layout="wide")
st.title("📊 Plano de Recolha de Dados - Luanda")

# Menu lateral para seleção da folha
sheet_names = list(sheets.keys())
selected_sheet = st.sidebar.selectbox("Seleciona a folha para explorar:", sheet_names)

# Carregar dados da folha selecionada
df = sheets[selected_sheet]

# Mostrar dados com base na folha selecionada
st.subheader(f"📄 Dados da folha: {selected_sheet}")

# Filtros interativos para folhas específicas
if selected_sheet == "Plano_Recolha":
    col1, col2, col3 = st.columns(3)
    with col1:
        area = st.multiselect("Área de Interesse Principal", options=df["Área de Interesse Principal"].dropna().unique())
    with col2:
        formato = st.multiselect("Formato", options=df["Formato"].dropna().unique())
    with col3:
        responsavel = st.multiselect("Responsável", options=df["Responsável"].dropna().unique())

    if area:
        df = df[df["Área de Interesse Principal"].isin(area)]
    if formato:
        df = df[df["Formato"].isin(formato)]
    if responsavel:
        df = df[df["Responsável"].isin(responsavel)]

elif selected_sheet == "Noticias_Incidentes":
    local = st.multiselect("Local Referido", options=df["Local Referido"].dropna().unique())
    if local:
        df = df[df["Local Referido"].isin(local)]

# Mostrar tabela com links clicáveis se houver coluna de links
def make_clickable(val):
    if pd.notna(val) and isinstance(val, str) and val.startswith("http"):
        return f'<a href="{val}" target="_blank">🔗 Link</a>'
    return val

if "Link" in df.columns:
    df["Link"] = df["Link"].apply(make_clickable)
if "Link para Consulta" in df.columns:
    df["Link para Consulta"] = df["Link para Consulta"].apply(make_clickable)
if "link oficial" in df.columns:
    df["link oficial"] = df["link oficial"].apply(make_clickable)

# Mostrar tabela com estilo
st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
