# -*- coding: utf-8 -*-
import streamlit as st
from datetime import date
import pandas as pd

# 1. Configuração da página
st.set_page_config(
    page_title="Caio Fukushima | Eng. Civil & Python Developer", 
    page_icon="🐍", 
    layout="wide"
)

# 2. Estilo CSS - FOCO EM TECNOLOGIA E LEITURA
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #0A192F !important;
        }
        /* Força todos os textos da lateral para branco */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        /* Destaque do contador de dias em Ouro */
        [data-testid="stMetricValue"] {
            color: #CDA434 !important;
        }
        /* Botões Estilizados */
        .stButton>button {
            width: 100% !important;
            border-radius: 10px !important;
            background-color: #CDA434 !important;
            color: white !important;
            font-weight: bold !important;
            border: none !important;
        }
        .stButton>button:hover {
            background-color: #FFD700 !important;
            color: #0A192F !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CÁLCULO DO CRONÔMETRO ---
data_formatura = date(2026, 12, 1) 
hoje = date.today()
dias_faltantes = (data_formatura - hoje).days

# --- BARRA LATERAL ---
st.sidebar.title("Navegação")
st.sidebar.markdown("### 🎓 Carreira")
st.sidebar.metric(label="Dias para Formatura", value=f"{dias_faltantes} dias")
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
        st.info("📸 [Dica: Coloque uma foto profissional aqui]")
        # st.image("minha_foto.jpg", width=250)
    
    with col2:
        st.write("""
        Diferente do engenheiro tradicional, meu foco é a **automação e digitalização da construção**. 
        Acredito que o futuro da engenharia civil está nos dados, e utilizo Python para criar 
        fluxos de trabalho mais inteligentes, rápidos e precisos.
        """)
        st.success("🎯 Objetivo: Trainee em Inovação, Planejamento Digital ou Gestão de Dados (BIM/VDC).")

# --- ABA 2: DATA SCIENCE ---
elif aba == "Data Science & Engenharia":
    st.title("📊 Manipulação de Dados de Projeto")
    st.write("Exemplo de como o Python substitui planilhas complexas por tabelas interativas.")
    
    # Exemplo prático usando PANDAS
    data = {
        'Insumo': ['Cimento', 'Aço CA-50', 'Areia', 'Brita'],
        'Quantidade': [500, 1200, 45, 38],
        'Unidade': ['Sacos', 'kg', 'm³', 'm³'],
        'Status': ['Entregue', 'Pendente', 'Entregue', 'Atrasado']
    }
    df = pd.DataFrame(data)
    
    st.subheader("📋 Controle de Suprimentos (Automatizado)")
    st.table(df) 
    
    st.info("💡 Imagine automatizar a leitura de 1.000 itens de um orçamento em segundos. É isso que eu faço.")

# --- ABA 3: TCC (AJUSTADA PARA IPHONE) ---
elif aba == "Pesquisa e Sinais (TCC)":
    st.title("🎓 Pesquisa Técnica Avançada")
    st.write("**Detecção de Danos via Análise de Vibração**")
    
    st.markdown("""
    Este projeto foi meu laboratório para dominar **Processamento de Dados**. 
    Através dele, aprendi a lidar com sensores MEMS e Transformada de Fourier para resolver problemas estruturais.
    """)
    
    st.markdown("#### 📐 Equação da Transformada de Fourier:")
    # Formatação robusta para evitar erro de Syntax no Safari/iPhone
    st.info("X(f) = ∫ x(t) e^(-i 2π f t) dt")
    
    st.write("> *Este projeto demonstra minha capacidade de aprender tecnologias complexas e aplicá-las na Engenharia Civil.*")

# --- ABA 4: GITHUB ---
elif aba == "Portfólio GitHub":
    st.title("💻 Meu Código")
    st.write("Acesse meus repositórios com scripts de automação e estudos de dados.")
    st.markdown("### [🔗 Visitar meu Perfil no GitHub](https://github.com/seu-usuario)")

# --- RODAPÉ ---
st.write("---")
st.write("📍 Dracena - SP")
st.markdown("📩 **E-mail:** [caio.fukushima@exemplo.com](mailto:caio.fukushima@exemplo.com)")
