from collections import deque
from NodeP import NodeP
from math import sqrt, fabs

class busca(object):
    
#--------------------------------------------------------------------------
# SUCESSORES PARA GRID
#--------------------------------------------------------------------------
    def sucessores_grid(self,st,nx,ny,mapa): #recebe  dimensãoX, dimensãoY e o mapa
        f = [] # f é vetor
        x, y = st[0], st[1] # var x recebe posição inicial do vetor st e y recebe segunda posição deste
        
        # DIREITA
        if y+1<ny:  #se ao andar 1 posição no st[1] for menor que o limite y
            if mapa[x][y+1]==0: #se ao andar no eixo y + 1 for 0 (caminho)
                suc = [] = #cria vetor suc
                suc.append(x) #atribui st[0] a suc
                suc.append(y+1) #atribui st[1] a suc
                custo = 5 #o custo é 5
                aux = [] #cria vetor auxiliar
                aux.append(suc) #atribui suc ao vetor aux
                aux.append(custo) #atribui 5 ao vetor aux
                f.append(aux) #atribui aux ao vetor f
 
        # ESQUERDA
        if y-1>=0: #se ao retroceder uma posição no st[1] for maior ou igual a 0 (limite negativo)
            if mapa[x][y-1]==0: #se ao andar no eixo y  - 1 for 0 (caminho)
                suc = [] #cria vetor suc
                suc.append(x) #atribui st[0] ao vetor suc
                suc.append(y-1) #atribui st[1] ao vetor suc
                custo = 7 #custo é 7
                aux = [] #cria vetor auxiliar
                aux.append(suc) #atribui suc ao vetor aux
                aux.append(custo) #atribui 7 ao vetor aux
                f.append(aux) #atribui aux ao vetor f
        
        # ABAIXO
        if x+1<nx: #se ao andar +1 no st[0] for menor que o limite do eixo x
            if mapa[x+1][y]==0: #se ao andar uma posição no eixo X for 0 (caminho)
                suc = [] #cria vetor suc
                suc.append(x+1) #atribui st[0] + 1 ao vetor suc
                suc.append(y)# atribui st[1] ao vetor suc
                custo = 2 #custo é 2
                aux = [] #criar vetor auxiliar
                aux.append(suc) #atribuir suc ao vetor aux
                aux.append(custo) #atribuir 2 ao vetor aux
                f.append(aux) #atribuir aux no vetor f
        
        # ACIMA
        if x-1>=0: #se ao retroceder -1 no vetor st[0] for maior ou igual a 0 (limite negativo)
            if mapa[x-1][y]==0: #se ao retroceder uma posição no eixo x for igual a 0 (caminho)
                suc = [] #criar vetor suc
                suc.append(x-1) #atribui st[0] ao vetor suc
                suc.append(y) #atribiu st[0] ao vetor suc
                custo = 3 #custo é 3
                aux = [] #criar vetor auxiliar
                aux.append(suc) #atribuir suc ao vetor aux
                aux.append(custo) #atribui 3 ao vetor aux
                f.append(aux) #atribui aux ao vetor f
        return f #retorne o vetor f

#--------------------------------------------------------------------------    
# INSERE NA LISTA MANTENDO-A ORDENADA
#--------------------------------------------------------------------------    
    def inserir_ordenado(self,lista, no): #exige lista e nó
        for i, n in enumerate(lista): #laço for para criar lista de tuplas enumeradas da lista informada
            if no.v1 < n.v1: #se valor1 do nó for menor que o valor1 de n (valor associado à tupla)
                lista.insert(i, no) #inserir na lista o índice e o valor do nó
                break #quebre o ciclo
        else:
            lista.append(no) #atribuir nó ao vetor lista
#--------------------------------------------------------------------------    
# EXIBE O CAMINHO ENCONTRADO NA ÁRVORE DE BUSCA
#--------------------------------------------------------------------------    
    def exibirCaminho(self,node): #recebe nó
        caminho = [] #criar vetor caminho
        while node is not None: #enquanto nó não estiver sem nada
            caminho.append(node.estado) #atribuir estado do nó ao vetor caminho
            node = node.pai #var nove recebe pai do mesmo nó
        caminho.reverse() #inverter a ordem da lista
        return caminho #retornar o vetor caminho

#--------------------------------------------------------------------------    
# GERA H - GRID
#--------------------------------------------------------------------------    
    def heuristica_grid(self,p1,p2): #exige posição1 e posição2
        if (p2[0]-p1[0])<0: #se a diferença entre vetor p2[0] e p1[0] for menor que 0
            c1 = 3 #variável c1 = 3
        else:
            c1 = 2 #variável c1 recebe 2
        if (p2[1]-p1[1])<0: #se a diferença entre vetor p2[1] e p1[1] for menor que 0
            c2 = 7 #variável c2 recebe 7
        else:
            c2 = 5 #variável c2 recebe 5
        h = sqrt(c1*(p1[0]-p2[0])*(p1[0]-p2[0]) + c2*(p1[1]-p2[1])*(p1[1]-p2[1])) '''var h recebe: 
        a raiz quadrada da multiplicação das diferenças entre p1[0] e p2[0], multiplicado por c1 mais a multiplicação 
        entre as diferenças entre p1[1] e p2[1]
        '''
        #h = c1*fabs(p1[0]-p2[0]) + c2*fabs(p1[1]-p2[1])
        '''
        
        '''
        return h
