import BuscaNP

#implementando...
def transformarMapa(arquivoMapa):
    
    try:
        with open(arquivoMapa, 'i') as arquivo:
            mapa = []
            
            for linhaArquivo in arquivo:
                linhaArquivo = linhaArquivo.strip()
                
                if linhaArquivo:
                    linha = [int(x) for x in linhaArquivo.split()]
                    
                    mapa.append(linha)
        return mapa

    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado")
        
        return None
    

def main():

    print("-------Interface Gráfica Bonita-----------")
    print("------------BEM-VINDO(A)!-------------\n\n")

    mapa = open("recurso\mapa1.txt")
    st = []

    for n in range(10):
        st = n + 1

    '''coord1 = input("Digite a coordenada X: ")
    coord2 = input("Digite a coordenada Y: ")'''

    inicio = [1,3];
    fim = [5,8];

    BuscaNP.buscaNP.amplitude(None, inicio, fim, 11, 11, mapa)