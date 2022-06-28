class Produto(object):
    nome = None
    codigo = None
    quantidade = None
    valor = None

    def __init__(self, nome=None, codigo=None, quantidade=None, valor=None):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor = valor

lista_produtos = []

lista_produtos.append(Produto("Manga", "1211", 15, 1.5))
lista_produtos.append(Produto("Leite", "9912", 12, 3.44))
lista_produtos.append(Produto("Coca-cola", "2314", 24, 5.99))
lista_produtos.append(Produto("Bolo de Chocolate", "5541", 13, 12.99))
lista_produtos.append(Produto("Kit-Barbeador", "1123", 50, 21.2))


def read():
    # Leia e imprima todos os objetos da lista
    # Faça uma tabela onde:
    # ------------------------------------------
    # | CODIGO  | PRODUTO | QUANTIDADE | PREÇO |
    # ------------------------------------------
    print(" ------------------------------------------")
    print("| CODIGO  | PRODUTO | QUANTIDADE | PREÇO |")
    print(" ------------------------------------------")
    for i in lista_produtos:
        print(f"| {i.codigo} | {i.nome} | {i.quantidade} | {i.valor} | ")

    read()

def read_first():
    # Leia e imprima o primeiro objetos da lista
    # Faça uma tabela onde:
    # ------------------------------------------
    # | CODIGO  | PRODUTO | QUANTIDADE | PREÇO |
    # ------------------------------------------
    print(" ------------------------------------------")
    print("| CODIGO  | PRODUTO | QUANTIDADE | PREÇO |")
    print(" ------------------------------------------")
    for i in lista_produtos:
        print(f"| {i.codigo} | {i.nome} | {i.quantidade} | {i.valor}")
        return [0]


def read_item(codigo=None):
    # Leia e imprima o item que tenha o codigo informado,
    # se nao informado o codigo, retorne todos os elementos,
    # se nao existir, retorne uma tabela vazia,
    # Faça uma tabela onde:
    # ------------------------------------------
    # | CODIGO  | PRODUTO | QUANTIDADE | PREÇO |
    # ------------------------------------------
    for i in lista_produtos:
        print(f'| {i.codigo} |')

