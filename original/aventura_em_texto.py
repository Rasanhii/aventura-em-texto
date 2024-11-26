import random


def mostrar_intro():
  print("\nBem-vindo à Aventura em Texto!")
  print("Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste.")


def obter_comando():
  comando = input("\nPara onde você vai? (norte, sul, leste, oeste, sair): ").lower()
  return comando


def processar_comando(comando, localizacao, inventario):
  if comando == "norte":
    if localizacao == "floresta":
      localizacao = "cabana"
      print("\nVocê encontra uma cabana abandonada.")
    else:
      print("\nVocê não pode ir para o norte daqui.")
  elif comando == "leste":
    if localizacao == "floresta":
      localizacao = "rio"
      print("\nVocê chega a um rio de águas turbulentas.")
    else:
      print("\nVocê não pode ir para o leste daqui.")
  elif comando == "sul":
    print("\nVocê não pode ir para o sul daqui.")
  elif comando == "oeste":
    print("\nVocê não pode ir para o oeste daqui.")
  elif comando == "sair":
    print("\nObrigado por jogar!")
    return "sair", localizacao, inventario
  else:
    print("\nComando inválido.")
  return comando, localizacao, inventario


def explorar_localizacao(localizacao, inventario):
  if localizacao == "cabana":
    print("\nDentro da cabana, você encontra uma chave enferrujada.")
    if "chave" not in inventario:
      inventario.append("chave")
  elif localizacao == "rio":
    print("\nHá uma ponte frágil sobre o rio.")
    if "chave" in inventario:
      print("Você usa a chave para destravar um mecanismo na ponte e atravessá-la.")
      localizacao = "tesouro"
      print("\nVocê encontrou um tesouro escondido! Parabéns!")
    else:
      print("Você precisa encontrar uma maneira de atravessar o rio.")
  return localizacao, inventario


def jogar():
  localizacao = "floresta"
  inventario = []
  mostrar_intro()


  while True:
    comando = obter_comando()
    comando, localizacao, inventario = processar_comando(comando, localizacao, inventario)
    if comando == "sair":
      break
    localizacao, inventario = explorar_localizacao(localizacao, inventario)


jogar()