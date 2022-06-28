import sqlite3

def create_table():

    con = sqlite3.connect('banco_teste.sqlite')
    cur = con.cursor()

    sql_create = """
    CREATE TABLE IF NOT EXISTS banco(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    data date NOT NULL,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    valor DECIMAL(10,2) NOT NULL DEFAULT 0.00

    )

    """
    cur.execute(sql_create)
    con.commit()
    con.close()

#create_table()


def insert(data,nome, tipo,valor):

    con = sqlite3.connect('banco_teste.sqlite')
    cur = con.cursor()

    sql_insert = f"""
        INSERT INTO
        banco (data, nome, tipo ,valor)
        VALUES
        ({data}, '{nome}' , '{tipo}' , {valor})

    """
    cur.execute(sql_insert)
    con.commit()
    con.close()

#insert(2022/12/10, "joazinho", "saque", 150)
#insert(2021/03/14, "maria", "saque", 300)
#insert(2052/11/24, "natalia", "deposito", 400)
#insert(1984/12/16, "amanda", "saque", 500)
#insert(1897/12/31, "lucas", "deposito", 600)



def select(id):
    con = sqlite3.connect('banco_teste.sqlite')
    cur = con.cursor()

    sql_select = f"""
        SELECT id
        FROM banco

    """

    cur.execute(sql_select)
    con.commit()
    con.close()


#select(4)

def select_list():
    con = sqlite3.connect('banco_teste.sqlite')

    sql_selecionando= """
        SELECT  data, nome, tipo ,valor
        FROM banco

    """
    cur = con.cursor()
    cur.execute(sql_selecionando)
    data = cur.fetchall()
    print(data)
    print()

    for i in data:
        print(i)

#select_list()


def update(id, nome):
    con = sqlite3.connect('banco_teste.sqlite')
    cur = con.cursor()

    sql_editando = f"""
        UPDATE banco SET nome = '{nome}'
        WHERE id = {id}


    """
    cur.execute(sql_editando)
    con.commit()
    con.close()

#update(2, "bloublou")
#update(1, "Julia")

def delete(id):

    con = sqlite3.connect('banco_teste.sqlite')
    cur = con.cursor()

    sql_delete = f"""
        DELETE FROM banco
        WHERE id = {id}

     """

    cur.execute(sql_delete)
    con.commit()
    con.close()

#delete(2)

def entradas():
        con = sqlite3.connect('banco_teste.sqlite')
        cur = con.cursor()

        sql_entrada = f"""
        SELECT tipo
        FROM banco
        WHERE tipo = 'entrada'

        """
        cur.execute(sql_entrada)
        data = cur.fetchall()
        con.close()
        return data
#entradas()
#print(entradas())

def saidas():
        con = sqlite3.connect('banco_teste.sqlite')
        cur = con.cursor()

        sql_saida = f"""

        SELECT tipo
        FROM banco
        WHERE tipo = 'saida'

        """
        cur.execute(sql_saida)
        data = cur.fetchall()
        con.close()
        return data

#saidas()
#print(saidas())

if __name__ == "__main__":
    pass
