import re

print("🎮 DETECTOR DE GTA 6")
print("Formato de códigos de PS5: XXXX-XXXX-XXXX")

def detectar(mensaje):
    patron = r'\b[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}\b'
    return re.findall(patron, mensaje.upper())

while True:
    mensaje = input("\nPega un mensaje del chat: ")
    codigos = detectar(mensaje)

    if codigos:
        for codigo in codigos:
            print("🚨 POSIBLE CÓDIGO:", codigo)
    else:
        print("No se detectaron códigos.")
