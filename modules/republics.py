from tinydb import TinyDB  as database, Query
db = database('./db.json', indent=4)
republic_db = db.table('republic')
Republic = Query()


def create(name, desc, owner):
    republic_db.insert(
        {
            'name': name,
            'desc': desc,
            'owner': owner['name']
        }
    )

    User     = Query()
    user_db = db.table('user')
    user_db.update({'has_republic': True}, User.name == owner['name'])
    user_db.update({'republic': name}    , User.name == owner['name'])

def read(name):
    republic = republic.search(Republic.name == name)
    printRepublic(republic[0])

def update(name, newName, newDesc):
    if not newName == '\n':
        republic_db.update({'name': newName}, Republic.name == name)
    if not newDesc == '\n':
        republic_db.update({'desc': newDesc}, Republic.name == name)

def delete(name):
    republic_db.remove(Republic.name == name)
    print("Removido com Sucesso!")
    return False

def search():
    text = input("Digite aqui o nome da república: ")

    for republic in republic_db:
        search = republic['name'].find(text)
        if search != -1:
            printRepublic(republic)

def list():
    print("Listando todas as Repúblicas...")
    for republic in republic_db:
        printRepublic(republic)

def printRepublic(republic): 
    print(f"República: {republic['name']}\n -> Descrição: {republic['desc']}\n -> Proprietário: {republic['owner']}")

def enter():
    print("Entrando em uma República...")