# -*- coding: utf-8 -*-
import streamlit as st
from datetime import date
import pandas as pd

# 1. Configuração da página
st.set_page_config(
    page_title="Caio Fukushima | Eng. Civil & Tech", 
    page_icon="🏗️", 
    layout="wide"
)

# 2. Estilo CSS Customizado
st.markdown("""
    <style>
        [data-testid="stSidebar"] { background-color: #0A192F !important; }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }
        [data-testid="stMetricValue"] { color: #CDA434 !important; }
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
    "Data Science (Estudos)", 
    "Projeto de TCC (SHM)", 
    "GitHub"
])

# --- ABA 1: PERFIL ---
if aba == "Perfil Profissional":
    st.title("🏗️ Caio Fukushima")
    st.subheader("Estudante de Engenharia Civil & Entusiasta de Tecnologia")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("📸 [Sua Foto Aqui]")
    
    with col2:
        st.write("""
        Atualmente cursando Engenharia Civil (conclusão em 2026). Meu diferencial é a busca por 
        soluções que integram a engenharia tradicional com a agilidade do **Python**.
        
        Tenho grande interesse no desenvolvimento de softwares que otimizam o dia a dia do engenheiro, 
        especialmente na área de monitoramento e análise de dados estruturais.
        """)
        st.success("🎯 Objetivo: Atuar como Analista de Produto Jr ou Trainee em Inovação Tecnológica.")

    st.write("---")
    st.subheader("🚀 Frentes de Estudo")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Engenharia de Estruturas**")
        st.caption("Foco em análise dinâmica, SHM (Monitoramento de Saúde Estrutural) e teoria de vigas.")
    with c2:
        st.markdown("**Programação Aplicada**")
        st.caption("Uso de Python para automação de tarefas e processamento de sinais (FFT).")

# --- ABA 2: DATA SCIENCE ---
elif aba == "Data Science (Estudos)":
    st.title("📊 Estudos de Automação e Dados")
    st.write("Exemplo de manipulação de dados de materiais, substituindo fluxos manuais por automação:")
    
    data = {
        'Material': ['Aço CA-50', 'Concreto Fck 30', 'Areia Média', 'Madeira'],
        'Quantidade': [1200, 45, 12, 110],
        'Unidade': ['kg', 'm³', 'm³', 'm²'],
        'Status': ['Ok', 'Pendente', 'Atrasado', 'Ok']
    }
    df = pd.DataFrame(data)
    st.table(df) 
    st.info("💡 Utilizo bibliotecas como Pandas para organizar dados complexos em informações acionáveis.")

# --- ABA 3: TCC (VERSÃO ESTRATÉGICA) ---
elif aba == "Projeto de TCC (SHM)":
    st.title("🎓 Monitoramento Estrutural Inteligente")
    st.write("### Detecção de Danos via Sensores MEMS e Python")
    
    st.markdown("""
    **Contextualização:** No Brasil, mais de 30% das pontes e viadutos públicos possuem comprometimento estrutural. 
    A inspeção visual é limitada e sistemas de monitoramento (SHM) tradicionais são extremamente caros.
    
    **A Solução Proposta:** Validar o uso de sensores de baixo custo (MEMS de smartphones) integrados ao processamento de dados em Python.
    """)

    st.warning("🔍 **Pergunta Norteadora:** O uso de sensores MEMS, associado ao processamento por FFT em Python, é eficaz para identificar variações na frequência natural de vigas e diferenciar o estado íntegro do danificado?")

    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🛠️ Metodologia Aplicada")
        st.write("""
        - **Modelo:** Vigas metálicas em balanço (Euler-Bernoulli).
        - **Aquisição:** Coleta de vibrações reais via smartphones.
        - **Algoritmo:** Transformada Rápida de Fourier (FFT) para análise modal.
        """)
    
    with col2:
        st.markdown("#### 🐍 Lógica de Processamento")
        st.code("""
# Exemplo do script de análise FFT
import numpy as np

def detectar_frequencia(sinal, fs):
    # Converte sinal do tempo para frequência
    valores_fft = np.abs(np.fft.fft(sinal))
    freqs = np.fft.fftfreq(len(sinal), 1/fs)
    return freqs, valores_fft
        """, language='python')

    st.write("> *Este projeto une a física da engenharia com a precisão da computação para prever falhas antes que elas aconteçam.*")

# --- ABA 4: GITHUB ---
elif aba == "GitHub":
    st.title("💻 Portfólio de Código")
    st.write("Veja como organizo meus estudos e scripts de engenharia:")
    st.markdown("### [🔗 Acessar meu Perfil no GitHub](https://github.com/caiofukushima)")

# --- RODAPÉ ---
st.write("---")
st.write("📍 Dracena - SP")
st.markdown("📩 **Contato:** [caio.fukushima@exemplo.com](mailto:caio.fukushima@exemplo.com)")
