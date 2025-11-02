import streamlit as st
from modulos.venta import mostrar_venta
from modulos.Producto import mostrar_productos
from modulos.login import login

if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    opciones = ["Ventas", "Productos", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")
else:
    login()



