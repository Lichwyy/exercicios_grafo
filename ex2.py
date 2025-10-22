

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
            print(f"Grau do vértice {vertice}: {grau}")
    
    def verificar_aresta_existe(self, vertice_inicio, vertice_fim):
        if self.matriz[vertice_inicio][vertice_fim] == 1:
            return True
        return False
    
    def listar_vizinhos(self, vertice):
        lista = []
        vertice_vizinho = 0
        for j in self.matriz[vertice]:
            vertice_vizinho +=1
            if j == 1:
                lista.append(vertice_vizinho)
        return lista

    def verificar_se_percurso_existe(self, percurso:list):
        

if __name__ == "__main__":
    matriza = MatrizAdjacencia(3)
    print(matriza.matriz)
    matriza.inserir_vertice()
    print(matriza.matriz)
    matriza.remover_vertice(2)
    matriza.inserir_aresta(0, 1)
    print(matriza.matriz)
    matriza.inserir_aresta(1, 0)
    print(matriza.matriz)
    matriza.calcular_grau_cada_vertice()
    print(matriza.listar_vizinhos(1))

matriz = [[],[],[],[],[],[],[]]