# -----------------------------------------------------------------------------
# CUSTO UNIFORME
# -----------------------------------------------------------------------------
    def custo_uniforme(self,inicio,fim,mapa,nx,ny): # grid
        # Origem igual a destino
        if inicio == fim:
            return [inicio]
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque()
        t_inicio = tuple(inicio)   # grid
        raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid
        lista.append(raiz)
    
        # Controle de nós visitados
        visitado = {tuple(inicio): raiz}    # grid
        
        # loop de busca
        while lista:
            # remove o primeiro nó
            atual = lista.popleft()
            valor_atual = atual.v2
    
            # Chegou ao objetivo
            if atual.estado == fim:
                caminho = self.exibirCaminho(atual)
                return caminho, atual.v2
            
            # Gera sucessores - grid
            filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid
    
            for novo in filhos: # grid
                # custo acumulado até o sucessor
                v2 = valor_atual + novo[1]
                v1 = v2 
    
                # Não visitado ou custo melhor
                t_novo = tuple(novo[0])       # grid
                if (t_novo not in visitado) or (v2<visitado[t_novo].v2): # grid
                #if (novo[0] not in visitado) or (v2 < visitado[novo[0]].v2):
                    filho = NodeP(atual,t_novo, v1, None, None, v2) # grid
                    visitado[t_novo] = filho # grid
                    self.inserir_ordenado(lista, filho)
        return None
# -----------------------------------------------------------------------------
# GREEDY
# -----------------------------------------------------------------------------
    def greedy(self,inicio,fim,mapa,nx,ny): # grid
        # Origem igual a destino
        if inicio == fim:
            return [inicio]
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque()
        t_inicio = tuple(inicio)   # grid
        raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid
        lista.append(raiz)
    
        # Controle de nós visitados
        visitado = {tuple(inicio): raiz}    # grid
        
        # loop de busca
        while lista:
            # remove o primeiro nó
            atual = lista.popleft()
            valor_atual = atual.v2
    
            # Chegou ao objetivo
            if atual.estado == fim:
                caminho = self.exibirCaminho(atual)
                return caminho, atual.v2
            
            # Gera sucessores - grid
            filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid
    
            for novo in filhos: # grid
                # custo acumulado até o sucessor
                v2 = valor_atual + novo[1]
                #v1 = self.heuristica_grafo(nos,novo[0],fim) 
                v1 = self.heuristica_grid(novo[0],fim)  
    
                # Não visitado ou custo melhor
                t_novo = tuple(novo[0])       # grid
                if (t_novo not in visitado) or (v2<visitado[t_novo].v2): # grid
                #if (novo[0] not in visitado) or (v2 < visitado[novo[0]].v2):
                    filho = NodeP(atual,t_novo, v1, None, None, v2) # grid
                    #visitado[novo[0]] = filho #grafo
                    visitado[t_novo] = filho # grid
                    self.inserir_ordenado(lista, filho)
        return None
# -----------------------------------------------------------------------------
# A ESTRELA
# -----------------------------------------------------------------------------
    def a_estrela(self,inicio,fim,mapa,nx,ny): # grid
        # Origem igual a destino
        if inicio == fim:
            return [inicio]
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque()
        t_inicio = tuple(inicio)   # grid
        raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid
        lista.append(raiz)
    
        # Controle de nós visitados
        visitado = {tuple(inicio): raiz}    # grid
        
        # loop de busca
        while lista:
            # remove o primeiro nó
            atual = lista.popleft()
            valor_atual = atual.v2
    
            # Chegou ao objetivo
            if atual.estado == fim:
                caminho = self.exibirCaminho(atual)
                return caminho, atual.v2
            
            # Gera sucessores - grid
            filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid
    
            for novo in filhos: # grid
                # custo acumulado até o sucessor
                v2 = valor_atual + novo[1]
                v1 = v2 + self.heuristica_grid(novo[0],fim)  
    
                # Não visitado ou custo melhor
                t_novo = tuple(novo[0])       # grid
                if (t_novo not in visitado) or (v2<visitado[t_novo].v2): # grid
                    filho = NodeP(atual,t_novo, v1, None, None, v2) # grid
                    visitado[t_novo] = filho # grid
                    self.inserir_ordenado(lista, filho)
        return None
# -----------------------------------------------------------------------------
# AI ESTRELA
# -----------------------------------------------------------------------------       
    def aia_estrela(self,inicio,fim,mapa,nx,ny): # grid
        # Origem igual a destino
        if inicio == fim:
            return [inicio]
        
        limite = self.heuristica_grid(inicio,fim)
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque()
        
        
        # Busca iterativa
        while True:
            lim_acima = []
            
            t_inicio = tuple(inicio)   # grid
            raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid
            lista.append(raiz)
        
            # Controle de nós visitados
            visitado = {tuple(inicio): raiz}    # grid
            
            # loop de busca
            while lista:
                # remove o primeiro nó
                atual = lista.popleft()
                valor_atual = atual.v2
        
                # Chegou ao objetivo
                if atual.estado == fim:
                    caminho = self.exibirCaminho(atual)
                    return caminho, atual.v2
                
                # Gera sucessores - grid
                filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid
        
                for novo in filhos: # grid
                    # custo acumulado até o sucessor
                    v2 = valor_atual + novo[1]
                    v1 = v2 + self.heuristica_grid(novo[0],fim)  
                
                    # Verifica se está dentro do limite
                    if v1<=limite:
                        # Não visitado ou custo melhor
                        t_novo = tuple(novo[0])       # grid
                        if (t_novo not in visitado) or (v2<visitado[t_novo].v2): # grid
                            filho = NodeP(atual,t_novo, v1, None, None, v2) # grid
                            visitado[t_novo] = filho # grid
                            self.inserir_ordenado(lista, filho)
                    else:
                        lim_acima.append(v1)
            
            limite = sum(lim_acima)/len(lim_acima)
            lista.clear()
            visitado.clear()
            filhos.clear()
                        
        return None
