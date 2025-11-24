

class MatrizAdjacencia:
    def __init__(self, matriz):
        self.matriz = []
        for i in range(0, matriz):
            self.matriz.append([])
            for j in range(0, matriz):
                self.matriz[i].append(0)

    def inserir_vertice(self):
        for i in self.matriz:
            i.append(0)
        self.matriz.append([0 for i in range(0, len(self.matriz)+1)])

    def remover_vertice(self, vertice):
        for i in self.matriz:
            i.pop(vertice)
        self.matriz.pop(vertice)

    def inserir_aresta(self, vertice_inicio, vertice_fim):
        self.matriz[vertice_inicio][vertice_fim] = 1
    
    def remover_aresta(self, vertice_inicio, vertice_fim):
        self.matriz[vertice_inicio][vertice_fim] = 0
    
    def calcular_grau_cada_vertice(self):
        vertice = 0
        for i in self.matriz:
            grau = 0
            vertice += 1
            for j in i:
                if j == 1:
                    grau += 1 
            print(f"Grau de saída do vértice {vertice}: {grau}")
    
    def calcular_grau_entrada(self):
        graus_entrada = [0] * len(self.matriz)
        for i in self.matriz:
            for n in range(0, len(self.matriz)):
                if i[n] == 1:
                    graus_entrada[n] += 1
        return graus_entrada
    
    def calcular_grau_saida(self):
        graus_saida = [0] * len(self.matriz)
        for idx, i in enumerate(self.matriz):
            for j in i:
                if j == 1:
                    graus_saida[idx] += 1
        return graus_saida
    
    def grau_vertices_direcionado(self):
        graus = {}
        entrada = self.calcular_grau_entrada()
        saida = self.calcular_grau_saida()
        for idx, i in enumerate(entrada):
                graus[f"Vértice: {idx}"] = {"Saída": saida[idx], "Entrada": i, "Total": saida[idx]+i}
        return graus
    
    def grau_vertices_nao_direcionado(self):
        graus = {}
        entrada = self.calcular_grau_entrada()
        for idx, i in enumerate(entrada):
            graus[f"Vértice: {idx}"] =  i
        return graus
    def verificar_aresta_existe(self, vertice_inicio, vertice_fim):
        if self.matriz[vertice_inicio][vertice_fim] == 1:
            return True
        return False
    
    def listar_vizinhos(self, vertice):
        lista = []
        for indice, valor in enumerate(self.matriz[vertice]):
            if valor == 1:
                lista.append(indice)
        return lista
    

    def verificar_se_percurso_existe(self, percurso:list):
        for i in range(len(percurso)-1):
                if not self.verificar_aresta_existe(percurso[i], percurso[i+1]):
                    return False
        return True
    
    def busca_profundidade(self, vertice_inicial):
        lista_visitados = []
        pilha = []
        pilha.append(vertice_inicial)
        encontrado = False
        while len(pilha) > 0:
            atual = pilha.pop()
            if(atual in lista_visitados or atual in pilha):
                continue

            lista_visitados.append(atual)
            
            for i in self.listar_vizinhos(atual):
                pilha.append(i)
        return lista_visitados

    def ciclo_det(self, vertice_inicial):
        visitados = set() 
        estrutura = {
            vertice_inicial: None
        }
        pilha = [vertice_inicial]
        while pilha:
            vertice_atual = pilha.pop()
            visitados.add(vertice_atual)
            for vizinho in self.listar_vizinhos(vertice_atual):
                if vizinho in pilha or vizinho in visitados: 
                    if not(estrutura[vertice_atual] == vizinho):
                        ciclo = [vertice_atual]
                        caminho = vertice_atual
                        while caminho != vizinho and caminho != None:
                            caminho = estrutura[caminho]
                            if caminho != None:
                                ciclo.append(caminho)
                        ciclo.reverse()
                        ciclo.append(vizinho)
                        return True, ciclo
                else:
                    pilha.append(vizinho)
                    estrutura[vizinho] = vertice_atual
        return False, []
                


