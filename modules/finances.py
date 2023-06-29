from modules    import republics    as republic
from tinydb     import TinyDB       as database, Query, table

db = database('./db.json', indent=4)
finance_db = db.table('finance')
republic_db = db.table('republic')
query = Query()

def create(republic, finance, value):

    _finances = finance_db.search(query.republic == republic)
    idnumber = 1+len(_finances)

    finance_db.insert(
        {
            'republic': republic,
            'id': idnumber, 
            'name': finance,
            'value': value,
        }
    )

def read(republic, finance):
    finance = finance_db.get((query.republic == republic['name']) & (query.name == finance))
    return finance

def update(republic, finance):
    return False

def delete(republic, finance):
    republic = republic_db.get(query.name == republic)
    finance  = finance_db.get((query.name == finance) & (query.republic == republic['name']))

    return False

# OPTIONS

def payOptions(republic, finance):
    republic = republic_db.get(query.name == republic)
    finances = search(finance, republic)

    if finances == []:
        finance = finance_db.get(query.id == int(finance))

        if finance:
            pay(republic, finance)
        else:
            print("Essa despesa que você está procurando não existe. Talvez você quis pagar alguma dessas: ")
            list(republic['name'])
    elif len(finances) > 1:
        print("Várias despesas foram retornadas, digite o nome completo: \n")
        for finance in finances:
            printFinance(finance)
    else:
        finance = finances[0]
        pay(republic, finance)
        

def pay(republic, finance):
    if republic['receipt'] >= finance['value']:
            republic_db.update({'receipt': republic['receipt'] - finance['value']}, query.name == republic['name'])

            finances_len = len(finance_db.search(query.republic == republic['name']))
            for id in range(finance['id']+1, finances_len+1):
                finance_db.update({'id': id-1}, query.id == id)

            finance_db.remove((query.name == finance['name']) & (query.republic == finance['republic']))
            print("Despesa paga com sucesso!")
    else:
        print("Receita insuficiente para pagar essa despesa.")
        print("Adicione: R$" + str(finance['value'] - republic['receipt']))

def search(text, republic):
    finances = []

    for finance in finance_db:
        search = finance['name'].find(text)
        if search != -1 and finance['republic'] == republic['name']:
            finances.append(finance)

    return finances

def list(republic):
    finances = finance_db.search(query.republic == republic)
    print("", end="\n")
    for finance in finances:
        printFinance(finance)
    
    if finances == []:
        print("Sem despesas para pagar.")

def verify(republic):
    finances = finance_db.search(query.republic == republic)

    if len(finances) > 0:
        return True
    else:
        return False

# STRING OPTIONS
def printFinance(finance): 
    print(f"[{finance['id']}] Despesa: {finance['name']}\n-> Valor: R${finance['value']}")