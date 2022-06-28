
class Carro:

    def __init__(self, id, marca, modelo, placa, proprietario):
      self.id = id
      self.marca = marca
      self.modelo = modelo
      self.placa = placa
      self.proprietario = proprietario

    def info(self):
      print(f'{self.id} | {self.marca} | {self.modelo} | {self.placa} | {self.proprietario}' )
      #print(f"ID: {self.id}")
      #print(f"MARCA: {self.marca}")
      #print(f"MODELO: {self.modelo}")
      #print(f"PLACA: {self.placa}")
      #print(f"PROPRIETARIO: {self.proprietario}")

id = 1
memoria = []
if __name__ == "__main__":

    while True:
      print("1- Criar um Carro")
      print("2 Ver os Carros")
      print("3- Editar um Carro na Lista")
      print("4- Deletar um Carro na Lista")
      print("5- sair ")

      opcao = input("Escolha a opcão: ")

      if opcao == "1":
          marca = input("Informe a marca: ")
          modelo = input("Informe o modelo: ")
          placa = input("Informe a placa: ")
          proprietario = input("Informe o proprietario:  ")
          memoria.append(Carro(id,marca,modelo,placa,proprietario))
          id +=1

      elif opcao == "2":
        print(" ID | Marca | Modelo | Placa | Proprietario")
        for item in memoria:
            item.info()
        print()

      elif opcao == "3":
        id_carro = int(input("informe o ID do Carro: "))
        carro_existe = False
        for item in memoria:
            if id_carro == item.id:
                carro_existe = True
                item.info()
                print("1 - Placa")
                print("2 - Proprietario")
                print("3 - Ambos")
                print("Qualquer outra tecla para sair")
                edt = input("Digite oq voce gostaria de editar: ")
                if edt == "1":
                    item.placa = input("Digite a placa nova: ")
                elif edt == "2":
                  item.proprietario = input("Digite o novo proprietario: ")
                elif edt == "3":
                    item.placa = input("Digite a placa nova: ")
                    item.proprietario = input("Digite o novo proprietario: ")

      elif opcao == "4":
           id_carro = int(input("informe o ID do Carro: "))
           carro_existe = False
           for item in memoria:
               if id_carro == item.id:
                  carro_existe = True
                  item.info()
                  print("1- Voce realmente deseja DELETAR o carro? ")
                  print("Digite qualquer tecla para sair")
                  edt = input("Digite a opção: ")
                  if edt == "1":
                     memoria.remove(item)


      elif opcao == 5:
        pass
      else:
        print("Opcao Errada \n")

#OBS:
################
#1- create
#2- read
#3 - alter(edit)
#4 - drop(delet)
