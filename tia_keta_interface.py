
import pandas as pd
import streamlit as st

excel_file = "Plano_Recolha_Dados_Master_Plan_Luanda_v05.xlsx"
df = pd.read_excel(excel_file, sheet_name="1 - Plano_Recolha", engine="openpyxl")

st.set_page_config(page_title="Agente Tia Keta", layout="wide")
st.title("👵🏽 Agente Tia Keta - Recolha de Dados para o Master Plan de Luanda")
st.markdown("Bem-vindo à interface da Tia Keta! Aqui podes explorar os documentos disponíveis para cada área de interesse. Filtra, consulta e identifica o que ainda falta recolher. Vamos lá, meu filho! 💪🏽")

areas = df["Área de Interesse Principal"].dropna().unique()
selected_area = st.sidebar.selectbox("Escolhe a área de interesse:", ["Todas"] + list(areas))

if selected_area != "Todas":
    filtered_df = df[df["Área de Interesse Principal"] == selected_area]
else:
    filtered_df = df

for idx, row in filtered_df.iterrows():
    st.subheader(f"📌 {row['Tipo de Dado']}")
    st.markdown(f"**Área:** {row['Área de Interesse Principal']}")
    st.markdown(f"**Fonte:** {row['Fonte']}")
    st.markdown(f"**Formato:** {row['Formato']}")
    st.markdown(f"**Responsável:** {row['Responsável']}")
    st.markdown(f"**Observações:** {row['Observações']}")
    
    if pd.notna(row['Link']):
        st.markdown(f"[🔗 Ver Documento]({row['Link']})")
    else:
        st.markdown("🚨 **Link em falta! Tia Keta ainda não encontrou este documento.**")

    st.markdown("---")
