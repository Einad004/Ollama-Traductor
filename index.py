import streamlit as st
from backend.monoagente import MultiSkillAgent

# Inicializar el agente
if 'agent' not in st.session_state:
    st.session_state.agent = MultiSkillAgent()

st.set_page_config(page_title="DeepL Mono-Agent", layout="wide")
st.title("🌐 Agente Traductor con Ollama")

# 1. Definir la entrada de texto PRIMERO
input_text = st.text_area("Escribe aquí el texto:", height=200, placeholder="Escribe algo...")

# 2. Definir los selectores
languages = ["Spanish", "English", "French", "German", "Italian"]
col_langs = st.columns(2)
with col_langs[0]:
    src_lang = st.selectbox("De:", ["Detectar automáticamente"] + languages)
with col_langs[1]:
    tgt_lang = st.selectbox("A:", languages, index=1)

# 3. Botones de acción (Habilidades del agente)
col_btns = st.columns(3)

with col_btns[0]:
    if st.button("🚀 Traducir"):
        if input_text:
            res = st.session_state.agent.act("traducir", {
                "text": input_text, "source": src_lang, "target": tgt_lang
            })
            st.text_area("Resultado:", value=res, height=150)
        else:
            st.warning("Escribe texto primero")

with col_btns[1]:
    if st.button("🔍 Detectar Idioma"):
        if input_text:
            res = st.session_state.agent.act("detectar", {"text": input_text})
            st.info(f"Idioma: {res}")

with col_btns[2]:
    if st.button("✨ Pulir Texto"):
        if input_text:
            with st.spinner("Mejorando redacción..."):
                # ¡AQUÍ ESTÁ EL CAMBIO! 
                # Agregamos "source": src_lang al diccionario
                res = st.session_state.agent.act("pulir", {
                    "text": input_text, 
                    "source": src_lang 
                })
                st.success(res)
        else:
            st.warning("Escribe algo primero")