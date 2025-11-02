import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_clientes():
    st.header("👤 Gestión de clientes")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # --- FORMULARIO PARA AGREGAR NUEVO CLIENTE ---
        with st.form("form_cliente"):
            st.subheader("➕ Agregar cliente")
            nombre = st.text_input("Nombre del cliente")
            correo = st.text_input("Correo electrónico")
            telefono = st.text_input("Teléfono")
            direccion = st.text_area("Dirección")
            enviar = st.form_submit_button("Guardar cliente")

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

        # --- MOSTRAR CLIENTES REGISTRADOS ---
        st.subheader("📋 Lista de clientes registrados")
        cursor.execute("SELECT * FROM Clientes")
        clientes = cursor.fetchall()

        if not clientes:
            st.info("No hay clientes registrados aún.")
            return

        # Crear una tabla editable con botones de acción
        for c in clientes:
            col1, col2, col3, col4, col5 = st.columns([2,2,2,3,1])
            with col1:
                st.write(c[1])  # Nombre
            with col2:
                st.write(c[2])  # Correo
            with col3:
                st.write(c[3])  # Teléfono
            with col4:
                st.write(c[4])  # Dirección
            with col5:
                # Botón de editar
                if st.button(f"✏️ Editar {c[0]}", key=f"edit_{c[0]}"):
                    st.session_state["editar_cliente"] = c[0]
                # Botón de eliminar
                if st.button(f"🗑️ Eliminar {c[0]}", key=f"del_{c[0]}"):
                    try:
                        cursor.execute("DELETE FROM Clientes WHERE ID=%s", (c[0],))
                        con.commit()
                        st.success(f"✅ Cliente eliminado: {c[1]}")
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al eliminar el cliente: {e}")

        # --- FORMULARIO PARA EDITAR CLIENTE ---
        if "editar_cliente" in st.session_state:
            cliente_id = st.session_state["editar_cliente"]
            cursor.execute("SELECT * FROM Clientes WHERE ID=%s", (cliente_id,))
            cliente = cursor.fetchone()
            if cliente:
                st.subheader(f"✏️ Editar cliente: {cliente[1]}")
                nombre_edit = st.text_input("Nombre", value=cliente[1])
                correo_edit = st.text_input("Correo", value=cliente[2])
                telefono_edit = st.text_input("Teléfono", value=cliente[3])
                direccion_edit = st.text_area("Dirección", value=cliente[4])
                if st.button("Guardar cambios", key="guardar_edit"):
                    try:
                        cursor.execute(
                            "UPDATE Clientes SET Nombre=%s, Correo=%s, Telefono=%s, Direccion=%s WHERE ID=%s",
                            (nombre_edit, correo_edit, telefono_edit, direccion_edit, cliente_id)
                        )
                        con.commit()
                        st.success("✅ Cliente actualizado correctamente")
                        del st.session_state["editar_cliente"]
                        st.rerun()
                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al actualizar el cliente: {e}")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'con' in locals():
            con.close()
