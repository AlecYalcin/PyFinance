from modules import authentication  as auth
from modules import republics       as republic

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
        user = auth.login()[0]
        print(user)
        if user:
            while(option > 0):
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
                elif option == 1:
                    republic.list()
                    republic.enter()
    elif option == 2:
        auth.register()
    elif option == 3:
        republic.list()
    elif option == 4:
        republic.read()