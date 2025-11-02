import streamlit as st
from modulos.Venta import mostrar_venta
from modulos.cliente import mostrar_clientes
from modulos.login import login

if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    opciones = ["Ventas", "Clientes", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Clientes":
        mostrar_clientes()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")
else:
    login()


