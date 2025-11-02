import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_productos():
    st.header("📦 Gestión de productos")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # --- FORMULARIO PARA AGREGAR PRODUCTO ---
        with st.form("form_producto"):
            nombre = st.text_input("Nombre del producto")
            precio = st.number_input("Precio", min_value=0.0, step=0.01)
            cantidad = st.number_input("Cantidad disponible", min_value=0, step=1)
            enviar = st.form_submit_button("✅ Guardar producto")

            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Productos (Nombre, Precio, Cantidad) VALUES (%s, %s, %s)",
                            (nombre, str(precio), str(cantidad))
                        )
                        con.commit()
                        st.success(f"✅ Producto registrado correctamente: {nombre} (Cantidad: {cantidad}, Precio: {precio})")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar el producto: {e}")

        # --- LISTA DE PRODUCTOS REGISTRADOS ---
        st.subheader("📋 Productos registrados")
        try:
            cursor.execute("SELECT * FROM Productos")
            productos = cursor.fetchall()

            if not productos:
                st.info("No hay productos registrados aún.")
            else:
                for p in productos:
                    # Suponiendo que la tabla Productos tiene columnas: ID, Nombre, Precio, Cantidad
                    st.write(f"🧾 **{p[1]}** — Precio: {p[2]} — Cantidad: {p[3]}")
        except Exception as e:
            st.error(f"❌ Error al obtener la lista de productos: {e}")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
