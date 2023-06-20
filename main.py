import webbrowser
from modules import authentication  as auth
from modules import republics       as republic

def pyMain():
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("[1] Login")
    print("[2] Registro")
    print("[3] Listar Repúblicas")
    print("[4] Pesquisar por Repúblicas")
    print("[5] Informações sobre o PyFinance")
    print("[0] Sair do Programa")
    print("##################################")
    option = int(input("Resposta: "))
    print("##################################\n")
    return option

def pyInfo():
    print("Todas as informações sobre o projeto podem ser lidas no README.md presente no Repositório do GitHub")
    print("Link: https://github.com/AlecYalcin/PyFinance")
    print("Abrindo o link...")
    webbrowser.open('https://github.com/AlecYalcin/PyFinance')
    print("", end="\n")

option = 1
while (option > 0):
    option = pyMain()
    if option == 1:
        name        = input("Nome do Usuário: ")
        password    = input("Senha do Usuário: ")
        user = auth.login(name, password)[0]
        if user:
            while(option > 0):
                option = auth.pyAuth(user)
    elif option == 2:
        name        = input("Nome do Usuário: ")
        password    = input("Senha do Usuário: ")
        tel         = input("Telefone do Usuário: ")
        is_staff    = input("Você é um proprietário de República? [S/N]: ").upper()
        user = auth.register(name, password, tel, is_staff)
    elif option == 3:
        republic.list()
    elif option == 4:
        republic.read()
    elif option == 5:
        pyInfo()