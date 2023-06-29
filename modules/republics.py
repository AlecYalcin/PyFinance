from tinydb     import TinyDB   as database, Query
from modules    import finances as finance

# DB OPTIONS
db = database('./db.json', indent=4)
republic_db = db.table('republic')
user_db     = db.table('user')
Republic    = Query()
User        = Query()

# CRUD
def create(name, desc, owner):

    republic_db.insert(
        {
            'name': name,
            'desc': desc,
            'owner': owner['name'],
            'receipt': 0
        }
    )

    user_db.update({'has_republic': True}, User.name == owner['name'])
    user_db.update({'republic': name}    , User.name == owner['name'])
    owner = user_db.get(User.name == owner['name'])

    return owner

def read(name):
    republic = republic_db.get(Republic.name == name)
    printRepublic(republic)

def update(user, newName, newDesc):

    if not newName == '\n' and not newDesc == '\n':
        republic_users = user_db.search(Republic.republic == user['republic'])
        republic_db.update({'name': newName, 'desc': newDesc}, Republic.name == user['republic'])
        for attuser in republic_users:
            user_db.update({'republic': newName}, User.name == attuser['name'])
    user = user_db.get(User.name == user['name'])

    return user

def delete(user, name):
    finances_db = db.table('finance')
    republic_finances = finances_db.search(Republic.republic == name)

    if republic_finances == []:
        republic_db.remove(Republic.name == name)
        republic_users = user_db.search(Republic.republic == name)
        for attuser in republic_users:
            attuser = leave(attuser)
        
        print("Removido com Sucesso!")
    else: 
        print("Ainda há despesas para se pagar, não foi possível efetuar a remoção.")
    user = user_db.get(User.name == user['name'])
    return user

# STRING OPTIONS

def printRepublic(republic): 
    print(f"\nRepública: {republic['name']}\n-> Descrição: {republic['desc']}\n-> Proprietário: {republic['owner']}\n-> Receita: {republic['receipt']}")

# USER OPTIONS

def search():
    text = input("Digite aqui o nome da república: ")

    for republic in republic_db:
        search = republic['name'].find(text)
        if search != -1:
            printRepublic(republic)
    print("", end="\n")

def list():
    print("Listando todas as Repúblicas...")
    for republic in republic_db:
        printRepublic(republic)
    print("", end="\n")

def enter(user, republic):
    print("Entrando da República...")
    republic = republic_db.search(Republic.name == republic)
    if not republic == []:
        republic = republic[0]
        user_db.update({'has_republic': True}, User.name == user['name'])
        user_db.update({'republic': republic['name']}, User.name == user['name'])
    else:
        print("Essa república não foi encontrada, tente com outra.")
    user = user_db.get(User.name == user['name'])

    return user

def leave(user):
    print("Saindo da República...")
    user_db.update({'has_republic': False}, User.name == user['name'])
    user_db.update({'republic': 'none'}, User.name == user['name'])
    
    user = user_db.get(User.name == user['name'])
    return user

def addReceipt(user, receipt):
    if not receipt > user['bank']:
        republic = republic_db.get(Republic.name == user['republic'])
        republic_db.update({'receipt': republic['receipt']+receipt}, Republic.name == republic['name'])
        user_db.update({'bank': user['bank']-receipt} , User.name == user['name'])
    else:
        print("Você não possui essa quantia para adicionar. ")

    user = user_db.get(User.name == user['name'])
    return user

def republicOptions(user):
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

    if not user['has_republic']:
        if not user['is_staff']:
            if option > 3 and option < 8:
                print("Você não pode realizar essa operação. Tente novamente.")
            elif option == 1:
                republicEnter = input("Escolha uma república: ")
                user = enter(user, republicEnter)
        else:
            if option > 3 and option < 8:
                print("Você não pode realizar essa operação. Tente novamente.")
            elif option == 1:
                name = input("Digite o nome da sua república: ") 
                desc = input("Descreva a sua república: ")
                user = create(name, desc, user)
        if option == 2:
            list()
        if option == 3:
            search()
    else:
        if option == 1:
            read(user['republic'])
        if option == 2:
            finance.list(user['republic'])
        if option == 3:
            financeName = input("\nDigite o nome da Despesa: ")
            value       = float(input("Digite o valor da Despesa: R$"))
            finance.create(user['republic'], financeName, value)
        if option == 4:
            receipt = float(input("\nDigite a quantia: R$"))
            user = addReceipt(user, receipt)
        if option == 5:
            if finance.verify(user['republic']):
                financeName = input("\nDigite o nome da Despesa ou seu ID: ")
                finance.payOptions(user['republic'], financeName)
            else:
                print("\nNão há despesas a pagar.")

        if not user['is_staff']:
            if option == 6:
                user = leave(user)
        else:
            if option == 6:
                newName = input("\nDigite o novo Nome: ")
                newDesc = input("Digite a nova Descrição: ")
                user = update(user, newName, newDesc)
            if option == 7:
                user = delete(user, user['republic'])

    if option == 0:
        print("", end="\n")
        option = -1
    else:
        input()
    return option, user