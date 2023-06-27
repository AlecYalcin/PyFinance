from tinydb     import TinyDB       as database, Query

db = database('./db.json', indent=4)
user_db = db.table('user')
User     = Query()

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

def addBank():
    print('Alterar Telefone')