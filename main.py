from modules import users as auth
from modules.screens import pyMain, pyInfo

option = 1
while (option != 0):
    option = pyMain()
    if option == 1:
        name        = input("Nome do Usuário: ")
        password    = input("Senha do Usuário: ")
        user = auth.login(name, password)
        if user:
            while(option > 0):
                option, user = auth.userOptions(user)
    elif option == 2:
        name        = input("Nome do Usuário: ")
        password    = input("Senha do Usuário: ")
        tel         = input("Telefone do Usuário: ")
        is_staff    = input("Você é um proprietário de República? [S/N]: ").upper()

        user = auth.register(name, password, tel, is_staff)
        if user:
            while(option > 0):
                option, user = auth.userOptions(user)
    elif option == 3:
        pyInfo()