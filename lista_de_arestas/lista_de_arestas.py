import pandas as pd
from lista_de_vertices import ListaVertices
from aresta import Aresta

class ListaArestas:
    def __init__(self):
        self.df = pd.DataFrame(columns=['start', 'end'])
    
    def mostrar_lista_vertices(self):
        print("\n--- Lista de Vértices ---")
        ListaVertices(self.df.values).mostrar_lista()

    def mostrar_lista_arestas(self):
        print("\n--- Lista de Arestas ---")
        print(self.df)

    def inserir_aresta(self, aresta: Aresta):
        self.df.loc[len(self.df.index)] = aresta.get_aresta()

    def remover_aresta(self, aresta: Aresta):
        aresta_valor = aresta.get_aresta()
        filtro = (self.df['start'] == aresta_valor[0]) & (self.df['end'] == aresta_valor[1])
        if not self.df[filtro].empty:
            index_to_drop = self.df[filtro].index[0]
            self.df = self.df.drop(index_to_drop, axis=0).reset_index(drop=True)
            print(f"Aresta {aresta_valor} removida com sucesso.")
        else:
            print(f"Aresta {aresta_valor} não encontrada.")

    def calcular_grau_cada_vertice(self):
        vertices = ListaVertices(self.df.values)
        grau_vertices = pd.DataFrame(columns=['Vertice', 'Entrada', 'Saída'])
        for vertice in vertices.df.values:
            saida = self.df['start'].isin(vertice).sum()
            entrada = self.df['end'].isin(vertice).sum()
            grau_vertices.loc[len(grau_vertices)] = (vertice[0], entrada, saida)
        grau_vertices = grau_vertices.set_index('Vertice')
        print(grau_vertices)

    def verificar_vizinhos_vertice(self, vertice: str):
        vizinhos = []
        for _, row in self.df.iterrows():
            if row['start'] == vertice:
                vizinhos.append(row['end'])
        print(vizinhos)

    def verificar_existencia_aresta(self, vertice_start, vertice_end):
        for _, row in self.df.iterrows():
            if row['start'] == vertice_start and row['end'] == vertice_end:
                return True
        return False
    
    def validar_percurso(self, percurso: list[str]):
        if len(percurso) < 2:
            return True

        for i in range(len(percurso) - 1):
            vertice_start = percurso[i]
            vertice_end = percurso[i+1]

            if not self.verificar_existencia_aresta(vertice_start, vertice_end):
                return False
        return True
