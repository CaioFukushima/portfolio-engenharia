# -*- coding: utf-8 -*-
import streamlit as st
from datetime import date
import pandas as pd

# 1. Configuração da página
st.set_page_config(
    page_title="Caio Fukushima | Eng. Civil & Python", 
    page_icon="🏗️", 
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
    "Meu TCC", 
    "GitHub"
])

# --- ABA 1: PERFIL (Sincero e Focado em Aprendizado) ---
if aba == "Perfil Profissional":
    st.title("🏗️ Caio Fukushima")
    st.subheader("Estudante de Engenharia Civil & Entusiasta de Tecnologia")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("📸 [Sua Foto Aqui]")
    
    with col2:
        st.write("""
        Atualmente cursando Engenharia Civil com previsão de formatura para 2026. 
        Diferente da formação tradicional, busco integrar a engenharia com a tecnologia, 
        utilizando **Python** para otimizar processos e analisar dados.
        
        Tenho grande interesse em entender como softwares de engenharia são construídos 
        e como eles podem melhorar a produtividade no setor.
        """)
        st.success("🎯 Objetivo: Oportunidade de estágio ou Trainee para aprender e crescer na área de tecnologia/produto.")

    st.write("---")
    st.subheader("🚀 O que estou desenvolvendo")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Engenharia Civil**")
        st.caption("Foco acadêmico em estruturas e métodos construtivos. Familiaridade teórica com softwares do setor.")
    with c2:
        st.markdown("**Tecnologia & Dados**")
        st.caption("Desenvolvimento de lógica de programação com Python e criação de dashboards com Streamlit.")

# --- ABA 2: DATA SCIENCE ---
elif aba == "Data Science (Estudos)":
    st.title("📊 Estudos de Automação")
    st.write("Aqui eu exploro como o Python pode organizar dados que normalmente ficam soltos em planilhas.")
    
    data = {
        'Exemplo de Dado': ['Material A', 'Material B', 'Material C'],
        'Quantidade': [100, 250, 50],
        'Status': ['Ok', 'Atrasado', 'Ok']
    }
    df = pd.DataFrame(data)
    st.table(df) 
    st.info("💡 Este é um exemplo de manipulação de dados utilizando a biblioteca Pandas.")

# --- ABA 3: TCC ---
elif aba == "Meu TCC":
    st.title("🎓 Pesquisa: Análise de Vibração")
    st.write("**Tema: Detecção de Danos Estruturais**")
    
    st.write("""
    Meu TCC foca no uso de sensores para monitorar a saúde de estruturas. 
    Estou utilizando **Python** como ferramenta principal para processar os sinais 
    coletados, aplicando conceitos como a Transformada de Fourier para identificar falhas.
    """)
    
    st.subheader("📐 Por que Python no TCC?")
    st.write("A escolha do Python me permite analisar grandes volumes de dados de sensores de forma rápida, algo que seria inviável manualmente.")

# --- ABA 4: GITHUB ---
elif aba == "GitHub":
    st.title("💻 Meu Progresso em Código")
    st.write("Acesse meu repositório para ver os scripts que estou desenvolvendo:")
    st.markdown("### [🔗 Visitar meu GitHub](https://github.com/caiofukushima)")

# --- RODAPÉ ---
st.write("---")
st.write("📍 Dracena - SP | 📩 **E-mail:** caio.fukushima@exemplo.com")
