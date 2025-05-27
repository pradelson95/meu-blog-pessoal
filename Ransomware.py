import tkinter as tk       # Importamos tkinter para crear la interfaz gráfica
import pyautogui           # Importamos pyautogui para controlar el mouse
from tkinter import messagebox  # Importamos messagebox para mostrar mensajes emergentes
import keyboard

# Contraseña que se usará para desbloquear la pantalla
CONTRASENA = "1234"

# Función que se ejecuta al presionar el botón "Desbloquear"
def verificar():
    # Verifica si lo escrito en la caja de entrada es igual a la contraseña
    if entrada.get() == CONTRASENA:
        root.destroy()  # Cierra la ventana si la contraseña es correcta
    else:
        # Si es incorrecta, muestra un mensaje en rojo
        messagebox.showerror(
            "Error",
            "Contraseña incorrecta. Intenta de nuevo.",
            parent=root # Muestra el mensaje en la ventana principal
        )

# Crear la ventana principal
root = tk.Tk()

# Hacemos que la ventana ocupe toda la pantalla (pantalla completa)
root.attributes('-fullscreen', True)

# Ponemos fondo negro para simular una pantalla bloqueada
root.configure(bg='black')

# Establecemos el título de la ventana
root.title("Bloqueo de Sistema")

# Evita que se pueda cerrar la ventana con Alt+F4 o el botón de cerrar
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Texto de instrucciones
label = tk.Label(
    root,
    text="Introduce la contraseña para desbloquear",
    font=("Arial", 24),
    bg="black",
    fg="white"
)
label.pack(pady=40)  # Empaqueta el texto con espacio vertical

# Caja de entrada para escribir la contraseña
entrada = tk.Entry(
    root,
    font=("Arial", 20),
    show="*",           # Oculta lo que se escribe (como contraseña)
    justify="center"    # Centra el texto dentro del cuadro
)
entrada.pack(pady=20)

# Botón que al presionarlo verifica la contraseña
boton = tk.Button(
    root,
    text="Desbloquear",
    font=("Arial", 18),
    command=verificar    # Llama a la función verificar cuando se presiona
)
boton.pack(pady=10)

# Mensaje que aparecerá si la contraseña es incorrecta
label_msg = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    bg="black"
)
label_msg.pack()

# Coloca el cursor automáticamente en la caja de entrada
entrada.focus_set()

# Función para mover el mouse constantemente al centro de la pantalla
# Esto simula un bloqueo del mouse (el usuario no puede moverlo)
def bloquear_mouse():
    if entrada.get() != CONTRASENA:
        ancho, alto = pyautogui.size()
        pyautogui.moveTo(ancho // 2, alto // 2)
        lista_teclas = teclas = ["ctrl", "alt", "shift", "esc", "f1", "f2", "f3", "f4", "f5", "f6", 
          "f7", "f8", "f9", "f10", "f11", "f12","home", "end", "insert", "delete", "up", "down", "left", "right"]
        for tecla in teclas:
            keyboard.block_key(tecla)    

    root.after(100, bloquear_mouse)


# Llama por primera vez a la función para empezar a bloquear el mouse
bloquear_mouse()

# Inicia el bucle principal de tkinter (muestra la ventana)
root.mainloop()
