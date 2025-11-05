import pandas as pd

class ListaVertices:
    def __init__(self, lista_arestas):
        self.df = pd.DataFrame(columns=['vertice'])
        vertices = sorted(set(item for sublist in lista_arestas for item in sublist))
        for vertice in vertices:
            self.df.loc[len(self.df)] = vertice

    def mostrar_lista(self):
        print("Lista de Vértices:")
        print(self.df)

    def inserir_vertice(self, vertice):
        if vertice not in self.df['vertice'].values:
            self.df.loc[len(self.df.index)] = vertice
        else:
            print(f"Vértice '{vertice}' já existe.")
