import numpy as np
import networkx as nx
import random as rd
import matplotlib.pyplot as plt
import os

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_grafo(tam: int) -> list:
    print(
        "🔭 De Tatooine a Alderaan, e depois a Hoth,\n"
        "as rotas levam até Endor e Naboo,\n"
        "conectando os mundos da galáxia Star Wars\n"
        "em uma rede de esperança e aventura. 🌏"
    )
    
    print(f"Assumindo os planetas numerados de 0 a {tam}, criando as rotas...")
    
    mat_adj = np.random.randint(0, 2, size=(tam, tam))
    np.fill_diagonal(mat_adj, 0)
    mat_adj = np.maximum(mat_adj, mat_adj.T)
    
    return mat_adj

def main():
    while(True):
        clear()
        print("🌌 Força Jedi 🌌")
        print("1. Construir grafo")
        print("2. Visualizar conexões")
        print("0. Sair")
        opcao = -1
        while(opcao < 0 or opcao > 2):
            opcao = int(input("Digite a opção desejada: "))
            if(opcao < 0 or opcao > 2):
                print("⚠️ Opção inválida, tente novamente...")
        
        if opcao == 1:
            tam = int(input("Digite o tamanho da galáxia: "))
            mat_adj = gerar_grafo(tam)
            
            print("\n🪐 Gálaxia e planetas criados, hora de criar os caminhos interplanetários...\n")
               
        elif opcao == 2:
            try:
                pos = nx.spring_layout(nx.from_numpy_array(np.array(mat_adj)))
                G = nx.from_numpy_array(np.array(mat_adj))
                nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray')
                plt.title("Conexões da Galáxia")
                plt.show()
            except NameError:
                print("⚠️ Grafo ainda não foi criado. Por favor, construa o grafo primeiro.")
                
        elif opcao == 0:
            print("✨ Que a força esteja com você!")
            break
        
        input("Pressione qualquer teclar para continuar...")
        
if __name__ == "__main__":
    main()