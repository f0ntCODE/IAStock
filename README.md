📦 Gestão de Estoques - Previsão e Planejamento

Simulação interativa de Gestão de Estoques, permitindo prever necessidades e planejar reabastecimentos para reduzir rupturas 🏪. Visualize rotas no depósito, defina pontos de coleta e entrega, e teste diferentes estratégias de logística.

🚀 Como Rodar

Abra o terminal.

Navegue até a pasta do projeto:

cd caminho/para/o/projeto


Execute o arquivo principal:

python InterfaceEstoque.py


⚠️ Certifique-se de que os arquivos Node.py e BuscaNP.py estão na mesma pasta.

🎮 Como Usar

Selecionar Modo de Edição

🟢 Coleta: definir ponto inicial de retirada do estoque

🔴 Entrega: definir destino do produto

⬛ Prateleira/Ocupado: adicionar ou remover obstáculos no depósito

Escolher Algoritmo de Busca

Amplitude, Profundidade, Profundidade Limitada, Aprofundamento Iterativo ou Bidirecional

Executar Planejamento

Clique em ▶ Executar Busca

Caminho otimizado é exibido no painel e destacado no grid

Resetar Depósito

🔄 Limpa o grid e restaura os obstáculos iniciais

🖌 Legenda do Depósito
Cor	Significado
⚪ Branco	Célula Livre
⬛ Cinza	Prateleira/Ocupada
🟢 Verde	Ponto de Coleta
🔴 Vermelho	Ponto de Entrega
🔵 Azul	Caminho Planejado
💡 Funcionalidades

Simulação de rotas no depósito para otimizar retirada e entrega

Planejamento de reabastecimento baseado em obstáculos e limites de profundidade

Visualização interativa para facilitar tomada de decisão

Ajuste do grid e obstáculos para refletir cenários reais do estoque
