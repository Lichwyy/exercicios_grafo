from aresta import Aresta
from lista_de_arestas import ListaArestas

# === Criação de Arestas ===
print("\n===== TESTE 1: Inserção de Arestas =====")
edge_list = [("A", "B"), ("B", "A"), ("C", "D"), ("D", "C"), ("E", "T"), ("C", "B"), ("G", "F"), ("E", "C"), ("O", "A")]
arestas = [Aresta(start, end) for start, end in edge_list]

lista_arestas = ListaArestas()

for a in arestas:
    lista_arestas.inserir_aresta(a)

lista_arestas.mostrar_lista_arestas()
lista_arestas.mostrar_lista_vertices()

# === Remoção de uma Aresta ===
print("\n===== TESTE 2: Remoção de uma Aresta Existente =====")
aresta_teste = Aresta('C', 'D')
lista_arestas.remover_aresta(aresta_teste)
lista_arestas.mostrar_lista_arestas()
lista_arestas.mostrar_lista_vertices()

# === Tentando remover uma Aresta inexistente ===
print("\n===== TESTE 3: Remoção de Aresta Inexistente =====")
aresta_inexistente = Aresta('X', 'Y')
lista_arestas.remover_aresta(aresta_inexistente)

# === Inserção de nova Aresta ===
print("\n===== TESTE 4: Inserção de nova Aresta =====")
nova_aresta = Aresta('E', 'F')
lista_arestas.inserir_aresta(nova_aresta)
lista_arestas.mostrar_lista_arestas()
lista_arestas.mostrar_lista_vertices()

# === Teste de Duplicidade de Vértices ===
print("\n===== TESTE 5: Inserção de vértice duplicado manualmente =====")
from lista_de_vertices import ListaVertices
lv = ListaVertices(lista_arestas.df.values)
lv.mostrar_lista()
lv.inserir_vertice('A')  # Deve avisar que já existe
lv.inserir_vertice('Z')  # Novo vértice
lv.mostrar_lista()

# === Teste de Grau de Vértices ===
print("\n===== TESTE 6: Calcular o grau de cada vertice =====")
lista_arestas.mostrar_lista_arestas()
print()
lista_arestas.calcular_grau_cada_vertice()

# === Teste de Calcular os Vizinhos de um Vértices ===
print("\n===== TESTE 7: Verificar o vizinho de um vertice =====")
lista_arestas.mostrar_lista_arestas()
print()
lista_arestas.verificar_vizinhos_vertice('E')

# === Teste de Verificar Existencia de Arestas ===
print("\n===== TESTE 8: Verificar Existencia de Arestas =====")
lista_arestas.mostrar_lista_arestas()
print()
condicao = lista_arestas.verificar_existencia_aresta('E', 'C')
print("Existe essa aresta!") if condicao else print("Não existe essa aresta!")

# === Teste de Validar um Percurso ===
print("\n===== TESTE 9: Verificar se um percurso é valido =====")
lista_arestas.mostrar_lista_arestas()
print()
condicao = lista_arestas.validar_percurso(['A', 'B', 'A'])
print("Existe esse percurso!") if condicao else print("Não existe esse percurso!")