if __name__ == "__main__":
    matriza = MatrizAdjacencia(3) # Criando um grafo com 3 vértices
    print("Grafo de 3 vértices: ", matriza.matriz) # Mostrando o grafo
    matriza.inserir_vertice() # Inserindo um vértice no grafo
    print("\n")
    print("Grafo de 4 vértices:", matriza.matriz) # Mostrando o grafo novamente
    matriza.remover_vertice(3) # Removendo o vértice adicionado
    matriza.inserir_aresta(0, 1) # Inserindo uma aresta entre o vértice 0 e o 1
    print("\n")
    print("Grafo de 3 vértices. Note que há uma aresta entre o 0 e o 1: ", matriza.matriz) # Mostrando o grafo novamente
    matriza.inserir_aresta(1, 2) # Inserindo uma aresta entre o vértice 1 e o 2
    matriza.inserir_aresta(2, 0) # Inserindo uma aresta entre o vértice 2 e o 0 
    print("\n")
    print("Grafo de 3 vértices. Note que há uma aresta entre o 0 e o 1, outra entre o 1 e o 2 e mais uma entre 2 e 0: ", matriza.matriz) # Mostrando o grafo novamente
    print("\n")
    print("Graus dos vértices: ", matriza.grau_vertices_direcionado()) # Mostrando o grau desse grafo direcionado
    print("\n")
    print("Vizinhos do vértice 1: ", matriza.listar_vizinhos(1)) # Mostrando os vizinhos do vértice 1

    print("\n")
    print("Verificando se o percurso existe: ", matriza.verificar_se_percurso_existe((2, 0, 1, 2, 0))) # Mostrando se o percurso existe
    
    # Tornando o grafo não direcionado
    matriza.inserir_aresta(0, 2)
    matriza.inserir_aresta(2, 1)
    matriza.inserir_aresta(1, 0)
    print("\n")

    print("Graus dos vértices: ", matriza.grau_vertices_nao_direcionado()) # Mostrando o grau desse grafo não direcionado

    matriz = MatrizAdjacencia(2)
    
    matriz_adjacencia = [
    #   A  B  C  D  E  F
        [0, 1, 1, 0, 0, 0],  # A
        [0, 0, 0, 1, 1, 0],  # B
        [0, 0, 0, 0, 0, 1],  # C
        [0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 1],  # E
        [0, 0, 0, 0, 0, 0]   # F
    ]
    matriz.matriz = matriz_adjacencia


    matriz_adjacencia_sem_ciclo = [ # A->C->F->E->B
    #   A  B  C  D  E  F
        [0, 1, 1, 0, 0, 0],  # A
        [1, 0, 0, 0, 0, 0],  # B
        [1, 0, 0, 0, 0, 1],  # C
        [0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 1],  # E
        [0, 0, 1, 0, 1, 0]   # F
    ]
    
    matriz_adjacencia_com_ciclo = [ # A->D->E->C->B->F
    #   A  B  C  D  E  F
        [0, 1, 0, 1, 0, 0],  # A
        [1, 0, 1, 0, 0, 1],  # B
        [0, 1, 0, 1, 0, 0],  # C
        [1, 0, 1, 0, 1, 0],  # D
        [0, 0, 0, 1, 0, 0],  # E
        [0, 1, 0, 0, 0, 0]   # F
    ]

    print("\n")
    matriz.matriz = matriz_adjacencia_sem_ciclo
    print("Busca por profundidade: ", matriz.busca_profundidade(0))
    print("Não há ciclos, portanto:", matriz.ciclo_det(0))

    matriz.matriz = matriz_adjacencia_com_ciclo

    print("Busca por profundidade: ", matriz.busca_profundidade(0))
    print("Aqui há ciclo, portanto: ",matriz.ciclo_det(0)) # A->D->C->B (Aí fica: 0, 3, 2, 1 porque são os indices deles)



