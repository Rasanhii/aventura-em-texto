def explorar_localizacao(localizacao, inventario):
  
  # CABANA
  if localizacao == "cabana":
    if "chave" not in inventario:
      print("Dentro da cabana, você encontra uma chave enferrujada.")
      inventario.append("chave")
    else:
      print("\nNada a explorar aqui")
    
    comando = input("\nDeseja sair da cabana? (sim, nao): ").lower()
    if comando == "sim":
      localizacao = "floresta"
      print("\nVocê saiu da casa e voltou para a floresta")

    elif comando == "nao":
      localizacao = "cabana"
      localizacao, inventario = explorar_localizacao(localizacao, inventario)
    else:
      print("\nComando inválido.")
      localizacao, inventario = explorar_localizacao(localizacao, inventario)

  # RIO
  elif localizacao == "rio":
    print("\nHá uma ponte frágil sobre o rio.")
    if "chave" in inventario:
      print("Você usa a chave para destravar um mecanismo na ponte e atravessá-la.")
      localizacao = "tesouro"
      print("\nVocê encontrou um tesouro escondido! Parabéns!")
    else:
      print("Você precisa encontrar uma maneira de atravessar o rio.")


  return localizacao, inventario