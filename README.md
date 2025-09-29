📦 Gestão de Estoque - Simulação de Caminhos

Simulação interativa de caminhos em um depósito 🏭 usando Python + Tkinter. Teste algoritmos de busca e visualize rotas entre pontos de coleta e entrega!

🚀 Como Rodar

Abra o terminal.

Entre na pasta do projeto:

cd caminho/para/o/projeto


Execute:

python InterfaceEstoque.py


⚠️ Certifique-se de que Node.py e BuscaNP.py estão no mesmo diretório.

🎮 Como Usar

Escolher Modo

🟢 Definir Coleta (ponto inicial)

🔴 Definir Entrega (destino)

⬛ Adicionar/Remover Prateleira

Selecionar Algoritmo

Amplitude, Profundidade, Profundidade Limitada, Aprofundamento Iterativo ou Bidirecional

Executar Busca

Clique em ▶ Executar Busca

Caminho é exibido no painel + grid

Resetar Depósito

🔄 Limpa o grid e restaura obstáculos iniciais

🖌 Legenda do Grid
Cor	Significado
⚪ Branco	Célula Livre
⬛ Cinza	Prateleira
🟢 Verde	Coleta
🔴 Vermelho	Entrega
🔵 Azul	Caminho
💡 Dicas

Grid padrão: 11x11 (alterável em GRID_SIZE)

Ajuste o Limite de Profundidade para algoritmos que precisam

Obstáculos iniciais representam prateleiras e podem ser editados
