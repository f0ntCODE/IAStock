# 📦 Gestão de Estoques - Previsão e Planejamento

Simulação interativa de Gestão de Estoques, permitindo prever necessidades e planejar reabastecimentos para reduzir rupturas 🏪. Visualize rotas no depósito, defina pontos de coleta e entrega, e teste diferentes estratégias de logística.

## 🚀 Como Rodar

1. Abra o terminal.

2. Navegue até a pasta do projeto:
```
  cd caminho/para/o/projeto
```

3. Execute o arquivo principal:
 ````
  python InterfaceGrafica.py
````
## 🎮 Como Usar

- Selecionar Modo de Edição

🟢 **Coleta**: definir ponto inicial de retirada do estoque

🔴 **Entrega**: definir destino do produto

⬛ **Prateleira/Ocupado**: adicionar ou remover obstáculos no depósito

- Escolher Algoritmo de Busca
  
Para algoritmos de busca não informada:
> Amplitude, Profundidade, Profundidade Limitada, Aprofundamento Iterativo ou Bidirecional

|Para algoritmo de busca ponderada
> Greedy, A*, AIA* e Custo Uniforme

- Executar Planejamento

Clique em **▶ Executar Busca**

Caminho otimizado é exibido no painel e destacado no grid

## 🖌 Legenda do Depósito

- Cor	Significado
  
  ⚪ Branco:	Célula Livre

  ⬛ Cinza:	Prateleira/Ocupada

  🟢 Verde:	Ponto de Coleta

  🔴 Vermelho:	Ponto de Entrega

  🔵 Azul:	Caminho Planejado

  💡 Funcionalidades:

  - Simulação de rotas no depósito para otimizar retirada e entrega

  - Planejamento de reabastecimento baseado em obstáculos e limites de profundidade

  - Visualização interativa para facilitar tomada de decisão

  - Ajuste do grid e obstáculos para refletir cenários reais do estoque
