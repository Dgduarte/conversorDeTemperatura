from time import sleep

def ler_numero(mensagem):
    """Garante que o usuário digite um valor numérico válido."""
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print("❌ Erro: Por favor, digite um número válido!")

def converter(origem, destino, valor):
    """Converte entre Celsius, Fahrenheit e Kelvin."""
    # 1. Converte qualquer origem para Celsius primeiro
    if origem == 'C':
        celsius = valor
    elif origem == 'F':
        celsius = (valor - 32) * 5 / 9
    elif origem == 'K':
        celsius = valor - 273.15

    # Validação física (Zero Absoluto: ~ -273.15 °C)
    if celsius < -273.15:
        return None  # Temperatura abaixo do zero absoluto

    # 2. Converte de Celsius para o destino
    if destino == 'C':
        return f"{celsius:.2f} °C"
    elif destino == 'F':
        f = (celsius * 9 / 5) + 32
        return f"{f:.2f} °F"
    elif destino == 'K':
        k = celsius + 273.15
        return f"{k:.2f} K"

def menu():
    print('=' * 40)
    print(f"{'CONVERSOR DE TEMPERATURA':^40}")
    print('=' * 40)

    unidades = {'C': 'Celsius', 'F': 'Fahrenheit', 'K': 'Kelvin'}

    while True:
        print("\nEscolha a unidade de ORIGEM:")
        print("[C] Celsius | [F] Fahrenheit | [K] Kelvin | [0] Sair")
        
        origem = input("Opção: ").strip().upper()
        
        if origem == '0':
            print("\nObrigado por usar o conversor!")
            break

        if origem not in unidades:
            print("❌ Opção inválida! Escolha C, F, K ou 0.")
            continue

        valor = ler_numero(f"Digite o valor em {unidades[origem]}: ")

        print("\nEscolha a unidade de DESTINO:")
        print("[C] Celsius | [F] Fahrenheit | [K] Kelvin")
        destino = input("Opção: ").strip().upper()

        if destino not in unidades:
            print("❌ Unidade de destino inválida!")
            continue

        print("\nConvertendo", end='')
        for _ in range(3):
            print('.', end='', flush=True)
            sleep(0.4)
        print()

        resultado = converter(origem, destino, valor)

        if resultado is None:
            print("⚠️ Atenção: Esse valor está abaixo do Zero Absoluto (impossível na física)!")
        else:
            print(f"\n👉 Resultado: {valor:.2f} em {unidades[origem]} = {resultado}")

        print('-' * 40)
        sleep(1)

if __name__ == '__main__':
    menu()
