# -*- coding: utf-8 -*-
import streamlit as st
from datetime import date
import pandas as pd

# 1. Configuração da página
st.set_page_config(
    page_title="Caio Fukushima | Eng. Civil & Python", 
    page_icon="🐍", 
    layout="wide"
)

# 2. Estilo CSS
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

# --- ABA 1: PERFIL ---
if aba == "Perfil Profissional":
    st.title("🏗️ Caio Fukushima")
    st.subheader("Engenheiro Civil & Desenvolvedor de Soluções Tech")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("📸 [Espaço para Foto]")
    
    with col2:
        st.write("""
        Diferente do engenheiro tradicional, meu foco é a automação e digitalização da construção. 
        Utilizo Python para criar fluxos de trabalho inteligentes e precisos.
        """)
        st.success("🎯 Objetivo: Trainee em Inovação ou Gestão de Dados (BIM/VDC).")

# --- ABA 2: DATA SCIENCE ---
elif aba == "Data Science & Engenharia":
    st.title("📊 Manipulação de Dados")
    data = {
        'Insumo': ['Cimento', 'Aço', 'Areia', 'Brita'],
        'Quantidade': [500, 1200, 45, 38],
        'Status': ['Entregue', 'Pendente', 'Entregue', 'Atrasado']
    }
    df = pd.DataFrame(data)
    st.table(df) 
    st.info("💡 Automação de extração de dados e relatórios gerenciais.")

# --- ABA 3: TCC (VERSÃO SEM ERROS) ---
elif aba == "Pesquisa e Sinais (TCC)":
    st.title("🎓 Pesquisa Técnica")
    st.write("**Detecção de Danos via Análise de Vibração**")
    
    st.write("""
    Este projeto foi meu laboratório para dominar o Processamento de Dados. 
    Trabalhei com sensores e algoritmos para identificar falhas estruturais.
    """)
    
    # Texto puro, sem Latex, sem Markdown matemático
    st.subheader("📐 Metodologia:")
    st.write("A Transformada de Fourier foi aplicada para converter os sinais do domínio do tempo para o domínio da frequência, permitindo a identificação de anomalias na assinatura vibracional da estrutura.")
    
    st.write("---")
    st.write("> Este projeto demonstra minha capacidade técnica com Python aplicado à engenharia.")

# --- ABA 4: GITHUB ---
elif aba == "Portfólio GitHub":
    st.title("💻 Meu Código")
    st.write("Acesse meus repositórios no link abaixo:")
    st.markdown("[🔗 Visitar Perfil no GitHub](https://github.com/seu-usuario)")

# --- RODAPÉ ---
st.write("---")
st.write("📍 Dracena - SP | 📩 caio.fukushima@exemplo.com")
