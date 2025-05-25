# Persistência de Dados (Básico)

import datetime
import json
import os # Importa o módulo os para verificar a existência do arquivo

nome_arquivo = "banco_dados.json" # Nome do arquivo para salvar os dados

# Tenta carregar os dados do arquivo, se existir 
if os.path.exists(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            saldo = dados.get("saldo", 1000.0) # Carrega o saldo, usa 1000.0 como padrão se não encontrar
            extrato = dados.get("extrato", []) # Carrega o extrato, usa [] como padrão
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com dados padrão.")
        saldo = 1000.0
        extrato = []
else:
    saldo = 1000.0 # Saldo inicial (você pode alterar este valor)
    extrato = [] # Lista para armazenar as transações

def consultar_saldo():
    """Exibe o saldo atual."""
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
    
def sacar():
    """Realiza a operação de saque, verificando o saldo."""
    global saldo, extrato 
    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")

    if valor_saque <= saldo:
        saldo -= valor_saque 
        agora = datetime.datetime.now()
        extrato.append({"data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"), "tipo": "Saque", "valor": valor_saque})
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insuficiente.")

def depositar():
    """Realiza a operação de depósito."""
    global saldo, extrato
    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    saldo += valor_deposito
    agora = datetime.datetime.now()
    extrato.append({"data_hora": agora.strftime("%d/%m/%Y %H:%M:%S"), "tipo": "Depósito", "valor": valor_deposito})
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    print(f"Seu novo saldo é: R$ {saldo:.2f}")

def exibir_extrato():
    """Exibe o extrato bancário."""
    global extrato
    if not extrato:
        print("Não foram realizadas transações.")
    else:
        print("\n--- Extrato Bancário ---")
        for transacao in extrato:
            data_hora = transacao["data_hora"]
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

# ... (seu código principal com o loop while)
while True:
    print("\n--- Bem-vindo ao seu banco virtual ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Extrato") #Opção para exibir o extrato
    print("5 - Sair")

    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1 <= opcao <= 5: # Modifiquei para incluir a opção 5
                break # Sai do loop se a opção for válida
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")         

    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4: # Nova condição para exibir extrato
        exibir_extrato()
    elif opcao == 5: # Opção para sair 
        print("Obrigado por utilizar nosso banco virtual!")
        break # Sai do laço while, encerrando o programa

# Salva o saldo e o extrato no arquivo antes de sair
try:
    with open(nome_arquivo, "w") as arquivo:
        json.dump({"saldo": saldo, "extrato": extrato}, arquivo, indent=4) # Indentação para melhor legibilidade
    print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Erro ao salvar os dados: {e}.")

