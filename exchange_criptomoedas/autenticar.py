from datetime import datetime
import random
import autenticar

# Função de inicio (login, cadastro, sair)
def usuario():
    print("Seja bem-vindo(a) a maior exchange de criptomoedas do Brasil.")
    print("0 - Sair")
    print("1 - Efetuar login")
    print("2 - Cadastrar usuário")
    x = input("Selecione uma opção: ")
    return x

# Função pra validar e obter o nome do usuário
def Nome():
    while True:
        nome = input("Digite o seu nome completo: ")
        if nome == "":
            print("Campo vazio. Digite o seu nome completo.")
            continue
        temp = "".join(nome.split(" "))
        for letra in temp:
            if letra.isdigit():
                print("Somente letras. Digite um nome válido.")
                break
        else:
            return nome.strip(" ")

# Função pra validar e obter o email do usuário
def Email():
    while True:
        email = input("Digite o seu email: ")
        if email == "":
            print("Campo vazio. Digite o seu email.")
        elif "@" and ".com" in email:
            return email.strip(" ")
        else:
            print("O seu email deve conter @ e .com. Digite o seu email.")

# Função pra validar e obter a data de nascimento do usuário
def Data():
    while True:
        data = input("Nascimento (dd/mm/aaaa): ")
        if data == "":
            print("Campo vazio. Digite a sua data de nascimento.")
            continue
        temp = "".join(data.split("/"))
        if not temp.isnumeric():
            print("Somente números. Digite uma data válida")
            continue
        if data.count("/") == 2 and data != "//":
            dia, mes, ano = data.split("/")
            if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2024:
                return data.strip(" ")
            else:
                print("Data inválida. Digite uma data válida.")
        else:
            print("A data deve seguir o padrão dd/mm/aaaa. Digite uma data válida.")

# Função pra validar e obter a senha do usuário
def Senha():
    while True:
        senha = input("Digite a sua senha de 6 dígitos: ")
        if senha == "":
            print("Campo vazio. Digite a sua senha.")
            continue
        return senha.strip(" ")

# Função pra chamar as opções do menu
def menu():
    print("1 - Consultar saldo")
    print("2 - Consultar extrato")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Comprar criptomoedas")
    print("6 - Vender criptomoedas")
    print("7 - Atualizar cotação")
    print("8 - Sair")
    x = input("Selecione uma opção: ")
    return x

# Função pra cadastrar um usuário
def cadastro():
    nome = Nome()
    login = Login()
    
    lerlogins = open('logins.txt', 'r')
    for linha in lerlogins.readlines():
        valores = linha.split('-')
        if login == valores[1].split(':')[1].strip():
            print("Login existente.")
            return
    lerlogins.close()
    
    senha = Senha()
    email = Email()
    data = Data()
    saldo_reais = 0.00
    saldo_bitcoin = 0.00
    saldo_ethereum = 0.00
    saldo_ripple = 0.00
    
    print("Seu cadastro foi concluído.")
    
    #envia os dados para logins.txt
    logins = open("logins.txt", 'a')
    logins.write(f'Nome: {nome} - Login: {login} - Senha: {senha} - Email: {email} - Data: {data} - Saldo Reais: {saldo_reais} - Saldo Bitcoin: {saldo_bitcoin} - Saldo Ethereum: {saldo_ethereum} - Saldo Ripple: {saldo_ripple}\n')
    logins.close()
    return

# Função pra fazer login
def Login():
    while True:
        login = input("Digite o seu login: ")
        if login == "":
            print("Campo vazio. Digite o seu login.")
            continue
        elif not login.isnumeric():
            print("Somente números. Digite o seu login.")
            continue
        lerlogins = open('logins.txt', 'r')
        login_encontrado = False
        senha_correta = False
        for linha in lerlogins.readlines():
            valores = linha.split('-')
            if login == valores[1].split(':')[1].strip():
                login_encontrado = True
                senha = input("Digite a sua senha de 6 dígitos: ")
                if senha == valores[2].split(':')[1].strip():
                    senha_correta = True
                    print("Login efetuado com sucesso.")
                    Opcoes()
                else:
                    print("Senha incorreta.")
                    continue
        lerlogins.close()
        if not login_encontrado:
            print("Você não possui cadastro.")
            return login.strip(" ")
        break

