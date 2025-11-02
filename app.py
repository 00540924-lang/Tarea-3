import streamlit as st
from modulos.venta import mostrar_venta
from modulos.Producto import mostrar_productos
from modulos.Cliente import mostrar_clientes
from modulos.login import login

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    
    # --- MENÚ LATERAL ---
    opciones = ["Ventas", "Productos", "Clientes", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # --- SEGÚN LA SELECCIÓN, MOSTRAMOS EL CONTENIDO ---
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Clientes":
        mostrar_clientes()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")
else:
    # Mostrar login si la sesión no está iniciada
    login()




