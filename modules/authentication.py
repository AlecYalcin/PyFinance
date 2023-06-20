from tinydb import TinyDB  as database, Query
db = database('./db.json', indent=4)
user_db = db.table('user')

def login(name, password):
    UserQuery = Query()
    user = user_db.search(UserQuery.name == name and UserQuery.password == password)
    if not user == []:
        print("Usuário encontrado, Autenticando....\n")
        return user
    return False

def register(name, password, tel, is_staff):
    if is_staff == 'S': 
        is_staff = True
    else:
        is_staff = False

    user_db.insert(
        {'name': name, 'password': password, 'tel': tel, 'is_staff': is_staff, 'has_republic': False, 'republic': 'none'}
    )

    return login(name, password)

def pyAuth(user):
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("Usuário Logado:", user['name'])
    # Ações de República
    if user['has_republic']:
        print("[1] Verificar República")
        print("[2] Verificar Despesas")
        print("[3] Adicionar Despesas")
        print("[4] Verificar Receita")
        print("[5] Adicionar Receita")
        print("[6] Sair da República")
    else:
        print("[1] Entrar em uma República")
    print("[0] Sair do Programa")
    option = int(input('Resposta: '))

    if user['has_republic']:
        print('É, irmão, você têm uma república.')
    print("", end="\n")
    return option
    
def newPassword():
    print('Alterar Senha')

def newName():
    print('Alterar Nome')

def newTel():
    print('Alterar Telefone')