from tinydb import TinyDB  as database, Query
# DB OPTIONS
db = database('./db.json', indent=4)
republic_db = db.table('republic')
user_db = db.table('user')
Republic = Query()
User     = Query()

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
    print("", end="\n")
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
    republic_db.remove(Republic.name == name)
    republic_users = user_db.search(Republic.republic == name)
    for attuser in republic_users:
        attuser = leave(attuser)
    
    print("Removido com Sucesso!")
    user = user_db.get(User.name == user['name'])
    return user

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

# STRING OPTIONS

def printRepublic(republic): 
    print(f"\nRepública: {republic['name']}\n-> Descrição: {republic['desc']}\n-> Proprietário: {republic['owner']}\n-> Receita: {republic['receipt']}")