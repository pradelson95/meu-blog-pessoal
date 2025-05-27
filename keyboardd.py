import keyboard



teclas = ["ctrl", "alt", "shift", "esc", "f1", "f2", "f3", "f4", "f5", "f6", 
          "f7", "f8", "f9", "f10", "f11", "f12", "page up", "page down", 
          "home", "end", "insert", "delete"]

print("Presiona ESC para salir")

while True:
    for t in teclas:
        if keyboard.is_pressed(t):
            print(f"{t} presionada")
    if keyboard.is_pressed("esc"):
        break
