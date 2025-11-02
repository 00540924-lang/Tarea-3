import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_clientes():
    st.header("👤 Registrar nuevo cliente")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para registrar clientes
        with st.form("form_cliente"):
            nombre = st.text_input("Nombre del cliente")
            correo = st.text_input("Correo electrónico")
            telefono = st.text_input("Teléfono")
            direccion = st.text_area("Dirección")

            enviar = st.form_submit_button("✅ Guardar cliente")

            if enviar:
                if nombre.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del cliente.")
                else:
                    try:
                        cursor.execute(
                            "INSERT INTO Clientes (Nombre, Correo, Telefono, Direccion) VALUES (%s, %s, %s, %s)",
                            (nombre, correo, telefono, direccion)
                        )
                        con.commit()
                        st.success(f"✅ Cliente registrado correctamente: {nombre}")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar el cliente: {e}")

        # Mostrar clientes registrados
        st.subheader("📋 Lista de clientes registrados")
        try:
            cursor.execute("SELECT * FROM Clientes")
            clientes = cursor.fetchall()

            if not clientes:
                st.info("No hay clientes registrados aún.")
            else:
                for c in clientes:
                    st.write(f"🧾 **{c[1]}** — 📧 {c[3]} — 📞 {c[2]}")
        except Exception as e:
            st.error(f"❌ Error al obtener la lista de clientes: {e}")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()

