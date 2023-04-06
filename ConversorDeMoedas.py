from cotacoes import Cotacoes, time

def continuar():
     while True: 
        novamente = input("Deseja realizar outra conversão? (s/n): ")
        if novamente == 'n':
            Cotacoes.sair()
        elif novamente == 's':
            print("\n")
            main()
        else:
            print("Opção inválida.")
            continue

def main():
    print("Conversor de moedas")
    print(f"US$ = R$ {float(Cotacoes.cotacoes['USDBRL']['bid']):.2f} | EUR€ = R$ {float(Cotacoes.cotacoes['EURBRL']['bid']):.2f}\n")
    print("Selecione a opção de conversão:")
    print("1 --> Real para dólar\n"
    "2 --> Dólar para real\n"
    "3 --> Real para euro\n"
    "4 --> Euro para real\n"
    "5 --> Dólar para euro\n"
    "6 --> Euro para dólar\n"
    "7 --> Sair do programa")
    while True:
        try:
            moeda = int(input("Digite a sua opção: "))
            if moeda >= 1 and moeda <= 7:
                moedaEscolhida, texto, moedinha = Cotacoes.escolherMoeda(moeda)
                converterMoeda(moedaEscolhida, texto, moedinha)
            else:
                print("Digite uma opção válida.")
        except ValueError:
            print("Digite uma opção válida.")
            continue




def converterMoeda(moedaEscolhida, texto, moedinha):
        while True:
            try:
                valor = float(input(texto).replace(",","."))
                valorConvertido = float(valor) * float(moedaEscolhida)
                print(f"Você possui: {moedinha} {valorConvertido:.2f}".replace(".",","))
                time.sleep(0.5)
                continuar()
            except ValueError:
                print("Número inválido.")
                time.sleep(1)
                continue

main()