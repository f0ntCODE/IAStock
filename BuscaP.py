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
                suc = [] #cria vetor suc
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
        #h = sqrt(c1*(p1[0]-p2[0])*(p1[0]-p2[0]) + c2*(p1[1]-p2[1])*(p1[1]-p2[1])) #h recebe a distância euclidiana ponderada entre p1 e p2, onde c1 e c2 são os custos direcionais que ponderam cada eixo
        
        h = c1*fabs(p1[0]-p2[0]) + c2*fabs(p1[1]-p2[1])
        '''
        heurística recebe a multiplicação de c1 com o valor abosluto em float da direferença entre p1[0] e p2[0], somado com a mesma expressão da anterior, porém, com c2 e 'p's na posição [1]
        '''
        return h #retorne a heurística
    
    def isFinal(self, atual ,fim):
        xI, yI = atual[0], atual[1]
        xF, yF = fim[0], fim[1]
        
        if(xI == xF and yI == yF):
            print("CAMINHO ENCONTRADO")
            
            return True
        
        return False
# -----------------------------------------------------------------------------
# CUSTO UNIFORME
# -----------------------------------------------------------------------------
    def custo_uniforme(self,inicio,fim,mapa,nx,ny): # grid | custo uniforme exige coordenada início, fim, mapa, limite x e limite y do grid
        # Origem igual a destino
        if inicio == fim: #se a coordenada do inicio for igual à coordenada fim, chegou ao lugar
            return [inicio], 0 #retorne o início e o custo
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque() #tranformar variável lista em uma lista que opera em baixo nível (mais eficiente)
        t_inicio = tuple(inicio)   # grid | t_inicio recebe a variável início em forma de tupla
        raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid | raiz recebe o retorno do método NodeP
        lista.append(raiz) #do resultado da raiz, atribua-a na variável lista
    
        # Controle de nós visitados
        visitado = {tuple(inicio): raiz}    # grid | ?
        
        # loop de busca
        while lista: #enquanto não chegar ao fim da lista
            # remove o primeiro nó
            atual = lista.popleft() #na lista "atual", remova o primeiro nó da variável lista
            valor_atual = atual.v2 #da variável valor_atual, receba o valor 2 da lista "atual"
    
            # Chegou ao objetivo
            if (self.isFinal(atual.estado, fim)): #se o estado (x, y) da lista "atual" for igual ao fim (x,y)
                caminho = self.exibirCaminho(atual) #a lista caminho recebe do método exibirCaminho o retorno do processamento da lista "atual"
                return caminho, atual.v2 #retorne a lista caminho e o segundo valor da variável "atual"
            
            # Gera sucessores - grid
            filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid | lista filhos recebe o retorno do método sucessores_grid
    
            for novo in filhos: # grid | laço for para iterar sobre o nó filhos
                # custo acumulado até o sucessor
                v2 = valor_atual + novo[1] #variável v2 recebe "valor atual" acrescido do valor no vetor "novo" na posição 2 deste
                v1 = v2 #v1 recebe o mesmo que o v2
    
                t_novo = tuple(novo[0])       # grid | variável t_novo recebe o valor do vetor "novo" em formato de tupla, ou seja, imutáveis e ordenados
                if (t_novo not in visitado) or (v1<visitado[t_novo].v1) : # grid | se o valor do t_novo não estiver em variável visitado ou se o valor v2 for menor que o valor do vetor "visitado", na posição t_novo do valor v2...
                    filho = NodeP(atual,t_novo, v1, None, None, v2) # grid | variável filho recebe o valor da classe NodeP, preenchida com os parâmetros: atual, t_novo, v1, nada, nada e v2
                    visitado[t_novo] = filho # grid | o valor que estará na posição t_novo do vetor "visitado" recebe o valor de filho
                    self.inserir_ordenado(lista, filho) #chamada de método "inserir_ordenado", com parâmetros: lista e filho
        return None #retorne nada
