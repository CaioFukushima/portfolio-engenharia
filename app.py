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

# 2. Estilo CSS para um visual Profissional (AltoQI Style)
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

# --- CÁLCULOS DO CRONÔMETRO ---
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

# --- ABA 1: PERFIL PROFISSIONAL ---
if aba == "Perfil Profissional":
    st.title("🏗️ Caio Fukushima")
    st.subheader("Estudante de Engenharia Civil & Desenvolvedor de Soluções Tech")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Tenta carregar a foto que você tem na pasta
        try:
            st.image("minha_foto.jpg", caption="Caio Fukushima", use_container_width=True)
        except:
            st.info("📸 Adicione o arquivo 'minha_foto.jpg' ao seu GitHub para exibir sua foto aqui.")
    
    with col2:
        st.write(f"""
        Atualmente cursando Engenharia Civil (conclusão em 2026). Meu objetivo é unir o conhecimento 
        técnico da construção civil com a agilidade da programação em **Python** para otimizar processos.
        
        Acredito que a tecnologia é a chave para uma engenharia mais precisa, econômica e produtiva.
        """)
        st.success("🎯 Objetivo: Atuar em times de Produto ou Inovação em empresas de tecnologia para Engenharia.")

    st.write("---")
    st.subheader("🚀 Frentes de Estudo e Habilidades")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Engenharia Civil**")
        st.caption("Foco em Engenharia Diagnóstica, SHM (Monitoramento de Estruturas) e Teoria de Vigas.")
    with c2:
        st.markdown("**Tecnologia**")
        st.caption("Desenvolvimento em Python, Manipulação de Dados (Pandas) e Automação de Processos.")

# --- ABA 2: MINI PROJETO - EXTRATOR DE DADOS ---
elif aba == "Mini Projeto: Automação":
    st.title("📊 Extrator de Insumos (PDF para Dados)")
    st.write("### Problema: Dados de engenharia 'presos' em arquivos estáticos (PDF).")
    
    st.markdown("""
    Este mini projeto demonstra um algoritmo que automatiza a leitura de listas de materiais e orçamentos. 
    O Python extrai as informações de documentos estáticos e as organiza em tabelas prontas para cálculo.
    """)

    # Tabela de exemplo do que o robô faz
    dados_exemplo = {
        'Insumo Extraído': ['Cimento CP-II', 'Aço CA-50 10mm', 'Areia Média', 'Brita 1'],
        'Quantidade': [150, 1250.5, 12.0, 10.5],
        'Unidade': ['sacos', 'kg', 'm³', 'm³'],
        'Status': ['Processado', 'Processado', 'Processado', 'Processado']
    }
    st.table(pd.DataFrame(dados_exemplo))

    st.write("---")
    st.subheader("💡 Onde isso é útil na Vida Real?")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("**1. Suprimentos**")
        st.write("Comparar preços de 10 fornecedores diferentes em segundos, lendo todos os orçamentos de uma vez.")
    with col_b:
        st.markdown("**2. Gestão de Obra**")
        st.write("Leitura automática de Notas Fiscais para atualizar o estoque e o custo real da obra sem erro humano.")
    with col_c:
        st.markdown("**3. Interoperabilidade**")
        st.write("Converter relatórios de outros softwares para formatos compatíveis com o ecossistema da empresa.")

    st.info("✅ Resultado: O engenheiro deixa de perder tempo digitando e passa a focar na análise técnica.")

# --- ABA 3: PROJETO DE TCC ---
elif aba == "Projeto de TCC (SHM)":
    st.title("🎓 Projeto de TCC: Monitoramento Estrutural")
    st.write("### Detecção de Danos via Sensores MEMS e Transformada de Fourier")
    
    st.markdown("""
    **Contextualização:** No Brasil, mais de 30% das pontes e viadutos apresentam comprometimento estrutural. 
    A inspeção visual é limitada e sistemas de monitoramento tradicionais são de altíssimo custo.
    
    **O Projeto:** Validar o uso de sensores MEMS (smartphones) associados ao processamento de dados por **FFT em Python** para identificar variações na frequência natural de vigas metálicas.
    """)

    st.warning("🔍 **Pergunta Norteadora:** O sistema é eficaz para diferenciar o estado íntegro do estado danificado através da análise modal?")

    st.write("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🛠️ Metodologia Tech")
        st.write("- Coleta de vibrações via acelerômetros MEMS.\n- Processamento via FFT (Fast Fourier Transform).\n- Identificação de perda de rigidez.")
    
    with c2:
        st.markdown("#### 🐍 O Papel do Python")
        st.code("""
import numpy as np

# Lógica para converter sinal em frequência
def analisar_vibracao(sinal, fs):
    fft_valores = np.abs(np.fft.fft(sinal))
    freqs = np.fft.fftfreq(len(sinal), 1/fs)
    return freqs, fft_valores
        """, language='python')

# --- ABA 4: GITHUB ---
elif aba == "GitHub":
    st.title("💻 Portfólio de Código")
    st.write("Acesse meus repositórios com estudos e scripts de automação:")
    st.markdown("### [🔗 Visitar meu GitHub](https://github.com/caiofukushima)")

# --- RODAPÉ ---
st.write("---")
st.write("📍 Dracena - SP")
st.markdown("📩 **E-mail:** [caiofukushima21@gmail.com](mailto:caiofukushima21@gmail.com)")
