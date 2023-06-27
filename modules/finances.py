from modules    import republics    as republic
from tinydb     import TinyDB       as database, Query, table

db = database('./db.json', indent=4)
finance_db = db.table('finance')
republic_db = db.table('republic')
query = Query()

def create(republic, finance, value):

    finance_db.insert(
        {
            'republic': republic,
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

def pay(republic, finance):
    republic = republic_db.get(query.name == republic)
    finance  = finance_db.get((query.name == finance) & (query.republic == republic['name']))
    
    if republic['receipt'] >= finance['value']:
        republic_db.update({'receipt': republic['receipt'] - finance['value']}, query.name == republic['name'])
        finance_db.remove((query.name == finance['name']) & (query.republic == finance['republic']))
        print("Receita paga com sucesso!")
    else:
        print("Receita insuficiente para pagar essa despesa.")
        print("Adicione: R$" + str(finance['value'] - republic['receipt']))

def list(republic):
    finances = finance_db.search(query.republic == republic)
    print("", end="\n")
    for finance in finances:
        printFinance(finance)
    
    if finances == []:
        print("Sem despesas para pagar.")

# STRING OPTIONS
def printFinance(finance): 
    print(f"Finança: {finance['name']}\n-> Valor: R${finance['value']}")