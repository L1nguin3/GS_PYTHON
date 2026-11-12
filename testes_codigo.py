# def calcular_k(temperatura):
#     temperatura = float(temperatura)
#     k = 0.0096 + 0.0011 * (temperatura - 22)
#     return k

# print(calcular_k(22))
# print(calcular_k(34))

from raiz import calcular_k


def calcular_horas(umidade, temperatura):
    if umidade < 0 or umidade > 100:
        return "SENSOR FALHOU"
    elif umidade <= 40:
        return "0 horas"
    taxa = calcular_k(temperatura)
    contadorK = 0
    while umidade > 40:
        k = 2.718281828 ** -taxa
        umidade = umidade * k
        contadorK += 1
    return f"{contadorK} horas"

print(calcular_horas(80, 34))