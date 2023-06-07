from getpass import getpass
from hashlib import sha256

def registro():
    arq = open("cadastros.txt", "a")
    user = input('Digite um Usuário: ')
    senha = sha256(getpass('Digite uma Senha: ').encode()).hexdigest()
    confirm_senha = sha256(getpass('Confirme a Senha: ').encode()).hexdigest()

    if senha != confirm_senha:
        print('As senhas são diferentes, tente novamente!')
        registro()
    
    arq.write(f"{user},{senha}\n")
    print('Conta registrada com sucesso!')
    arq.close()

def login():
    contas = open("cadastros.txt", 'r')
    listaLogin = contas.readlines()
    contas.close()

    user = input('Digite o Usuário: ')
    senha = sha256(getpass('Digite a Senha: ').encode()).hexdigest()

    for cadastro in listaLogin:
        dados = cadastro.strip().split(',')
        if user == dados[0]:
            if senha == dados[1]:
                print("Bem Vindo!!!")
            else:
                print("Senha Incorreta!!")
def possui_conta():
    possui_conta = input('Você possui conta? (Digite s para Sim ou n para Não)').lower()
    if possui_conta == 'n':
        registro()
    elif possui_conta == 's':
        login()
    else:
        print('Você digitou uma opção invalida, tente novamente!')
        possui_conta()
