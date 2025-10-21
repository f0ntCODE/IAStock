import tkinter as tk
from tkinter import messagebox, filedialog
from Node import Node
from BuscaNP import buscaNP
from BuscaP import busca

class InterfaceEstoque:
   
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Estoque - Simulação de Caminhos")
        self.root.geometry("1400x850")
        self.root.configure(bg="#f0f0f0")

        # ===== CONFIGURAÇÕES DO GRID =====
        self.GRID_SIZE = 11
        self.CELL_SIZE = 50

        # ===== ESTADOS INICIAIS =====
        self.grid = [[0 for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        self.inicio = [1, 3]
        self.fim = [5, 8]
        self.caminho = []
        self.custo = 0
        self.modo_edicao = "inicio"

        # Obstáculos iniciais
        obstaculos = [[2,5], [3,5], [4,5], [6,3], [7,3], [8,3], [5,7]]
        for obs in obstaculos:
            self.grid[obs[0]][obs[1]] = 1

        # Instâncias das classes de busca
        self.busca_np = buscaNP()
        self.busca_p = busca()

        self.criar_interface()
        self.desenhar_grid()
        self.iniciar_grid()

    def criar_interface(self):
        """Cria a interface com painel de controles e painel do grid."""
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # ---- PAINEL ESQUERDO COM SCROLLBAR ----
        left_container = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        left_container.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        
        left_canvas = tk.Canvas(left_container, bg="white", highlightthickness=0, width=320)
        scrollbar = tk.Scrollbar(left_container, orient="vertical", command=left_canvas.yview)
        
        left_frame = tk.Frame(left_canvas, bg="white")
        
        left_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        canvas_frame = left_canvas.create_window((0, 0), window=left_frame, anchor="nw")
        
        def configure_scroll(event):
            left_canvas.configure(scrollregion=left_canvas.bbox("all"))
            canvas_width = event.width
            left_canvas.itemconfig(canvas_frame, width=canvas_width)
        
        left_frame.bind("<Configure>", configure_scroll)
        left_canvas.bind("<Configure>", lambda e: left_canvas.itemconfig(canvas_frame, width=e.width))
        
        def _on_mousewheel(event):
            left_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        left_canvas.bind_all("<MouseWheel>", _on_mousewheel)

        tk.Label(left_frame, text="Controles de Estoque", font=("Arial", 16, "bold"), 
                 bg="white", fg="#2c3e50").pack(pady=10)

        # ===== SELEÇÃO DE ALGORITMO =====
        algo_frame = tk.LabelFrame(left_frame, text="Algoritmo de Busca", 
                                   font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        algo_frame.pack(fill=tk.X, padx=10, pady=5)

        self.algoritmo_var = tk.StringVar(value="amplitude")
        
        todos_algoritmos = [
            ("Busca em Amplitude", "amplitude"),
            ("Busca em Profundidade", "profundidade"),
            ("Profundidade Limitada", "profundidadeLimitada"),
            ("Aprofundamento Iterativo", "aprofundamentoIterativo"),
            ("Busca Bidirecional", "bidirecional"),
            ("Greedy (Ganancioso)", "greedy"),
            ("A* (A-Estrela)", "a_estrela"),
            ("IDA* (AIA-Estrela)", "aia_estrela")
        ]
        for texto, valor in todos_algoritmos:
            tk.Radiobutton(algo_frame, text=texto, variable=self.algoritmo_var, 
                           value=valor, bg="white", font=("Arial", 10)).pack(anchor=tk.W, pady=2)

        # ===== CONFIGURAÇÕES =====
        limite_frame = tk.LabelFrame(left_frame, text="Configurações", 
                                     font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        limite_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(limite_frame, text="Limite de Profundidade:", bg="white", font=("Arial", 10)).pack(anchor=tk.W)
        self.limite_var = tk.IntVar(value=20) 
        tk.Scale(limite_frame, from_=1, to=50, orient=tk.HORIZONTAL,
                 variable=self.limite_var, bg="white").pack(fill=tk.X, pady=5)

        # ===== PONTOS NO DEPÓSITO =====
        estados_frame = tk.LabelFrame(left_frame, text="Pontos no Depósito", 
                                      font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        estados_frame.pack(fill=tk.X, padx=10, pady=5)
        self.inicio_label = tk.Label(estados_frame, text=f"Coleta: ({self.inicio[0]}, {self.inicio[1]})",
        bg="#d4edda", font=("Arial", 10, "bold"), relief=tk.RAISED, padx=10, pady=5)
        self.inicio_label.pack(fill=tk.X, pady=3)
        self.fim_label = tk.Label(estados_frame, text=f"Entrega: ({self.fim[0]}, {self.fim[1]})",
        bg="#f8d7da", font=("Arial", 10, "bold"), relief=tk.RAISED, padx=10, pady=5)
        self.fim_label.pack(fill=tk.X, pady=3)

        # ===== MODO DE EDIÇÃO =====
        modo_frame = tk.LabelFrame(left_frame, text="Modo de Edição", font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        modo_frame.pack(fill=tk.X, padx=10, pady=5)
        self.btn_inicio = tk.Button(modo_frame, text="Definir Coleta", command=lambda: self.set_modo("inicio"),
                                    bg="#28a745", fg="white", font=("Arial", 10, "bold"))
        self.btn_inicio.pack(fill=tk.X, pady=3)
        self.btn_fim = tk.Button(modo_frame, text="Definir Entrega", command=lambda: self.set_modo("fim"),
                                 bg="#dc3545", fg="white", font=("Arial", 10, "bold"))
        self.btn_fim.pack(fill=tk.X, pady=3)
        self.btn_obstaculo = tk.Button(modo_frame, text="Adicionar/Remover Prateleira", 
         command=lambda: self.set_modo("obstaculo"),
         bg="#6c757d", fg="white", font=("Arial", 10, "bold"))
        self.btn_obstaculo.pack(fill=tk.X, pady=3)

        # ===== RESULTADO DA BUSCA =====
        resultado_frame = tk.LabelFrame(left_frame, text="Resultado da Busca", font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        resultado_frame.pack(fill=tk.X, padx=10, pady=5)
        self.custo_label = tk.Label(resultado_frame, text="Custo: 0", font=("Arial", 14, "bold"), bg="white")
        self.custo_label.pack(pady=5)
        self.tamanho_label = tk.Label(resultado_frame, text="Tamanho do Caminho: 0", font=("Arial", 12), bg="white")
        self.tamanho_label.pack(pady=5)
        tk.Label(resultado_frame, text="Caminho:", font=("Arial", 10, "bold"), bg="white").pack(pady=(10, 5))
        caminho_scroll = tk.Scrollbar(resultado_frame)
        caminho_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.caminho_text = tk.Text(resultado_frame, height=8, width=30, yscrollcommand=caminho_scroll.set, font=("Arial", 9), bg="#f8f9fa")
        self.caminho_text.pack(fill=tk.BOTH, expand=True)
        caminho_scroll.config(command=self.caminho_text.yview)

        # ---- PAINEL DIREITO: GRID ----
        right_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        tk.Label(right_frame, text="Visualização do Depósito", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=10)
        
        self.canvas = tk.Canvas(right_frame, width=self.GRID_SIZE*self.CELL_SIZE, 
                                height=self.GRID_SIZE*self.CELL_SIZE, bg="white",
                                highlightthickness=2, highlightbackground="#2c3e50")
        self.canvas.pack(padx=20, pady=10)
        self.canvas.bind("<Button-1>", self.on_click_grid)
        
        # ===== BOTÕES DE AÇÃO =====
        acoes_frame = tk.Frame(right_frame, bg="white", padx=20, pady=10)
        acoes_frame.pack(fill=tk.X)
        
        self.btn_executar = tk.Button(acoes_frame, text="Executar Busca", command=self.executar_busca,
                                      bg="#007bff", fg="white", font=("Arial", 12, "bold"), height=2)
        self.btn_executar.pack(fill=tk.X, pady=3)
        
        botoes_frame = tk.Frame(acoes_frame, bg="white")
        botoes_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(botoes_frame, text="Resetar Depósito", command=self.resetar_grid,
                  bg="#6c757d", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
        
        tk.Button(botoes_frame, text="Criar/Importar Grid", command=self.iniciar_grid,
                  bg="#ffc107", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
        
        tk.Button(botoes_frame, text="Importar Mapa", command=self.importar_mapa,
                  bg="#17a2b8", fg="white", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=2, fill=tk.X, expand=True)
        
        self.caminho_label_grid = tk.Label(right_frame, text="Caminho: (nenhum)", font=("Arial", 11), 
                                           bg="white", fg="#2c3e50", wraplength=500, justify="left")
        self.caminho_label_grid.pack(pady=10)

        # ===== LEGENDA =====
        legenda_frame = tk.Frame(right_frame, bg="white", pady=10)
        legenda_frame.pack()
        legendas = [
            ("Livre", "white", "black"),
            ("Prateleira", "#34495e", "white"),
            ("Coleta", "#28a745", "white"),
            ("Entrega", "#dc3545", "white"),
            ("Caminho", "#3498db", "white")
        ]
        for i, (texto, bg, fg) in enumerate(legendas):
            frame = tk.Frame(legenda_frame, bg="white")
            frame.grid(row=i//3, column=i%3, padx=10, pady=3)
            tk.Label(frame, bg=bg, width=3, height=1, relief=tk.SOLID, borderwidth=1).pack(side=tk.LEFT, padx=(0,5))
            tk.Label(frame, text=texto, font=("Arial", 9), bg="white").pack(side=tk.LEFT)

    # ================== MÉTODOS AUXILIARES ==================
    def set_modo(self, modo):
        """Define o modo de edição: início, fim ou obstáculo."""
        self.modo_edicao = modo
        self.btn_inicio.config(relief=tk.RAISED)
        self.btn_fim.config(relief=tk.RAISED)
        self.btn_obstaculo.config(relief=tk.RAISED)
        if modo == "inicio":
            self.btn_inicio.config(relief=tk.SUNKEN)
        elif modo == "fim":
            self.btn_fim.config(relief=tk.SUNKEN)
        else:
            self.btn_obstaculo.config(relief=tk.SUNKEN)

    def desenhar_grid(self):
        """Desenha o grid no canvas com cores humanizadas para estoque."""
        self.canvas.delete("all")
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                x1, y1 = j*self.CELL_SIZE, i*self.CELL_SIZE
                x2, y2 = x1+self.CELL_SIZE, y1+self.CELL_SIZE
                cor = "white"
                texto = ""
                cor_texto = "black"

                if self.grid[i][j] == 1:
                    cor = "#34495e"
                elif [i,j] == self.inicio:
                    cor = "#28a745"
                    texto = "C"
                    cor_texto = "white"
                elif [i,j] == self.fim:
                    cor = "#dc3545"
                    texto = "E"
                    cor_texto = "white"
                elif self.esta_no_caminho(i,j):
                    cor = "#3498db"

                self.canvas.create_rectangle(x1,y1,x2,y2,fill=cor,outline="#95a5a6",width=1)
                if texto:
                    self.canvas.create_text((x1+x2)/2,(y1+y2)/2,text=texto,font=("Arial",20,"bold"),fill=cor_texto)

    def esta_no_caminho(self, x, y):
        """Verifica se a célula pertence ao caminho encontrado."""
        return any((x == estado[0] and y == estado[1]) for estado in self.caminho)

    def on_click_grid(self, event):
        """Edita o grid ao clicar, dependendo do modo selecionado."""
        j = event.x // self.CELL_SIZE
        i = event.y // self.CELL_SIZE
        if 0 <= i < self.GRID_SIZE and 0 <= j < self.GRID_SIZE:
            if self.modo_edicao == "inicio" and self.grid[i][j] != 1:
                self.inicio = [i,j]
                self.inicio_label.config(text=f"Coleta: ({i},{j})")
            elif self.modo_edicao == "fim" and self.grid[i][j] != 1:
                self.fim = [i,j]
                self.fim_label.config(text=f"Entrega: ({i},{j})")
            elif self.modo_edicao == "obstaculo" and [i,j] != self.inicio and [i,j] != self.fim:
                self.grid[i][j] = 0 if self.grid[i][j] == 1 else 1

            self.caminho = []
            self.desenhar_grid()

    def resetar_grid(self):
        """Reseta o grid, obstáculos e resultados."""
        self.grid = [[0 for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        obstaculos = [[2,5], [3,5], [4,5], [6,3], [7,3], [8,3], [5,7]]
        for obs in obstaculos:
            self.grid[obs[0]][obs[1]] = 1
        self.caminho = []
        self.custo = 0
        self.custo_label.config(text="Custo: 0")
        self.tamanho_label.config(text="Tamanho do Caminho: 0")
        self.caminho_text.delete(1.0,tk.END)
        self.caminho_label_grid.config(text="Caminho: (nenhum)")
        self.desenhar_grid()

    def executar_busca(self):
        """Executa o algoritmo de busca selecionado e atualiza resultados."""
        self.btn_executar.config(state=tk.DISABLED, text="Executando...")
        self.root.update()
        algoritmo = self.algoritmo_var.get()
        resultado = None

        try:
           
            if algoritmo == "amplitude":
                resultado = self.busca_np.amplitude(self.inicio, self.fim, self.GRID_SIZE, self.GRID_SIZE, self.grid)
            elif algoritmo == "profundidade":
                resultado = self.busca_np.profundidade(self.inicio, self.fim, self.GRID_SIZE, self.GRID_SIZE, self.grid)
            elif algoritmo == "profundidadeLimitada":
                resultado = self.busca_np.prof_limitada(self.inicio, self.fim, self.GRID_SIZE, self.GRID_SIZE, self.grid, self.limite_var.get())
            elif algoritmo == "aprofundamentoIterativo":
                resultado = self.busca_np.aprof_iterativo(self.inicio, self.fim, self.GRID_SIZE, self.GRID_SIZE, self.grid, self.limite_var.get())
            elif algoritmo == "bidirecional":
                resultado = self.busca_np.bidirecional(self.inicio, self.fim, self.GRID_SIZE, self.GRID_SIZE, self.grid)
            
            elif algoritmo == "greedy":
                resultado, custo = self.busca_p.greedy(self.inicio, self.fim, self.grid, self.GRID_SIZE, self.GRID_SIZE)
            elif algoritmo == "a_estrela":
                resultado, custo = self.busca_p.a_estrela(self.inicio, self.fim, self.grid, self.GRID_SIZE, self.GRID_SIZE)
            elif algoritmo == "aia_estrela":
                resultado, custo = self.busca_p.aia_estrela(self.inicio, self.fim, self.grid, self.GRID_SIZE, self.GRID_SIZE)

            # Atualiza resultados
            if resultado:
                self.caminho = resultado
                
                # Calcula custo apropriado
                if algoritmo in ["greedy", "a_estrela", "aia_estrela"]:
                    self.custo = custo
                else:
                    self.custo = len(resultado) - 1
                
                self.custo_label.config(text=f"Custo: {self.custo}")
                self.tamanho_label.config(text=f"Tamanho do Caminho: {len(resultado)}")
                self.caminho_text.delete(1.0, tk.END)
                caminho_str = " → ".join(f"({p[0]},{p[1]})" for p in resultado)
                self.caminho_text.insert(tk.END, caminho_str)
                self.caminho_label_grid.config(text=f"Caminho: {caminho_str}")
                self.desenhar_grid()
            else:
                messagebox.showwarning("Sem Solução", "Caminho não encontrado!")
                self.resetar_grid()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao executar busca: {e}")
            import traceback
            traceback.print_exc()
        finally:
            self.btn_executar.config(state=tk.NORMAL, text="Executar Busca")

    def importar_mapa(self):
        """Importa um mapa do arquivo mapa.txt e atualiza o grid."""
        arquivo = filedialog.askopenfilename(title="Selecione o arquivo mapa.txt",
                                             filetypes=[("Arquivos de Texto", "*.txt")])
        if arquivo:
            try:
                with open(arquivo, "r") as arq:
                    linhas = arq.readlines()
                
                if len(linhas) != self.GRID_SIZE:
                    messagebox.showerror("Erro", f"O mapa deve ter exatamente {self.GRID_SIZE} linhas.")
                    return

                novo_grid = []
                for linha in linhas:
                    valores = linha.strip().split()
                    if len(valores) != self.GRID_SIZE:
                        messagebox.showerror("Erro", f"Cada linha do mapa deve ter {self.GRID_SIZE} números.")
                        return
                    novo_grid.append([int(v) for v in valores])
                
                self.grid = novo_grid
                for i in range(self.GRID_SIZE):
                    for j in range(self.GRID_SIZE):
                        if self.grid[i][j] == 2:
                            self.inicio = [i,j]
                            self.grid[i][j] = 0
                        elif self.grid[i][j] == 3:
                            self.fim = [i,j]
                            self.grid[i][j] = 0

                self.inicio_label.config(text=f"Coleta: ({self.inicio[0]},{self.inicio[1]})")
                self.fim_label.config(text=f"Entrega: ({self.fim[0]},{self.fim[1]})")
                self.caminho = []
                self.desenhar_grid()
                messagebox.showinfo("Sucesso", "Mapa importado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao importar mapa: {e}")

    def iniciar_grid(self):
        escolha = messagebox.askquestion("Iniciar Grid",
                                         "Deseja importar um mapa do arquivo?\n\n"
                                         "Clique 'Sim' para importar ou 'Não' para criar manualmente no grid.")
        if escolha == "yes":
            self.importar_mapa()
        else:
            self.resetar_grid()


# ===== EXECUÇÃO =====
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceEstoque(root)
    root.mainloop()