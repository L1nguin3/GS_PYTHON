umidades = [80, 55, 38]
temperaturas = [30, 28, 22]


def classificar_umidade(umidade):
    if umidade < 0 or umidade > 100:
        return "SENSOR FALHOU"
    elif umidade <= 40:
        return "IRRIGAR AGORA"
    elif umidade <= 60:
        return "ATENÇÃO"
    else:
        return "SOLO OK"


def pedir_numero(mensagem, minimo, maximo):
    while True:
        numero = float(input(mensagem))
        if minimo <= numero <= maximo:
            return numero
        print(f"Digite um número entre {minimo} e {maximo}")


while True:
    print("\n1 - Cadastrar | 2 - Listar | 0 - Sair")
    opcao = input("Escolha: ")

    if opcao in ["0", "1", "2"]:
        match int(opcao):

            case 1:
                cadastro_umidade = pedir_numero("Digite a umidade: ", -100, 200)
                cadastro_temperatura = pedir_numero("Digite a temperatura: ", 15, 40)
                umidades.append(cadastro_umidade)
                temperaturas.append(cadastro_temperatura)
                print("Cadastro realizado com sucesso!")

            case 2:
                if len(umidades) != len(temperaturas):
                    print("Erro: quantidade de registros diferente!")
                elif len(umidades) == 0:
                    print("Nenhum registro encontrado!")
                else:
                    print("Registros")
                    contador = 0
                    while contador < len(umidades):
                        umidade = umidades[contador]
                        temperatura = temperaturas[contador]
                        classificacao = classificar_umidade(umidade)
                        print(f"Umidade: {umidade} | Temperatura: {temperatura} | Classificação: {classificacao}")
                        contador += 1

            case 0:
                print("Até logo!")
                break
    else:
        print("Opção inválida!")
        
def calcular_k(temperatura):
    temperatura = float(temperatura)
    k = 0.0096 + 0.0011 * (temperatura - 22)
    return k