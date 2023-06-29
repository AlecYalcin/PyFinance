from tinydb     import TinyDB           as database, Query
from modules.republics  import republicOptions

db = database('./db.json', indent=4)
user_db = db.table('user')
User     = Query()

#AUTHENTICATION
def login(name, password):
    UserQuery = Query()
    user = user_db.search((UserQuery.name == name) & (UserQuery.password == password))
    if not user == []:
        print("Usuário encontrado, Autenticando....\n")
        return user[0]
    return False

def register(name, password, tel, is_staff):
    if is_staff == 'S': 
        is_staff = True
    else:
        is_staff = False

    user_db.insert(
        {
            'name': name, 
            'password': password, 
            'tel': tel, 
            'is_staff': is_staff, 
            'has_republic': False, 
            'republic': 'none',
            'bank': 0
        }
    )

    return login(name, password)

#USER OPTIONS

def printUser(user):
    print(f"\n-> Usuário: {user['name']}\n-> Telefone: {user['tel']}\n-> Saldo: {user['bank']}\n-> República: {user['republic']}")

def newPassword(user, _password):
    if user['password'] == _password:
        print('Senha repetida, favor insira outra.')
    else:
        confirm = input('Digite a senha novamente: ')
        if confirm != _password:
            print('Confirmação de senha errada.')
        else:
            user_db.update({'password': _password}, User.name == user['name'])
            print('Senha alterada com sucesso.')
    
    user = user_db.get(User.name == user['name'])
    return user

def newName(user, _name):
    if user['name'] == _name:
        print('O nome de usuário é o mesmo.')
    else:
        confirm = user_db.get(User.name == _name)
        if not confirm:
            user_db.update({'name': _name}, User.name == user['name'])
            print('Nome alterado com sucesso.')
        else:
            print('Nome já existente, tente outro.')
    
    user = user_db.get(User.name == _name)
    return user

def newTel(user, _tel):
    if user['tel'] == _tel:
        print('O telefone de usuário é o mesmo.')
    else:
        confirm = user_db.get(User.tel == _tel)
        if not confirm:
            user_db.update({'tel': _tel}, User.name == user['name'])
            print('Telefone alterado com sucesso.')
        else:
            print('Telefone já existente, tente outro.')
    
    user = user_db.get(User.name == user['name'])
    return user

def addBank(user, _bank):
    user_db.update({'bank': user['bank']+_bank}, User.name == user['name'])
    user = user_db.get(User.name == user['name'])

    print("Valor atual: R$" + str(user['bank']))

    return user

def userOptions(user):
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("Usuário Logado: Teste")
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

    if option == 1:
        print("", end="\n")
        while(option > 0):
            option, user = republicOptions(user)
    elif option == 2:
        printUser(user)
    elif option == 3:
        _name = input("\nDigite seu novo nome: ")
        user = newName(user, _name)
    elif option == 4:
        _password = input("\nDigite sua nova senha: ")
        user = newPassword(user, _password)
    elif option == 5:
        _tel = input("\nDigite seu novo telefone: ")
        user = newTel(user, _tel)
    elif option == 6:
        _bank = float(input("\nDigite um valor para adicionar: R$"))
        user = addBank(user, _bank)
    
    if option == 0:
        print("", end="\n")
        option = -1
    elif option == -1:
        option = 8
    else:
        input()

    return option, user