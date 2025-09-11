import streamlit as st
import smtplib
from email.message import EmailMessage

st.title("✉️ Enviar correo con Gmail")

# Información del remitente pre-configurada
# ¡Advertencia de seguridad!
# No se recomienda poner contraseñas directamente en el código.
# Es preferible usar un archivo de secretos o variables de entorno.
remitente = "070899Eavc@gmail.com"
password = "Eavc1106742184"

destinatario = st.text_input("Destinatario:")
asunto = st.text_input("Asunto:")
mensaje = st.text_area("Mensaje:")

if st.button("Enviar correo"):
    # Comprobar que los campos no estén vacíos
    if not destinatario or not asunto or not mensaje:
        st.warning("Por favor, completa todos los campos para enviar el correo.")
    else:
        try:
            msg = EmailMessage()
            msg.set_content(mensaje)
            msg["Subject"] = asunto
            msg["From"] = remitente
            msg["To"] = destinatario

            # Conectar al servidor SMTP de Gmail
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(remitente, password)
                server.send_message(msg)
            st.success("¡Correo enviado con éxito!")

        except Exception as e:
            st.error(f"Error al enviar el correo: {e}")
            st.error("Revisa tu contraseña y si tienes la verificación en dos pasos, "
                     "usa una contraseña de aplicación.")