# -----------------------------------------------------------------------------
# GREEDY
# -----------------------------------------------------------------------------
    def greedy(self,inicio,fim,mapa,nx,ny): # grid | método greedy recebe parâmetros: início, fim, o mapa, o eixo x e o eixo y
        # Origem igual a destino
        if inicio == fim: #se o valor do início for igual ao valor fim...
            print("INÍCIO É IGUAL A FIM")
            return [inicio], 0 #retorne valor início em formato de vetor e o custo 0
        
        print("INICIANDO ALGORITMO GREED")
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque() #transforme o vetor lista em deque, para melhoria na manipulação de fila/pilha
        t_inicio = tuple(inicio)   # grid | vetor t_inicio recebe a variável início em formato de tupla, isto é, imutável e ordenado
        raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid | variável "raiz" recebe o retorno do modelo NodeP, que recebe o t_inicio, 0, nada, nada e 0 também
        lista.append(raiz) #atribua à lista o valor da variável "raiz"
    
        # Controle de nós visitados
        visitado = {tuple(inicio): raiz}    # grid | variável visitada recebe uma lista de "inicio" em formato de tupla, até chegar à raiz
        
        # loop de busca
        while lista: #enquanto for possível iterar na lista...
            # remove o primeiro nó
            atual = lista.popleft() #variável "atual" recebe a variável "lista" com um valor retirado
            valor_atual = atual.v2 #variável "valor_atual" recebe o valor de atual.v2
    
            # Chegou ao objetivo
            if (self.isFinal(atual.estado, fim)): #se o estado do valor atual for igual ao fim...
                caminho = self.exibirCaminho(atual) #variável caminho recebe o retorno da rotina "exibirCaminho", recebendo como parâmetro o valor "atual"
                return caminho, atual.v2 #retorne o caminho e o v2 de atual
            
            # Gera sucessores - grid
            filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid | variável "filhos" recebe o retorna do método "sucessores_grid", que recebe os parâmetros: estado do atual, eixo x, eixo y e o mapa
    
            for novo in filhos: # grid | laço for-each dos valores do vetor "filhos"
                # custo acumulado até o sucessor
                v2 = valor_atual + novo[1] # valor v2 recebe a soma de valor atual com o segundo valor do vetor "novo"
                v1 = self.heuristica_grid(novo[0],fim) #variável v1 recebe o retorno do método "heurística_grid", recebendo parâmetros: primeiro valor do vetor "novo" e o valor fim  
    
                # Não visitado ou custo melhor
                t_novo = tuple(novo[0])       # grid | variável t_novo recebe o primeiro valor do vetor "novo", em formato de tupla, isto é, imutável e ordenado
                if (t_novo not in visitado) or (v1<visitado[t_novo].v1): # grid | se o valor de t_novo não existir no vetor "visitado" ou se valor de v2 for menor que a posição "t_novo" do vetor "visitado" x v2...
                    filho = NodeP(atual,t_novo, v1, None, None, v2) # grid | variável filho recebe o retorno da função NodeP, que recebe os parâmetros: atual, t_novo, v1, nada, nada, v2
                    visitado[t_novo] = filho # grid | posição t_novo no vetor "visitado" recebe o valor "filho"
                    self.inserir_ordenado(lista, filho) #execute a rotina "inserir_ordenado, com seguintes parâmetros: lista e filho"
                    
        return None, None #retorno vazio
# -----------------------------------------------------------------------------
# A ESTRELA
# -----------------------------------------------------------------------------
    def a_estrela(self,inicio,fim,mapa,nx,ny): # grid | método "a_estrela" recebe como parâmetros: início, fim, mapa, eixo x e eixo y
        
        print("INICIANDO ALGORITMO A*")
        # Origem igual a destino
        if inicio == fim: #se o valor início for igual ao valor fim...
            return [inicio] , 0 #retorne valor início em formato de vetor e o custo 0
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque() #variável "lista" se transforma em deque, para melhor eficiência quanto à manipulação de lista/fila
        t_inicio = tuple(inicio)   # grid | variável t_inicio recebe o valor de início em fomato de tupla, isto é, imutável e ordenado
        raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid | variável raiz recebe o valor do modelo NodeP, que recebe os parâmetros: nada, t_inicio, 0, nada, nada, 0
        lista.append(raiz) #atribua ao vetor "lista" o valor "raiz" 
    
        # Controle de nós visitados
        visitado = {tuple(inicio): raiz}    # grid | variável visitado recebe o valor início em formato de tupla, iterando do vetor "raiz"
        
        # loop de busca
        while lista: #enquanto for possível iterar no vetor "lista"
            # remove o primeiro nó
            atual = lista.popleft() #valor atual recebe a "lista" com um valor retirado
            valor_atual = atual.v2 #variável "valor_atual" recebe o valor atual.v2
    
            if(self.isFinal(atual.estado, fim)):
                
                print("Destino encontrado!")
                caminho = self.exibirCaminho(atual) #variável caminho recebe o retorno da rotina "exibirCaminho", atribuindo o valor "atual"
                return caminho, atual.v2 #retorne o valor caminho e o v2 do atual
            
            # Gera sucessores - grid
            filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid | vetor filhos recebe a rotina "sucessores_grid", que recebe os valores: estado do atual, valor x, valor y e o mapa
    
            for novo in filhos: # grid | laço for-each do vetor filhos
                # custo acumulado até o sucessor
                v2 = valor_atual + novo[1] #v2 recebe o valor de "valor_atual"somado com o segundo valor do vetor "novo"
                v1 = v2 + self.heuristica_grid(novo[0],fim) # variável v1 recebe a soma de v2 com o retorno da rotina "heurística_grid", que recebe o primeiro valor da lista "novo" e o valor fim  
    
                # Não visitado ou custo melhor
                t_novo = tuple(novo[0])       # grid | variável t_novo recebe o primeiro valor do vetor novo, em formato de tupla, isto é, ordenado e imutável
                if (t_novo not in visitado) or (v2<visitado[t_novo].v2): # grid | se o valor de t_novo não existir em vetor visistado ou se v2 for menor que a posição "t_novo" do vetor "visitado".v2... 
                    filho = NodeP(atual,t_novo, v1, None, None, v2) # grid | variável filho recebe o retorno do modelo NodeP, que recebe os parâmetros: atual, t_novo, v1, nada, nada, v2.
                    visitado[t_novo] = filho # grid | posição "t_novo" do vetor "visitado" recebe o valor filho
                    self.inserir_ordenado(lista, filho) # executar a função "inserir_ordenado", que recebe os parâmetros: lista e filho
        return None, None #retorno vazio
