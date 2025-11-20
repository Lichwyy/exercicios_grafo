
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

queue = []


class MatrizAdjacencia:
    def __init__(self, matriz):
        self.matriz = []
        for i in range(0, matriz):
            self.matriz.append([])
            for j in range(0, matriz):
                self.matriz[i].append(0)
        self.queue = []
        self.visitados = []
    def listar_vizinhos(self, vertice):
        lista = []
        for indice, valor in enumerate(self.matriz[vertice]):
            if valor == 1:
                lista.append(indice)
        return lista
    
    def busca_largura(self, vertice_inicial):
        self.queue.append(vertice_inicial)

        while len(self.queue) > 0:
            
            for i in self.listar_vizinhos(self.queue[0]):
                if i in self.queue or i in self.visitados:
                    continue
                self.queue.append(i)

            self.visitados.append(self.queue.pop(0))

        return self.visitados
    
    def menor_caminho(self, vertice_inicial, vertice_final):
        self.queue.append(vertice_inicial)
        encontrou = False
        while len(self.queue) > 0:
            if encontrou == True:
                break
            
            for i in self.listar_vizinhos(self.queue[0]):
                if i == vertice_final:
                    self.visitados.append(self.queue.pop(0))
                    self.visitados.append(i)
                    encontrou = True
                    break
                if i in self.queue or i in self.visitados:
                    continue
                self.queue.append(i)

            self.visitados.append(self.queue.pop(0))

        return self.visitados
    
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

    def busca_profundidade_cycle_detector(self, vertice_inicial):
        lista_visitados = []
        pilha = []
        pilha.append(vertice_inicial)
        estrutura = {
            vertice_inicial: None
        }
        ciclo = False
        while len(pilha) > 0 and ciclo == False:
            atual = pilha.pop()
        
            lista_visitados.append(atual)
                    
            for i in self.listar_vizinhos(atual):
                if(i in lista_visitados or i in pilha):
                    continue    
                if estrutura[atual] == i:
                    ciclo = False
                else:
                    ciclo =  True
                    break

                estrutura[i] = atual
                pilha.append(i)

        return lista_visitados, ciclo


# Codigo do professor
# Vértices: A, B, C, D, E, F

matriz = MatrizAdjacencia(2)

matriz_adjacencia = [
#   A  B  C  D  E  F
    [0, 1, 1, 0, 1, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [1, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0]   # F
]
matriz.matriz = matriz_adjacencia
print(matriz.busca_profundidade(1))
print(matriz.busca_profundidade_cycle_detector(0))
