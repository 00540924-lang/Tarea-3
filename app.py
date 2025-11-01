# app.py
import streamlit as st
from modulos.Venta import mostrar_Venta  # Importamos la función mostrar_venta del módulo venta
from modulos.login import login

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    # Si la sesiòn esta iniciada, mostrar el contenido de ventas
    mostrar_Venta()
else:
    # Si la sesión no está iniciada, mostrar el login
    login()
