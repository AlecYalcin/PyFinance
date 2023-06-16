from tinydb import TinyDB  as database, Query
db = database('./db.json', indent=4)
user_db = db.table('user')

def login():
    name        = input("Nome do Usuário: ")
    password    = input("Senha do Usuário: ")

    UserQuery = Query()
    user = user_db.search(UserQuery.name == name and UserQuery.password == password)
    if not user == []:
        print("Usuário encontrado, Autenticando....")
        return user
    return False

def register():
    name        = input("Nome do Usuário: ")
    password    = input("Senha do Usuário: ")
    tel         = input("Telefone do Usuário: ")
    is_staff    = input("Você é um proprietário de República? [S/N]: ").upper()
    if is_staff == 'S': 
        is_staff = True
    else:
        is_staff = False

    user_db.insert(
        {'name': name, 'password': password, 'tel': tel, 'is_staff': is_staff, 'has_republic': False, 'republic': 'none'}
    )

def newPassword():
    print('Alterar Senha')

def newName():
    print('Alterar Nome')

def newTel():
    print('Alterar Telefone')