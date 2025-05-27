# Importar la clase para crear mensajes de correo
from email.message import EmailMessage
# Importar el módulo para manejar conexiones seguras
import ssl
# Importar el módulo para interactuar con servidores SMTP
import smtplib


# Configurar los detalles del correo
remitente = 'pradelsonfrancois@gmail.com'  # Dirección de correo del remitente
contraseña = "meuhicuflzdmbwdh"  # Contraseña del remitente (aquí parece ser una contraseña de aplicación)
destinatarios = ['benitapolite799@gmail.com', "rosapolite799@gmail.com"]  # Lista de destinatarios
asunto = 'Reporte de Sistema'
contenido = "Adjunto el archivo con la información del sistema."



# Crear el mensaje de correo
em = EmailMessage()  # Crear una instancia del mensaje
em["From"] = remitente  # Configurar el remitente
em["To"] = ", ".join(destinatarios)  # Configurar los destinatarios, separados por coma
em["Subject"] = asunto  # Configurar el asunto del correo
em.set_content(contenido)  # Configurar el contenido del mensaje

nombre_archivo = "info_sistema.txt"  # Nombre del archivo que contiene la información del sistema

try:
    with open(nombre_archivo, "rb") as file:  # Abrir el archivo en modo lectura
        contenido = file.read()  # Leer el contenido del archivo
        em.add_attachment(file.read(), maintype='text', subtype='plain', filename=nombre_archivo)  # Adjuntar el archivo al correo
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encontró. Asegúrate de que el archivo exista en la misma carpeta que este script.")

# Configurar la conexión segura
context = ssl.create_default_context()  # Crear un contexto SSL seguro

# Enviar el correo
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:  # Conectar al servidor SMTP usando SSL
    smtp.login(remitente, contraseña)  # Autenticarse con el correo del remitente
    smtp.sendmail(remitente, destinatarios, em.as_string())  # Enviar el correo a los destinatarios

