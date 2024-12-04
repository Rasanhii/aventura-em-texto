import tkinter as tk

class JogoAventura:
    def __init__(self, root):
        self.root = root
        self.root.title("Em Busca do Tesouro")
        self.root.geometry("600x400")

        # Estado inicial do jogo
        self.localizacao = "floresta"
        self.inventario = []
        self.explorou_cabana = False

        # Tela inicial
        self.tela_inicial()

    def tela_inicial(self):
        """Exibe a tela inicial do jogo."""
        self.limpar_tela()

        titulo = tk.Label(self.root, text="Em Busca do Tesouro", font=("Arial", 24, "bold"))
        titulo.pack(pady=20)

        descricao = tk.Label(
            self.root,
            text="Bem-vindo ao jogo! Você está em uma floresta e precisa encontrar um tesouro\n"
                 "para salvar o seu vilarejo. O que deseja fazer?",
            font=("Arial", 14),
            wraplength=500,
            justify="center",
        )
        descricao.pack(pady=20)

        botoes_frame = tk.Frame(self.root)
        botoes_frame.pack()

        botao_jogar = tk.Button(botoes_frame, text="Jogar", font=("Arial", 14), command=self.introducao)
        botao_jogar.pack(side="left", padx=20)

        botao_sair = tk.Button(botoes_frame, text="Sair", font=("Arial", 14), command=self.root.quit)
        botao_sair.pack(side="left", padx=20)

    def introducao(self):
        """Exibe a introdução da história antes do início do jogo."""
        self.limpar_tela()

        introducao_texto = tk.Label(
            self.root,
            text="Você está em uma floresta escura e perigosa. O tesouro que você busca\n"
                 "é a única esperança para salvar seu vilarejo da destruição.\n\n"
                 "Sua missão é encontrar o tesouro, enfrentando desafios e tomando decisões sábias.\n"
                 "Boa sorte!",
            font=("Arial", 14),
            wraplength=500,
            justify="center",
        )
        introducao_texto.pack(pady=20)

        botao_continuar = tk.Button(self.root, text="Continuar", font=("Arial", 14), command=self.iniciar_jogo)
        botao_continuar.pack(pady=20)

    def iniciar_jogo(self):
        """Inicia a interface principal do jogo."""
        self.limpar_tela()

        # Configuração principal do jogo
        self.frame_texto = tk.Frame(self.root)
        self.frame_texto.pack(fill="both", expand=True)

        self.texto_localizacao = tk.Text(self.frame_texto, wrap="word", height=10, state="disabled")
        self.texto_localizacao.pack(fill="both", expand=True, padx=10, pady=5)

        self.label_inventario = tk.Label(self.root, text="Inventário: Nenhum item", font=("Arial", 12))
        self.label_inventario.pack(pady=5)

        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack()

        self.botao_sair = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.botao_sair.pack(pady=5)

        self.mostrar_localizacao()

    def limpar_tela(self):
        """Remove todos os widgets da tela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_localizacao(self):
        """Atualiza o texto da localização e o inventário."""
        descricao = self.descrever_localizacao()
        self.texto_localizacao.config(state="normal")
        self.texto_localizacao.delete(1.0, tk.END)
        self.texto_localizacao.insert(tk.END, descricao)
        self.texto_localizacao.config(state="disabled")

        inventario_str = ", ".join(self.inventario) if self.inventario else "Nenhum item"
        self.label_inventario.config(text=f"Inventário: {inventario_str}")

        self.atualizar_botoes()

    def descrever_localizacao(self):
        """Retorna a descrição da localização atual."""
        descricoes = {
            "floresta": "Você está em uma floresta escura. Pode ir para o norte até uma cabana, para o leste até um rio ou explorar outros caminhos.",
            "cabana": "Você encontrou uma cabana abandonada. O que deseja fazer?",
            "dentro_cabana": (
                "Você está dentro da cabana. Há poucos objetos aqui, mas parece que há algo no canto."
                if not self.explorou_cabana else
                "A cabana está vazia agora. Nada mais a explorar."
            ),
            "rio": "Você chegou a um rio com águas turbulentas. Há uma ponte que pode ser atravessada.",
            "bau": "Você encontrou um baú trancado. O que deseja fazer?",
            "pós-rio": "Você está em uma área além do rio. Ao sul, há algo interessante.",
        }
        return descricoes.get(self.localizacao, "Local desconhecido.")

    def atualizar_botoes(self):
        """Atualiza os botões baseados na localização."""
        for widget in self.frame_botoes.winfo_children():
            widget.destroy()

        botoes = {}
        if self.localizacao == "floresta":
            botoes = {
                "Norte": lambda: self.ir_para("cabana"),
                "Leste": lambda: self.ir_para("rio"),
                "Sul": self.explorar_sul,
                "Oeste": self.explorar_oeste,
            }
        elif self.localizacao == "cabana":
            botoes = {
                "Entrar na Cabana": self.explorar_cabana,
                "Voltar para Floresta": lambda: self.ir_para("floresta"),
            }
        elif self.localizacao == "dentro_cabana":
            if not self.explorou_cabana:
                botoes = {
                    "Pegar Chave": self.pegar_chave,
                }
            botoes["Voltar para Floresta"] = lambda: self.ir_para("floresta")
        elif self.localizacao == "rio":
            botoes = {
                "Atravessar a Ponte": lambda: self.ir_para("pós-rio"),
                "Voltar para Floresta": lambda: self.ir_para("floresta"),
            }
        elif self.localizacao == "pós-rio":
            botoes = {
                "Explorar Sul": lambda: self.ir_para("bau"),
                "Voltar para a Ponte": lambda: self.ir_para("rio"),
            }
        elif self.localizacao == "bau":
            if "chave" in self.inventario:
                botoes = {
                    "Abrir Baú": self.abrir_bau,
                }
            else:
                self.texto_localizacao.config(state="normal")
                self.texto_localizacao.insert(tk.END, "\nVocê precisa de uma chave para abrir o baú.\n")
                self.texto_localizacao.config(state="disabled")
            botoes["Voltar para a Ponte"] = lambda: self.ir_para("rio")

        for texto, comando in botoes.items():
            tk.Button(self.frame_botoes, text=texto, command=comando).pack(side="left", padx=5)

    def ir_para(self, localizacao):
        """Move o jogador para a nova localização."""
        self.localizacao = localizacao
        self.mostrar_localizacao()

    def explorar_cabana(self):
        """Entra e explora a cabana."""
        self.localizacao = "dentro_cabana"
        self.mostrar_localizacao()

    def pegar_chave(self):
        """Pega a chave dentro da cabana."""
        if "chave" not in self.inventario:
            self.inventario.append("chave")
            self.explorou_cabana = True
            self.texto_localizacao.config(state="normal")
            self.texto_localizacao.insert(tk.END, "\nParabéns, você pegou a chave!\n")
            self.texto_localizacao.config(state="disabled")
        self.atualizar_botoes()

    def explorar_sul(self):
        """Explora o sul da floresta."""
        self.texto_localizacao.insert(tk.END, "\nNão há nada interessante ao sul.\n")

    def explorar_oeste(self):
        """Explora o oeste da floresta."""
        self.texto_localizacao.insert(tk.END, "\nVocê encontrou um muro alto. Não dá para prosseguir.\n")

    def abrir_bau(self):
        """Abre o baú e adiciona o tesouro ao inventário."""
        if "tesouro" not in self.inventario:
            self.inventario.append("tesouro")
            self.texto_localizacao.config(state="normal")
            self.texto_localizacao.insert(tk.END, "\nParabéns! Você abriu o baú e encontrou um tesouro!\n")
            self.texto_localizacao.config(state="disabled")
        self.atualizar_botoes()


if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAventura(root)
    root.mainloop()
