def explorar_localizacao(localizacao, inventario, comando):
    mensagens = []
    opcoes = []

    if localizacao == "floresta":
        if comando == "norte":
            localizacao = "cabana"
            mensagens.append("Você encontra uma cabana abandonada.")
            opcoes.append({"texto": "Entrar na cabana", "comando": "explorar"})
        elif comando == "leste":
            localizacao = "rio"
            mensagens.append("Você chega a um rio de águas turbulentas.")
            opcoes.append({"texto": "Tentar atravessar a ponte", "comando": "atravessar"})
            opcoes.append({"texto": "Voltar para a floresta", "comando": "voltar"})
        else:
            mensagens.append("Você não pode ir nessa direção.")
    elif localizacao == "cabana":
        if comando == "explorar":
            if "chave" not in inventario:
                inventario.append("chave")
                mensagens.append("Dentro da cabana, você encontra uma chave enferrujada e a pega.")
            else:
                mensagens.append("Você já explorou a cabana e não encontra mais nada útil.")
            mensagens.append("Você decide voltar para a floresta.")
            opcoes.append({"texto": "Voltar para a floresta", "comando": "voltar"})
        elif comando == "voltar":
            localizacao = "floresta"
            mensagens.append("Você retorna para a floresta.")
    elif localizacao == "rio":
        if comando == "atravessar":
            if "chave" in inventario:
                localizacao = "pos_ponte"
                mensagens.append("Você atravessa a ponte com cuidado e entra em um lugar perigoso.")
                mensagens.append("Você pode explorar mais ao sul ou oeste, ou voltar para a floresta.")
                opcoes.append({"texto": "Ir para o sul", "comando": "sul"})
                opcoes.append({"texto": "Ir para o oeste", "comando": "oeste"})
                opcoes.append({"texto": "Voltar para a floresta", "comando": "voltar"})
            else:
                mensagens.append("A ponte é frágil e você precisa de algo para garantir sua segurança (talvez uma chave?).")
                opcoes.append({"texto": "Voltar para a floresta", "comando": "voltar"})
        elif comando == "voltar":
            localizacao = "floresta"
            mensagens.append("Você retorna para a floresta.")
    elif localizacao == "pos_ponte":
        mensagens.append("Você está em um lugar perigoso além do rio.")
        if comando == "sul":
            mensagens.append("Você explora ao sul, mas não encontra nada de interessante.")
        elif comando == "oeste":
            mensagens.append("Você explora ao oeste e vê sinais de uma caverna.")
        elif comando == "voltar":
            localizacao = "floresta"
            mensagens.append("Você retorna para a floresta.")
        opcoes.append({"texto": "Voltar para a floresta", "comando": "voltar"})
        opcoes.append({"texto": "Ir para o sul", "comando": "sul"})
        opcoes.append({"texto": "Ir para o oeste", "comando": "oeste"})

    return localizacao, inventario, mensagens, opcoes
