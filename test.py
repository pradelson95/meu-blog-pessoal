# import socket

# print("Nombre del host:", socket.gethostname())
# print("Dirección IP local:", socket.gethostbyname(socket.gethostname()))



# from PIL import ImageGrab
# import time


# for screen in range(1,6):
#     screenshot = ImageGrab.grab()
#     screenshot.save(f"screenshot_{screen}.png", "PNG")
#     time.sleep(1)  # Espera 1 segundo entre capturas
#     # Aquí puedes agregar un tiempo de espera entre capturas si es necesario
#     # time.sleep(1)  # Espera 1 segundo entre capturas
# screenshot.close()

# import platform 


# info = { 
#             "sistema operativo": platform.system(),
#             "versión": platform.version(),
#             "arquitectura": platform.architecture()[0],
#             "nombre de usuario": platform.node(),
#             "procesador": platform.processor(),
#             "nombre completo de la SO": platform.platform()
#         }
#         # Guardar información en un archivo

# with open("info_sistema.txt", "a") as file:
#         for key, value in info.items():
#             file.write(f"{key}: {value}\n")
#             file.write("\n") 