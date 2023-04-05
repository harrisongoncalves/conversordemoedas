import requests
import time

class Cotacoes:
    try:
        cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,EUR-USD,BRL-USD,USD-EUR,BRL-EUR")
        cotacoes.raise_for_status()
        cotacoes = cotacoes.json()
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível obter as cotações: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")

    def sair():
        print("Obrigado por utilizar o meu programa.")
        time.sleep(1.5)
        exit()



    def escolherMoeda(moeda):
        if moeda == 1:
            moedaEscolhida = float(Cotacoes.cotacoes['BRLUSD']["bid"])
            texto = "Digite o valor que você quer transformar em dólar: R$ "
            moedinha = "US$"
        elif moeda == 2:
            moedaEscolhida = float(Cotacoes.cotacoes['USDBRL']["bid"])
            texto = "Digite o valor que você quer transformar em real: US$ "
            moedinha = "R$"
        elif moeda == 3:
            moedaEscolhida = float(Cotacoes.cotacoes['BRLEUR']["bid"])
            texto = "Digite o valor que você quer transformar em euro: R$ "
            moedinha = "EUR€"
        elif moeda == 4:
            moedaEscolhida = float(Cotacoes.cotacoes['EURBRL']['bid'])
            texto = "Digite o valor que você quer transformar em real: EUR€ "
            moedinha = "R$"
        elif moeda == 5:
            moedaEscolhida = float(Cotacoes.cotacoes['USDEUR']["bid"])
            texto = "Digite o valor que você quer transformar em euro: US$ "
            moedinha = "EUR€"
        elif moeda == 6:
            moedaEscolhida = float(Cotacoes.cotacoes['EURUSD']["bid"])
            texto = "Digite o valor que você quer transformar em dólar: EUR€ "
            moedinha = "US$"
        elif moeda == 7:
            Cotacoes.sair()
        return moedaEscolhida, texto, moedinha
         
