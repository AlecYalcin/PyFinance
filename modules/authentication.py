from modules    import republics    as republic
from tinydb     import TinyDB       as database, Query

db = database('./db.json', indent=4)
user_db = db.table('user')

def login(name, password):
    UserQuery = Query()
    user = user_db.search(UserQuery.name == name and UserQuery.password == password)
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
            'republic': 'none'
        }
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

        if user['is_staff']:
            print("[6] Atualizar República")
            print("[7] Desfazer República")
        else:
            print("[6] Sair da República")
    else:
        if user['is_staff']:
            print('[1] Criar uma República')
        else:
            print("[1] Entrar em uma República")
    print("[0] Sair do Programa")
    option = int(input('Resposta: '))

    if not user['has_republic']:
        if not user['is_staff']:
            if option > 1:
                print("Você não pode realizar essa operação. Tente novamente.")
            elif option == 1:
                print("Escolha uma república a seguir: ")
                republic.list()
        else:
            if option > 1:
                print("Você não pode realizar essa operação. Tente novamente.")
            elif option == 1:
                name = input("Digite o nome da sua república: ") 
                desc = input("Descreva a sua república: ")
                republic.create(name, desc, user)
    else:
        if not user['is_staff']:
            print("Estudante")
        else:
            if option == 6:
                print("Para cada opção que quiser permanecer a mesma, simplesmente aperte enter. ")
                newName = input("Digite o novo Nome: ")
                newDesc = input("Digite a nova Descrição: ")
                republic.update(user['name'], newName, newDesc)

    print("", end="\n")
    return option
    
''' FUTURAS ATUALIZAÇÕES
def newPassword():
    print('Alterar Senha')

def newName():
    print('Alterar Nome')

def newTel():
    print('Alterar Telefone')
'''