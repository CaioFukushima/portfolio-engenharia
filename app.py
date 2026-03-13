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
    "Mini Projeto: Automação", 
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
        Atualmente cursando Engenharia Civil (conclusão em 2026). Meu foco é integrar a engenharia 
        tradicional com o poder do **Python** para criar ferramentas que otimizam o fluxo de trabalho.
        """)
        st.success("🎯 Objetivo: Atuar em times de Produto ou Inovação em empresas de Software para Engenharia.")

# --- ABA 2: MINI PROJETO (EXTRATOR DE DADOS) ---
elif aba == "Mini Projeto: Automação":
    st.title("📊 Extrator de Insumos (PDF para Dados)")
    st.write("### Problema: Dados de orçamento 'presos' em arquivos estáticos.")
    
    st.markdown("""
    Este projeto demonstra um algoritmo que desenvolvi para **automatizar a leitura de listas de materiais**. 
    O Python extrai as informações de documentos estáticos e as organiza em tabelas dinâmicas.
    """)

    # Simulando a função de extração para o portfólio
    dados = {
        'Código': ['001', '002', '003', '004'],
        'Descrição do Insumo': ['Cimento CP-II 50kg', 'Aço CA-50 10mm', 'Areia Média Lavada', 'Brita 1'],
        'Qtd Original (PDF)': ['150.00', '1.250,50', '12,0', '10,5'],
        'Qtd Tratada (Python)': [150.0, 1250.5, 12.0, 10.5]
    }
    df_extraido = pd.DataFrame(dados)

    st.subheader("📋 Resultado da Extração Automática")
    st.dataframe(df_extraido, use_container_width=True)

    st.success("✅ **Ganho de Eficiência:** Redução drástica no erro humano e tempo de transcrição de orçamentos.")
    
    with st.expander("🔍 Ver lógica por trás (Python)"):
        st.code("""
import pdfplumber
import pandas as pd

# Exemplo de como o script processa o documento
def processar_pdf(caminho):
    with pdfplumber.open(caminho) as pdf:
        tabela = pdf.pages[0].extract_table()
        df = pd.DataFrame(tabela[1:], columns=tabela[0])
        # Limpeza e conversão de tipos
        return df
        """, language='python')

# --- ABA 3: TCC ---
elif aba == "Projeto de TCC (SHM)":
    st.title("🎓 Monitoramento Estrutural Inteligente")
    st.write("### Detecção de Danos via Sensores MEMS e Python")
    
    st.markdown("""
    **Contextualização:** No Brasil, mais de 30% das pontes e viadutos públicos possuem comprometimento estrutural. 
    A inspeção visual é limitada e sistemas de monitoramento (SHM) tradicionais são extremamente caros.
    """)

    st.warning("🔍 **Pergunta Norteadora:** O uso de sensores MEMS, associado ao processamento por FFT em Python, é eficaz para identificar variações na frequência natural de vigas?")

    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🛠️ Metodologia")
        st.write("- Coleta de vibrações reais via smartphones.\n- Algoritmo FFT para análise modal.")
    
    with col2:
        st.markdown("#### 🐍 Ferramenta")
        st.code("import numpy as np\n# FFT em Python", language='python')

# --- ABA 4: GITHUB ---
elif aba == "GitHub":
    st.title("💻 Portfólio de Código")
    st.write("Acesse meus repositórios e scripts:")
    st.markdown("### [🔗 Acessar meu Perfil no GitHub](https://github.com/caiofukushima)")

# --- RODAPÉ ---
st.write("---")
st.write("📍 Dracena - SP | 📩 **Contato:** caio.fukushima@exemplo.com")
