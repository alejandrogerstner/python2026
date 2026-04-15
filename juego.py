import random

numero_secreto = random.randint(1, 10)
intentos = 0

print("🎮 Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número del 1 al 10...")

while True:
    intento = int(input("Ingresá tu número: "))
    intentos += 1

    if intento < numero_secreto:
        print("🔼 Muy bajo")
    elif intento > numero_secreto:
        print("🔽 Muy alto")
    else:
        print(f"🎉 Correcto! Lo lograste en {intentos} intentos")
        break
        