# -----------------------------------------------------------------------------
# AI ESTRELA
# -----------------------------------------------------------------------------       
    def aia_estrela(self,inicio,fim,mapa,nx,ny): # grid | função aia_estrela recebe os parâmetros: início, fim, mapa, eixo x e eixo y
        
        print("INICIANDO ALGORITMO AIA*")
        # Origem igual a destino
        if inicio == fim: #se o valor início for igual ao valor fim...
            return [inicio] , 0 #retorne valor início em formato de vetor e o custo 0
        
        limite = self.heuristica_grid(inicio,fim) #valor limite recebe o retorno da rotina "heurística_grid", que recebe os parâmetros: início e fim
        
        # Fila de prioridade baseada em deque + inserção ordenada
        lista = deque() # vetor "lista" recebe função deque(), para melhor eficiência quanto à manipulação de fila/pilha
        
        # Busca iterativa
        while True: #loop infinito
            lim_acima = [] #lim_acima é um vetor
            
            t_inicio = tuple(inicio)   # grid | variável t_início recebe o valor "início" em formato de tupla, isto é, ordenada e imutável
            raiz = NodeP(None, t_inicio,0, None, None, 0)  # grid | variável "raiz" recebe o modelo NodeP, com os parâmetros: nada, t_inicio, 0, nada, nada e 0
            lista.append(raiz) #atribua à "lista" o valor raiz
        
            # Controle de nós visitados
            visitado = {tuple(inicio): raiz}    # grid | variável "visitado" recebe o valor início em formato de tupla, iterando ao valor raiz
            
            # loop de busca
            while lista: # enquanto for possível iterar o vetor lista...
                # remove o primeiro nó
                atual = lista.popleft() #vetor "atual" recebe o valor lista se um método
                valor_atual = atual.v2 # valor_atual recebe o atual.v2
        
                # Chegou ao objetivo
                if (self.isFinal(atual.estado, fim)): #se o estado do valor atual for igual ao valor fim
                    caminho = self.exibirCaminho(atual) #valor caminho recebe o retorno da função "exibirCaminho", que recebe o parâmetro "atual"
                    return caminho, atual.v2 #retorne o valor caminho e o valor atual.v2
                
                # Gera sucessores - grid
                filhos = self.sucessores_grid(atual.estado,nx,ny,mapa) # grid | vetor filhos recebe o retorno da rotina "sucessoresGrid", que recebe os valores: estado do atual, eixo x, eixo y e o mapa
        
                for novo in filhos: # grid | laço for-each do vetor filhos
                    # custo acumulado até o sucessor
                    v2 = valor_atual + novo[1] # v2 recebe a soma do valor_atual com o segundo valor do vetor "novo"
                    v1 = v2 + self.heuristica_grid(novo[0],fim)  #v1 recebe a soma do v2 com o retorno da "heurística_grid", que recebe o primeiro valor do vetor "novo" e o valor fim
                
                    # Verifica se está dentro do limite
                    if v1<=limite: # se o v1 for menor ou igual a valor limite...
                        # Não visitado ou custo melhor
                        t_novo = tuple(novo[0])       # grid | t_novo recebe o primeiro valor do vetor "novo" em formato de tupla, isto é, imutável e ordenado
                        if (t_novo not in visitado) or (v2<visitado[t_novo].v2): # grid | se o valor t_novo não exisitir em "visitado" ou se v2 for menor que a posição "t_novo" do vetor "visitado".v2...
                            filho = NodeP(atual,t_novo, v1, None, None, v2) # grid | variável filho recebe o retorno do modelo "NodeP", que contém estes oarâmetros: atual, t_novo, v1, nada, nada e v2
                            visitado[t_novo] = filho # grid | a posição "t_novo" do vetor "visitado" recebe o valor filho
                            self.inserir_ordenado(lista, filho) #execute a rotina inserir_ordenado, com os parâmetros: lista e filhos
                    else: #senão...
                        lim_acima.append(v1) #atribua o v1 ao vetor "lim_acima"
    
            if(len(lim_acima) == 0):
                return None, None
            
            limite = sum(lim_acima)/len(lim_acima) #variável limite recebe o somatório de lim_acima dividido pelo tamanho do lim_acima
            lista.clear() #limpar a lista
            visitado.clear() #limpar vetor "visitado"               
                     
        return None, None #retorno vazio