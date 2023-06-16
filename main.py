from modules import authentication  as auth
from modules import republics       as republic
from tinydb  import TinyDB          as database
db = database('db.json')

option = 1
while (option > 0):
    print("##################################")
    print("            PyFinance             ")
    print("##################################")
    print("[1] Login")
    print("[2] Registro")
    print("[3] Listar Repúblicas")
    print("[4] Pesquisar por Repúblicas")
    print("[0] Sair do Programa")
    print("##################################")
    option = int(input("Resposta: "))
    print("##################################")

    if option == 1:
        auth.login()
    elif option == 2:
        auth.register()
    elif option == 3:
        republic.list()
    elif option == 4:
        republic.read()