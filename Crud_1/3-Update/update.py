class Agenda(object):
  codigo = None
  titulo = None
  horario = None
  data = None

  def __init__(self, codigo=None, titulo=None, horario=None, data=None):
    self.codigo = codigo
    self.titulo = titulo
    self.horario = horario
    self.data = data

  def __repr__(self) -> str:

   return (f'{self.titulo}, {self.horario}, {self.data}, {self.codigo}')

lista_agendamento = [
  Agenda(1, "Dentista", "13:11", "12/05/2022"),
  Agenda(2, "Entrega de Notas Escolares", "8:30", "28/05/2022"),
  Agenda(3, "Aniversario de Ana", "19:30", "15/07/2022"),
  Agenda(4, "Reunião", "15:30", "21/06/2022")
]


def update(codigo, titulo=None, horario=None, data=None):
  # TODO: Fazer a implementacao de update, recebendo o codigo do objeto
  # procurando na lista, e modificando o que for passado
  for i in lista_agendamento:
      if i.codigo ==int(codigo):
          if titulo:
            i.titulo = titulo
          if horario:
            i.horario = horario
          if data: data
          i.data = data
          return lista_agendamento


  return codigo

print(lista_agendamento)
update(2, titulo = "teste")
