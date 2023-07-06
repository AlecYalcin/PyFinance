import webbrowser
import os
import platform

from modules    import users, finances, republics

def osClear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def pyInfo():
    osClear()
    print("Todas as informações sobre o projeto podem ser lidas no README.md presente no Repositório do GitHub")
    print("Link: https://github.com/AlecYalcin/PyFinance")
    print("Abrindo o link...")
    webbrowser.open('https://github.com/AlecYalcin/PyFinance')
    print("##################################")
    input("Aperte ENTER para voltar a tela original...")

def pyMain():
    osClear()
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("[1] Login")
    print("[2] Registro")
    print("[3] Informações sobre o PyFinance")
    print("[0] Sair do Programa")
    print("##################################")
    option = int(input("Resposta: "))
    print("##################################\n")
    return option

def pyUser(user):
    osClear()
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("Usuário Logado:", user['name'])
    print("##################################")
    print("[1] Acessar República")
    print("[2] Informações da Conta")
    print("[3] Alterar Nome")
    print("[4] Alterar Senha")
    print("[5] Alterar Telefone")
    print("[6] Adicionar Saldo")
    print("[0] Logout")
    print("##################################")
    option = int(input('Resposta: '))
    print("##################################")
    return option

def pyRepublic(user):
    osClear()
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("Usuário Logado:", user['name'])
    print("########### República ############")
    # Ações de República
    if user['has_republic']:
        print("[1] Informações da República")
        print("[2] Lista de Despesas")
        print("[3] Adicionar Despesa")
        print("[4] Adicionar Receita")
        print("[5] Pagar Despesas")

        if user['is_staff']:
            print("[6] Modificar República")
            print("[7] Excluir República")
        else:
            print("[6] Sair da República")
    else:
        if user['is_staff']:
            print('[1] Criar uma República')
            print("[2] Listar Repúblicas")
            print("[3] Pesquisar por Repúblicas")
        else:
            print("[1] Entrar em uma República")
            print("[2] Listar Repúblicas")
            print("[3] Pesquisar por Repúblicas")
    print("[0] Voltar a Tela de Usuário")
    print("##################################")
    option = int(input('Resposta: '))
    print("##################################")
    return option