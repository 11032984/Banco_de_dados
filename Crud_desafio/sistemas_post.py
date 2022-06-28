import sqlite3


def create_tables():
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()

    usuario_table = """
        CREATE TABLE IF NOT EXISTS usuarios(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          email TEXT NOT NULL,
          password TEXT NOT NULL

        )

    """
    cur.execute(usuario_table)
    con.commit()
    con.close()

#create_tables()

def post_tables():
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()


    post_table = """
        CREATE TABLE IF NOT EXISTS posts(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          usuario_id INTEGER NOT NULL,
          titulo TEXT NOT NULL,
          texto TEXT NOT NULL,
          FOREIGN KEY (usuario_id) REFERENCES usuarios(id)

          )


    """

    cur.execute(post_table)
    con.commit()
    con.close()


#post_tables()


def comentario_table():
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()


    sql_comentarios = """
     CREATE TABLE IF NOT EXISTS comentarios(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          usuario_id INTEGER NOT NULL,
          post_id TEXT NOT NULL,
          texto TEXT NOT NULL,
          FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
          FOREIGN KEY (post_id) REFERENCES post(id)

          )


    """
    cur.execute(sql_comentarios)
    con.commit()
    con.close()

#comentario_table()


def insert_usuario(nome, email, password):
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()

    sql_insert = f"""
        INSERT INTO
        usuarios (nome, email ,password)
        VALUES
        ('{nome}', '{email}', '{password}')

    """
    cur.execute(sql_insert)
    con.commit()
    con.close()

#insert_usuario("Joao", "joazinho@gmail.com", "551511788")



def insert_post(usuario_id, titulo, texto):
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()

    sql_insert = f"""
        INSERT INTO
        posts (usuario_id, titulo, texto)
        VALUES ({usuario_id}, '{titulo}', '{texto}')

    """
    cur.execute(sql_insert)
    con.commit()
    con.close()

#insert_post(2,'Jantando','Frango frito')

def insert_comentario(usuario_id, post_id, texto):
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()

    sql_coment = f"""
        INSERT INTO
        comentarios (usuario_id, post_id, texto)
        VALUES ({usuario_id},{post_id}, '{texto}')


    """
    cur.execute(sql_coment)
    con.commit()
    con.close()

#insert_comentario(3, 1, 'carne passou do ponto')

def select():
    con = sqlite3.connect('banco_de_dados.sqlite')

    sql_procurando = """
        SELECT  id, nome, email, password
        FROM usuarios

    """
    cur = con.cursor()
    cur.execute(sql_procurando)
    data = cur.fetchall()
    print(data)
    print()

    for i in data:
        print(i)

#select()

def editando(id, nome):
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()

    sql_editando = f"""
        UPDATE usuarios SET nome = '{nome}'
        WHERE id = {id}


    """
    cur.execute(sql_editando)
    con.commit()
    con.close()

#editando(1, "Duda")


def deletando(id):
    con = sqlite3.connect('banco_de_dados.sqlite')
    cur = con.cursor()

    sql_deletando = f"""
        DELETE FROM usuarios
        WHERE id = {id}

    """

    cur.execute(sql_deletando)
    con.commit()
    con.close()

#deletando(3)
