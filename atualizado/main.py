import random
from explorar_localizacao import explorar_localizacao


def mostrar_intro():
  print("Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste.")


def obter_comando():
  comando = input("\nPara onde você vai? (norte, sul, leste, oeste, sair): ").lower()
  return comando


def processar_comando(comando, localizacao, inventario):

  # NORTE
  if comando == "norte":
    if localizacao == "floresta":
      localizacao = "cabana"
      print("\nVocê encontra uma cabana abandonada.")
    else:
      print("\nVocê não pode ir para o norte daqui.")


  # LESTE
  elif comando == "leste":
    if localizacao == "floresta":
      localizacao = "rio"
      print("\nVocê chega a um rio de águas turbulentas.")
    else:
      print("\nVocê não pode ir para o leste daqui.")


  # SUL
  elif comando == "sul":
    print("\nVocê não pode ir para o sul daqui.")


  # OESTE
  elif comando == "oeste":
    print("\nVocê não pode ir para o oeste daqui.")
  

  # SAIR
  elif comando == "sair":
    print("\nObrigado por jogar!")
    return "sair", localizacao, inventario
  
  # ERRO
  else:
    print("\nComando inválido.")
  return comando, localizacao, inventario



def jogar():
  print("\nBem-vindo à Aventura em Texto!")
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