# Função pra consultar e exibir informações do usuário
def Opcoes():
    while True:
        opcao = menu()
        lerlogins = open('logins.txt', 'r')
        if opcao ==  "1":
            senha_correta = False
            senha = input("Digite a sua senha de 6 dígitos: ")
            for linha in lerlogins.readlines():
                valores = linha.split('-')
                if senha == valores[2].split(':')[1].strip():
                    senha_correta = True
                    print("Nome: ", valores[0].split(':')[1].strip())
                    print("CPF: ", valores[1].split(':')[1].strip())
                    print("Reais: ", valores[5].split(':')[1].strip())
                    print("Bitcoin: ", valores[6].split(':')[1].strip())
                    print("Ethereum: ", valores[7].split(':')[1].strip())
                    print("Ripple: ", valores[8].split(':')[1].strip())
            continue
        elif opcao == "2":
            consultarExtrato()
            continue
        elif opcao == "3":
            Depositar()
            continue
        elif opcao == "4":
            Sacar()
            continue
        elif opcao == "5":
            comprarCripto()
            continue
        elif opcao == "6":
            venderCripto()
            continue
        elif opcao == "7":
            cotacao_bitcoin = 300000
            cotacao_ethereum = 15000
            cotacao_ripple = 5
            print("As cotações estão sendo atualizadas...")
            cotacao_bitcoin = atualizarCotacao(cotacao_bitcoin)
            cotacao_ethereum = atualizarCotacao(cotacao_ethereum)
            cotacao_ripple = atualizarCotacao(cotacao_ripple)
            print(f"Cotação atualizada: Bitcoin - {cotacao_bitcoin} / Ethereum - {cotacao_ethereum} / Ripple - {cotacao_ripple}")
            continue
        elif opcao == "8":
            print("Você selecionou a opção sair.")
            break
        else:
            print("Digite uma opção válida.")
            continue
        lerlogins.close()
        return

