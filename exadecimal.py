def decimal_a_hex(numero):
    hex_chars = "0123456789ABCDEF"
    resultado = ""

    while numero > 0:
        resto = numero % 16
        resultado = hex_chars[resto] + resultado
        numero = numero // 16

    return resultado if resultado != "" else "0"


# prueba
num = int(input("Ingrese un número decimal: "))
print("Hexadecimal:", decimal_a_hex(num))
input("Presioná Enter para salir...")