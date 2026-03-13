# -*- coding: utf-8 -*-
import streamlit as st
from datetime import date
import pandas as pd

# 1. Configuração da página
st.set_page_config(
    page_title="Caio Fukushima | Product & Eng. Tech", 
    page_icon="🏗️", 
    layout="wide"
)

# 2. Estilo CSS - Foco em Profissionalismo e Tecnologia
st.markdown("""
    <style>
        [data-testid="stSidebar"] { background-color: #0A192F !important; }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        [data-testid="stMetricValue"] { color: #CDA434 !important; }
        .stButton>button {
            width: 100% !important;
            border-radius: 10px !important;
            background-color: #CDA434 !important;
            color: white !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CÁLCULOS ---
data_formatura = date(2026, 12, 1) 
hoje = date.today()
dias_faltantes = (data_formatura - hoje).days

# --- BARRA LATERAL ---
st.sidebar.title("Navegação")
st.sidebar.metric(label="Dias para Formatura", value=f"{dias_faltantes}")
st.sidebar.write("---")

aba = st.sidebar.radio("Ir para:", [
    "Perfil Profissional", 
    "Data Science & Engenharia", 
    "Pesquisa e Sinais (TCC)", 
    "Portfólio GitHub"
])

# --- ABA 1: PERFIL (Focado em Product Analyst na AltoQI) ---
if aba == "Perfil Profissional":
    st.title("🏗️ Caio Fukushima")
    st.subheader("Engenheiro Civil & Desenvolvedor de Soluções Tech")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("📸 [Espaço para Foto Profissional]")
    
    with col2:
        st.write("""
        Sou um entusiasta da tecnologia aplicada à construção. Meu diferencial é a capacidade de unir 
        o conhecimento técnico da Engenharia Civil com o poder da análise de dados e automação em Python.
        
        Busco atuar na intersecção entre engenharia e desenvolvimento de software, ajudando a criar 
        ferramentas que tornem o trabalho do engenheiro mais eficiente e orientado a dados.
        """)
        st.success("🎯 Foco: Product Analyst | Inteligência em Software para Engenharia")

    st.write("---")
    st.subheader("🛠️ Minha Stack Tecnológica")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Engenharia**")
        st.caption("BIM (Eberick e QiBuilder), Projetos Estruturais, Alvenaria Estrutural.")
    with c2:
        st.markdown("**Desenvolvimento**")
        st.caption("Python (Scripts de Automação), Streamlit (Dashboards), Lógica de Produto.")
    with c3:
        st.markdown("**Dados**")
        st.caption("Pandas, Visualização de Dados, Análise de Requisitos técnicos.")

# --- ABA 2: DATA SCIENCE ---
elif aba == "Data Science & Engenharia":
    st.title("📊 Análise de Dados e Automação")
    st.write("Abaixo, um exemplo de como utilizo Python (Pandas) para gerenciar informações de projeto de forma dinâmica:")
    
    data = {
        'Insumo': ['Cimento', 'Aço CA-50', 'Areia', 'Brita'],
        'Quantidade': [500, 1200, 45, 38],
        'Status': ['Entregue', 'Pendente', 'Entregue', 'Atrasado']
    }
    df = pd.DataFrame(data)
    st.table(df) 
    st.info("💡 Soluções como esta reduzem erros manuais em orçamentos e cronogramas.")

# --- ABA 3: TCC (Sem erro de iPhone) ---
elif aba == "Pesquisa e Sinais (TCC)":
    st.title("🎓 Pesquisa e Engenharia Diagnóstica")
    st.write("**Detecção de Danos Estruturais via Análise de Vibração**")
    
    st.write("""
    Neste projeto, utilizei sensores acelerômetros para coletar dados de vibração em estruturas. 
    O grande desafio foi a criação de um algoritmo em Python capaz de processar esses sinais e 
    identificar padrões de falha.
    """)
    
    st.subheader("📐 Metodologia Tech:")
    st.write("""
    Apliquei a **Transformada de Fourier** para converter os dados brutos (tempo) em frequências. 
    Isso permite identificar se a 'assinatura' da estrutura mudou, indicando uma possível patologia.
    """)
    
    st.info("Nota: Este projeto demonstra minha competência em transformar dados complexos em insights acionáveis.")

# --- ABA 4: GITHUB ---
elif aba == "Portfólio GitHub":
    st.title("💻 Meu Código")
    st.write("Acompanhe meus estudos e projetos de automação:")
    # Lembre-se de trocar 'seu-usuario' pelo seu nome real do GitHub
    st.markdown("### [🔗 Acessar meu GitHub](https://github.com/caiofukushima)")

# --- RODAPÉ ---
st.write("---")
st.markdown("📍 Dracena - SP | 📩 **Contato:** [caio.fukushima@exemplo.com](mailto:caio.fukushima@exemplo.com)")
