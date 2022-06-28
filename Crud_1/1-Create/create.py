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


def create(nome=None, codigo=None, quantidade=None, valor=None):
    # TODO: Implemente um método que cria um objeto Produto e retorna ele:
  produto = Produto(nome, codigo, quantidade, valor)
  return produto

  #print(produto.nome, produto.codigo, produto.quantidade, produto.valor)

def list_create(list_produtos):
    # TODO: Crie um método que receba a lista de tuplas parâmetros (nome, código, quantidade, valor)
    # e retorna uma lista de objecto Produto

    lista_retorno = []
    for i in list_produtos:
        lista_retorno.append(create(i[0], i[1], i[2], i[3]))
    return lista_retorno


itens = [["Bolo", 45804, 30, 26], ["Pizza", 20203, 10, 50], ["Brigadeiro", 50696, 500, 3]]
#print(create("Pizza", 20203, 10, 50))
produtos = list_create(itens)

for item in list_create(itens):
    print(f"{item.nome} - {item.codigo} - {item.quantidade} - {item.valor}")

#list_create(itens)
