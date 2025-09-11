import streamlit as st
import smtplib
from email.message import EmailMessage

st.title("✉️ Enviar Correo con SMTP")

remitente = st.text_input("Tu correo:")
password = st.text_input("Tu contraseña:", type="password")
destinatario = st.text_input("Destinatario:")
asunto = st.text_input("Asunto:")
mensaje = st.text_area("Mensaje:")

if st.button("Enviar Correo"):
    try:
        msg = EmailMessage()
        msg.set_content(mensaje)
        msg["Subject"] = asunto
        msg["From"] = remitente
        msg["To"] = destinatario

        with smtplib.SMTP_SSL("smtp.gmail.com", 587) as server:
            server.login(remitente, password)
            server.send_message(msg)
        st.success("¡Correo enviado con éxito!")
    except Exception as e:
        st.error(f"Error al enviar el correo: {e}")
        
