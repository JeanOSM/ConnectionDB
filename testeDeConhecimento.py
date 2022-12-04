import mysql.connector

class Celular:
    def __init__(self):
        self.id = 0
        self.descricao = ""
        self.marca = ""
        self.quantidade = 0
        self.valor = 0.0

def inserir(x):
    x = Celular()
    x.descricao = input("Descrição: ")
    x.marca = input("Marca:")
    x.quantidade = int(input("Quantidade:"))
    x.valor = float(input("Insira o valor:"))
    return x

def salvar(x):
    banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "2001",
        database = "algoritmos"
    )
    cursor = banco.cursor()

    sql = "INSERT INTO celular VALUES(%s,%s,%s,%s,%s)"
    valores = (None, x.descricao, x.marca, x.quantidade, x.valor)

    cursor.execute(sql,valores)
    banco.commit()
    cursor.close()
    banco.close()

    print("Itens cadastrados no Banco de Dados!")

def ler():
    banco = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "2001",
        database = "algoritmos"
    )

    cursor = banco.cursor()

    sql = "SELECT * FROM celular"
    cursor.execute(sql)
    lista = cursor.fetchall()

    vetor = [Celular()]* cursor.rowcount

    cont = 0

    for cel in lista:
        c = Celular()
        c.id = cel[0]
        c.descricao = cel[1]
        c.marca = cel[2]
        c.quantidade = cel[3]
        c.valor = cel[4]

        vetor[cont] = c
        cont +=1
    return vetor


cadastar = (input("deseja cadastrar:S/N"))
while ( cadastar != 'N'):
    ins = inserir(Celular())

    salvar(ins)

    cadastar = (input("deseja cadastrar outro item:S/N"))

lerr = input("Ver os dados salvos:S/N")

if (lerr == "S"):
    x= ler()

    for i in range(0,len(x)):
        l = x[i]
        print("id:", l.id, "\nDescrição:", l.descricao, "\nMarca:", l.marca, "\nQuantidade:", l.quantidade, "\nValor:", l.valor, "\n\n")

print("Fim do programa!")
