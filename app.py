import streamlit as st
from modulos.venta import mostrar_venta  # ← minúscula aquí
from modulos.login import login

if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    mostrar_venta()
else:
    login()

