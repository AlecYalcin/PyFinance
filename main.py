import webbrowser
from modules import users            as auth
from modules import republics       as republic
from modules import finances        as finance

def pyInfo():
    print("Todas as informações sobre o projeto podem ser lidas no README.md presente no Repositório do GitHub")
    print("Link: https://github.com/AlecYalcin/PyFinance")
    print("Abrindo o link...")
    webbrowser.open('https://github.com/AlecYalcin/PyFinance')
    print("##################################")

def pyAuth(user):
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("Usuário Logado:", user['name'])
    print("########### República ############")
    # Ações de República
    if user['has_republic']:
        print("[1] República:   (!) Verificar")
        print("[2] Despesas:    (!) Verificar")
        print("[3] Despesas:    (+) Adicionar")
        print("[4] Receita:     (+) Adicionar")
        print("[5] Receita:     (-) Pagar")

        if user['is_staff']:
            print("[6] República:   (?) Alterar")
            print("[7] República:   (*) Desfazer")
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

    print("############ Usuário #############")
    print("[8] Alterar Senha")
    print("[9] Alterar Nome")
    print("[10] Alterar Telefone")
    print("[0] Logout")
    print("##################################")
    option = int(input('Resposta: '))
    print("##################################")

    if option == 8:
        _password = input("Digite sua nova senha: ")
        user = auth.newPassword(user, _password)
    if option == 9:
        _name = input("Digite seu novo nome: ")
        user = auth.newName(user, _name)
    if option == 10:
        _tel = input("Digite seu novo telefone: ")
        user = auth.newTel(user, _tel)

    if not user['has_republic']:
        if not user['is_staff']:
            if option > 3 and option < 8:
                print("Você não pode realizar essa operação. Tente novamente.")
            elif option == 1:
                republicEnter = input("Escolha uma república: ")
                user = republic.enter(user, republicEnter)
        else:
            if option > 3 and option < 8:
                print("Você não pode realizar essa operação. Tente novamente.")
            elif option == 1:
                name = input("Digite o nome da sua república: ") 
                desc = input("Descreva a sua república: ")
                user = republic.create(name, desc, user)
        if option == 2:
            republic.list()
        if option == 3:
            republic.search()
    else:
        if option == 1:
            republic.read(user['republic'])
        if option == 2:
            finance.list(user['republic'])
        if option == 3:
            financeName = input("\nDigite o nome da Despesa: ")
            value       = float(input("Digite o valor da Despesa: R$"))
            finance.create(user['republic'], financeName, value)
        if option == 4:
            receipt = float(input("\nDigite a quantia: R$"))
            user = republic.addReceipt(user, receipt)
        if option == 5:
            financeName = input("\nDigite o nome da Despesa: ")
            finance.pay(user['republic'], financeName)

        if not user['is_staff']:
            if option == 6:
                user = republic.leave(user)
        else:
            if option == 6:
                newName = input("\nDigite o novo Nome: ")
                newDesc = input("Digite a nova Descrição: ")
                user = republic.update(user, newName, newDesc)
            if option == 7:
                user = republic.delete(user, user['republic'])
    if option == 0:
        print("", end="\n")
        option = -1
    else:
        input()
    return option, user

def pyMain():
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

option = 1
while (option != 0):
    option = pyMain()
    if option == 1:
        name        = input("Nome do Usuário: ")
        password    = input("Senha do Usuário: ")
        user = auth.login(name, password)
        if user:
            while(option > 0):
                option, user = pyAuth(user)
    elif option == 2:
        name        = input("Nome do Usuário: ")
        password    = input("Senha do Usuário: ")
        tel         = input("Telefone do Usuário: ")
        is_staff    = input("Você é um proprietário de República? [S/N]: ").upper()

        user = auth.register(name, password, tel, is_staff)
        if user:
            while(option > 0):
                option, user = pyAuth(user)
    elif option == 3:
        pyInfo()