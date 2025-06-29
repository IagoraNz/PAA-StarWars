import numpy as np
import networkx as nx
import random as rd
import matplotlib.pyplot as plt
import time as t
import os
import tracemalloc

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
    
    for i in range(tam):
        print(mat_adj[i], end="\n")
    
    return mat_adj

def bfs(mat_adj: list, inicio: int, fim: int) -> list:
    print("🚀 Iniciando a busca em largura (BFS) entre os vértices ", inicio, "e", fim)
    
    visitados = [False] * len(mat_adj)
    fila = []

    fila.append((inicio, [inicio]))
    visitados[inicio] = True
    
    while fila:
        vertice, caminho = fila.pop(0)
        if vertice == fim:
            print(f"🌟 Caminho encontrado: {caminho}")
            return caminho
        for i in range(len(mat_adj[vertice])):
            if mat_adj[vertice][i] == 1 and not visitados[i]:
                visitados[i] = True
                fila.append((i, caminho + [i]))
    print("❌ Caminho não encontrado.")
    return []

def coletando_uso_memoria_bfs( mat_adj: list, inicio: int, fim: int) -> None:
    tracemalloc.start()
    
    bfs(mat_adj, inicio, fim)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return peak / 10**6

def main():
    while(True):
        clear()
        print("🌌 Força Jedi 🌌")
        print("1. Construir grafo")
        print("2. Visualizar conexões")
        print("3. Aplicar BFS")
        print("4. Animação do BFS passo a passo")
        print("0. Sair")
        opcao = -1
        while(opcao < 0 or opcao > 5):
            opcao = int(input("Digite a opção desejada: "))
            if(opcao < 0 or opcao > 5):
                print("⚠️ Opção inválida, tente novamente...")
        
        if opcao == 1:
            tam = int(input("Digite o tamanho da galáxia: "))
            mat_adj = gerar_grafo(tam)
            
            print("\n🪐 Gálaxia e planetas criados, hora de criar os caminhos interplanetários...\n")
               
        elif opcao == 2:
            try:
                pos = nx.spring_layout(nx.from_numpy_array(np.array(mat_adj)))
                G = nx.from_numpy_array(np.array(mat_adj))
                nx.draw(
                    G, pos, with_labels=True, node_color='skyblue', edge_color='gray',
                    node_size=900, edgecolors='#1a3a5a', linewidths=2
                )
                plt.title("Conexões da Galáxia")
                plt.show()
            except NameError:
                print("⚠️ Grafo ainda não foi criado. Por favor, construa o grafo primeiro.")
                
        elif opcao == 3:
            try:
                ini = t.time()
                res = bfs(mat_adj, 0, len(mat_adj) - 1)
                fim = t.time()
                print(f"🕒 Tempo de execução: {fim - ini:.4f} segundos")
                coletando_uso_memoria_bfs(mat_adj, 0, len(mat_adj) - 1)
            except NameError:
                print("⚠️ Grafo ainda não foi criado. Por favor, construa o grafo primeiro.")
                
        elif opcao == 4:
            try:
                print("🚀 Iniciando a animação do BFS passo a passo...")
                G = nx.from_numpy_array(np.array(mat_adj))
                pos = nx.spring_layout(G)
                visitados = [False] * len(mat_adj)
                fila = []
                fila.append((0, [0]))
                visitados[0] = True

                plt.ion()
                fig, ax = plt.subplots()
                nx.draw(
                    G, pos, with_labels=True, node_color='skyblue', edge_color='gray',
                    node_size=900, edgecolors='#1a3a5a', linewidths=2, ax=ax
                )
                plt.title("Animação do BFS")
                aresta_percorrida = []
                caminho_final = []
                encontrou = False
                while fila:
                    vertice, caminho = fila.pop(0)
                    if vertice == len(mat_adj) - 1:
                        print(f"🌟 Caminho encontrado: {caminho}")
                        caminho_final = caminho
                        encontrou = True
                        break
                    for i in range(len(mat_adj[vertice])):
                        if mat_adj[vertice][i] == 1 and not visitados[i]:
                            visitados[i] = True
                            fila.append((i, caminho + [i]))
                            aresta_percorrida.append((vertice, i))
                            nx.draw_networkx_nodes(
                                G, pos, nodelist=[i], node_color='orange',
                                node_size=900, edgecolors='#a35a1a', linewidths=2, ax=ax
                            )
                            nx.draw_networkx_edges(
                                G, pos, edgelist=[(vertice, i)], edge_color='blue', width=2, ax=ax
                            )
                            plt.pause(0.5)
                # Ao final, desenhar o menor caminho encontrado em vermelho
                if encontrou and len(caminho_final) > 1:
                    caminho_edges = [(caminho_final[j], caminho_final[j+1]) for j in range(len(caminho_final)-1)]
                    nx.draw_networkx_edges(
                        G, pos, edgelist=caminho_edges, edge_color='red', width=3, ax=ax
                    )
                    nx.draw_networkx_nodes(
                        G, pos, nodelist=caminho_final, node_color='red',
                        node_size=900, edgecolors='#a35a1a', linewidths=2, ax=ax
                    )
                    plt.title(f"Menor caminho: {caminho_final}")
                plt.ioff()
                plt.show()
            except NameError:
                print("⚠️ Grafo ainda não foi criado. Por favor, construa o grafo primeiro.")
        elif opcao == 5:
            resultados_memoria = []
            for i in range(15):
                print(f"Coletando uso de memória {i+1}/15...")
                resultados_memoria.append(coletando_uso_memoria_bfs(mat_adj, 0, len(mat_adj) - 1))
            print("📊 Resultados de uso de memória:")
            for i, uso in enumerate(resultados_memoria):
                print(f"Teste {i+1}: {uso:.2f} MB")
            media = sum(resultados_memoria) / len(resultados_memoria)
            print(f"📈 Uso médio de memória: {media:.2f} MB")

        elif opcao == 0:
            print("✨ Que a força esteja com você!")
            break
        
        input("Pressione qualquer teclar para continuar...")


        
if __name__ == "__main__":
    main()