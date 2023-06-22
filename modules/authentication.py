from tinydb     import TinyDB       as database, Query

db = database('./db.json', indent=4)
user_db = db.table('user')

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
    
''' FUTURAS ATUALIZAÇÕES
def logout():
    return False

def newPassword():
    print('Alterar Senha')

def newName():
    print('Alterar Nome')

def newTel():
    print('Alterar Telefone')

def addBank():
    print('Alterar Telefone')
'''