# Função pra comprar cripto
def comprarCripto():
    while True:
        cpf = input("Digite o seu CPF: ")
        senha = input("Digite a sua senha de 6 dígitos: ")
        with open("logins.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            encontrado = False
            for i, linha in enumerate(linhas):
                valores = linha.strip().split('-')
                cpf_arquivo = valores[1].split(':')[1].strip()
                senha_arquivo = valores[2].split(':')[1].strip()
                if cpf == cpf_arquivo and senha == senha_arquivo:
                    print("1 - Bitcoin")
                    print("2 - Ethereum")
                    print("3 - Ripple")
                    num = int(input("Digite o número correspondente à criptomoeda que deseja comprar: "))
                    valor = float(input("Digite o valor que deseja comprar: "))
                    
                    if num == 1:
                        cripto = "Bitcoin"
                        taxa = 0.02
                        cotacao = 30000
                    elif num == 2:
                        cripto = "Ethereum"
                        taxa = 0.01
                        cotacao = 1500
                    elif num == 3:
                        cripto = "Ripple"
                        taxa = 0.01
                        cotacao = 5
                    else:
                        print("Opção inválida.")
                        continue
                    
                    saldo_atual = float(valores[5].split(':')[1].strip())
                    saldo_cripto = float(valores[6 + num - 1].split(':')[1].strip())
                    
                    if saldo_atual >= valor:
                        saldo_atual -= valor
                        saldo_cripto += (valor / cotacao) * (1 - taxa)
                        
                        valores[5] = f"Saldo Reais: {saldo_atual:.2f}"
                        valores[6 + num - 1] = f"Saldo {cripto}: {saldo_cripto:.4f}"
                        
                        linhas[i] = '-'.join(valores) + '\n'
                        encontrado = True
        
        if encontrado:
            with open("logins.txt", "w") as arquivo:
                arquivo.writelines(linhas)
                with open('extrato.txt','a') as arquivo:
                    now = datetime.now()
                    data_hora = now.strftime("%d-%m-%Y %H:%M")
                    arquivo.write(f"{data_hora} - {valor:.2f} REAL CT: 0.0 TX: 0.00 REAL: {valor:.2f} : {cripto} : {saldo_cripto}\n")
                    print("Compra efetuada com sucesso.")
                    break
        else:
            print("CPF ou senha incorretos.")

# Função pra vender cripto
def venderCripto():
    while True:
        cpf = input("Digite o seu CPF: ")
        senha = input("Digite a sua senha de 6 dígitos: ")
        with open("logins.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            encontrado = False
            for i, linha in enumerate(linhas):
                valores = linha.strip().split('-')
                cpf_arquivo = valores[1].split(':')[1].strip()
                senha_arquivo = valores[2].split(':')[1].strip()
                if cpf == cpf_arquivo and senha == senha_arquivo:
                    print("1 - Bitcoin")
                    print("2 - Ethereum")
                    print("3 - Ripple")
                    num = int(input("Digite o número correspondente à criptomoeda que deseja vender: "))
                    valor = float(input("Digite o valor que deseja vender: "))
                    
                    if num == 1:
                        cripto = "Bitcoin"
                        taxa = 0.03
                        cotacao = 30000
                    elif num == 2:
                        cripto = "Ethereum"
                        taxa = 0.02
                        cotacao = 1500
                    elif num == 3:
                        cripto = "Ripple"
                        taxa = 0.01
                        cotacao = 5
                    else:
                        print("Opção inválida.")
                        continue
                    
                    saldo_atual = float(valores[5].split(':')[1].strip())
                    saldo_cripto = float(valores[6 + num - 1].split(':')[1].strip())
                    
                    quantidade_venda = valor / cotacao
                    if saldo_cripto >= quantidade_venda:
                        saldo_cripto -= valor
                        saldo_atual += (valor * taxa) * cotacao
                        
                        valores[5] = f"Saldo Reais: {saldo_atual:.2f}"
                        valores[6 + num - 1] = f"Saldo {cripto}: {saldo_cripto:.4f}"
                        
                        linhas[i] = '-'.join(valores) + '\n'
                        encontrado = True
        
        if encontrado:
            with open("logins.txt", "w") as arquivo:
                arquivo.writelines(linhas)
                with open('extrato.txt','a') as arquivo:
                    now = datetime.now()
                    data_hora = now.strftime("%d-%m-%Y %H:%M")
                    arquivo.write(f"{data_hora} + {valor:.2f} REAL CT: 0.0 TX: 0.00 REAL: {valor:.2f} : {cripto} : {saldo_cripto}\n")
                    print("Venda efetuada com sucesso.")
                    break
        else:
            print("CPF ou senha incorretos.")

# Função pra depositar
def Depositar(): 
    while True:
        cpf = input("Digite o seu CPF: ")
        senha = input("Digite a sua senha de 6 dígitos: ")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        
        if valor_deposito <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return
        
        with open("logins.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        for i, linha in enumerate(linhas):
            valores = linha.split('-')
            cpf_arquivo = valores[1].split(':')[1].strip()
            senha_arquivo = valores[2].split(':')[1].strip()

            if cpf == cpf_arquivo and senha == senha_arquivo:
                saldo_atual = float(valores[5].split(':')[1].strip())
                novo_saldo = saldo_atual + valor_deposito
                valores[5] = f"Saldo Reais: {novo_saldo:.2f}"
                linhas[i] = '-'.join(valores)
                encontrado = True
                break 

        if encontrado:
            with open("logins.txt", "w") as loginarquivo:
                loginarquivo.writelines(linhas)
            with open("extrato.txt", "a") as extratoarquivo:
                now = datetime.now()
                data_hora = now.strftime("%d-%m-%Y %H:%M")
                extratoarquivo.write(f"{data_hora} + {valor_deposito:.2f} REAL CT: 0.0 TX: 0.00 REAL: {valor_deposito}\n")
                print("Depósito efetuado com sucesso.")
                break
        else:
            print("CPF ou senha incorretos.")

# Função pra sacar
def Sacar(): 
    while True:
        cpf = input("Digite o seu CPF: ")
        senha = input("Digite a sua senha de 6 dígitos: ")
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        
        if valor_saque <= 0:
            print("O valor do saque deve ser maior que zero.")
            return
        
        with open("logins.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        for i, linha in enumerate(linhas):
            valores = linha.split('-')
            cpf_arquivo = valores[1].split(':')[1].strip()
            senha_arquivo = valores[2].split(':')[1].strip()

            if cpf == cpf_arquivo and senha == senha_arquivo:
                saldo_atual = float(valores[5].split(':')[1].strip())
                novo_saldo = saldo_atual - valor_saque
                valores[5] = f"Saldo Reais: {novo_saldo:.2f}"
                linhas[i] = '-'.join(valores)
                encontrado = True
                break 

        if encontrado:
            with open("logins.txt", "w") as loginarquivo:
                loginarquivo.writelines(linhas)
            with open("extrato.txt", "a") as extratoarquivo:
                now = datetime.now()
                data_hora = now.strftime("%d-%m-%Y %H:%M")
                extratoarquivo.write(f"{data_hora} - {valor_saque:.2f} REAL CT: 0.0 TX: 0.00 REAL: {valor_saque}\n")
                print("Saque efetuado com sucesso.")
                break
        else:
            print("CPF ou senha incorretos.")

# Função pra consultar extrato
def consultarExtrato():
    cpf = input("Digite o seu CPF: ")
    senha = input("Digite a sua senha de 6 dígitos: ")
    
    with open("logins.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    encontrado = False
    for linha in linhas:
        valores = linha.split('-')
        cpf_arquivo = valores[1].split(':')[1].strip()
        senha_arquivo = valores[2].split(':')[1].strip()
        
        if cpf == cpf_arquivo and senha == senha_arquivo:
            encontrado = True
            break
    
    if encontrado:
        nome_arquivo = f"extrato.txt"
        try:
            with open("extrato.txt", "r") as extratoarquivo:
                print(f"Extrato do CPF {cpf}:")
                print(extratoarquivo.read())
        except FileNotFoundError:
            print("Nenhuma transação encontrada.")
    else:
        print("CPF ou senha incorretos.")

# Função pra atualizar a cotação da criptomoeda
def atualizarCotacao(cotacao_atual):
    variacao = random.uniform(-0.05, 0.05)
    nova_cotacao = cotacao_atual * (1 + variacao)
    return round(nova_cotacao, 2)

# Chamada da função para iniciar o programa
while True:
    escolha = usuario()
    if escolha == "1":
        autenticar.Login()
        break
    elif escolha == "2":
        cadastro()
        break
    elif escolha == "0":
        print("Você selecionou a opção sair.")
        break
    else:
        print("Digite uma opção válida.")