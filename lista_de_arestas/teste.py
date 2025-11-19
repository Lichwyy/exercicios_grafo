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

# === Testes de Busca em Profundidade (DFS) ===
print("\n" + "="*60)
print("===== TESTES DE BUSCA EM PROFUNDIDADE (DFS) =====")
print("="*60)

# TESTE 10: DFS em grafo conectado simples
print("\n===== TESTE 10: DFS em Grafo Conectado Simples =====")
grafo_simples = ListaArestas()
arestas_simples = [
    ("A", "B"), ("B", "A"),  # A-B (não direcionado)
    ("A", "C"), ("C", "A"),  # A-C
    ("B", "D"), ("D", "B"),  # B-D
    ("C", "D"), ("D", "C")   # C-D
]
for start, end in arestas_simples:
    grafo_simples.inserir_aresta(Aresta(start, end))

print("Grafo:")
grafo_simples.mostrar_lista_arestas()
print("\nDFS a partir de 'A':")
resultado = grafo_simples.busca_em_profundidade("A")
print(f"Ordem de visita: {resultado}")
print(f"Vértices visitados: {len(resultado)} de 4 esperados")
assert len(resultado) == 4, "Deveria visitar todos os 4 vértices"
assert resultado[0] == "A", "Primeiro vértice deve ser A"
print("✓ Teste passou!")

# TESTE 11: DFS em grafo linear (caminho)
print("\n===== TESTE 11: DFS em Grafo Linear (Caminho) =====")
grafo_linear = ListaArestas()
arestas_linear = [
    ("1", "2"), ("2", "1"),
    ("2", "3"), ("3", "2"),
    ("3", "4"), ("4", "3"),
    ("4", "5"), ("5", "4")
]
for start, end in arestas_linear:
    grafo_linear.inserir_aresta(Aresta(start, end))

print("Grafo (caminho linear 1-2-3-4-5):")
grafo_linear.mostrar_lista_arestas()
print("\nDFS a partir de '1':")
resultado = grafo_linear.busca_em_profundidade("1")
print(f"Ordem de visita: {resultado}")
print(f"Vértices visitados: {len(resultado)}")
assert len(resultado) == 5, "Deveria visitar todos os 5 vértices"
assert resultado[0] == "1", "Primeiro vértice deve ser 1"
assert "5" in resultado, "Deve alcançar o vértice final 5"
print("✓ Teste passou!")

# TESTE 12: DFS em grafo com ciclo
print("\n===== TESTE 12: DFS em Grafo com Ciclo =====")
grafo_ciclo = ListaArestas()
arestas_ciclo = [
    ("X", "Y"), ("Y", "X"),
    ("Y", "Z"), ("Z", "Y"),
    ("Z", "W"), ("W", "Z"),
    ("W", "X"), ("X", "W")  # Fecha o ciclo
]
for start, end in arestas_ciclo:
    grafo_ciclo.inserir_aresta(Aresta(start, end))

print("Grafo (ciclo X-Y-Z-W-X):")
grafo_ciclo.mostrar_lista_arestas()
print("\nDFS a partir de 'X':")
resultado = grafo_ciclo.busca_em_profundidade("X")
print(f"Ordem de visita: {resultado}")
print(f"Vértices visitados: {len(resultado)}")
assert len(resultado) == 4, "Deveria visitar todos os 4 vértices"
assert len(resultado) == len(set(resultado)), "Não deve visitar vértice duplicado"
print("✓ Teste passou! (Nenhum vértice visitado duas vezes)")

# TESTE 13: DFS em grafo desconexo
print("\n===== TESTE 13: DFS em Grafo Desconexo =====")
grafo_desconexo = ListaArestas()
arestas_desconexo = [
    # Componente 1: P-Q
    ("P", "Q"), ("Q", "P"),
    # Componente 2: R-S-T (isolado do primeiro)
    ("R", "S"), ("S", "R"),
    ("S", "T"), ("T", "S")
]
for start, end in arestas_desconexo:
    grafo_desconexo.inserir_aresta(Aresta(start, end))

print("Grafo (2 componentes desconexas: P-Q e R-S-T):")
grafo_desconexo.mostrar_lista_arestas()
print("\nDFS a partir de 'P' (componente 1):")
resultado = grafo_desconexo.busca_em_profundidade("P")
print(f"Ordem de visita: {resultado}")
print(f"Vértices visitados: {len(resultado)} (deveria ser 2, apenas da componente conectada)")
assert len(resultado) == 2, "Deveria visitar apenas vértices da componente conectada"
assert "P" in resultado and "Q" in resultado, "Deve conter P e Q"
assert "R" not in resultado and "S" not in resultado, "Não deve alcançar componente desconectada"
print("✓ Teste passou!")

print("\nDFS a partir de 'R' (componente 2):")
resultado = grafo_desconexo.busca_em_profundidade("R")
print(f"Ordem de visita: {resultado}")
print(f"Vértices visitados: {len(resultado)} (deveria ser 3)")
assert len(resultado) == 3, "Deveria visitar os 3 vértices da componente"
assert "R" in resultado and "S" in resultado and "T" in resultado, "Deve conter R, S e T"
print("✓ Teste passou!")

# TESTE 14: DFS em grafo estrela (um centro conectado a vários vértices)
print("\n===== TESTE 14: DFS em Grafo Estrela =====")
grafo_estrela = ListaArestas()
centro = "CENTRO"
pontas = ["P1", "P2", "P3", "P4"]
arestas_estrela = []
for ponta in pontas:
    arestas_estrela.extend([(centro, ponta), (ponta, centro)])

for start, end in arestas_estrela:
    grafo_estrela.inserir_aresta(Aresta(start, end))

print(f"Grafo estrela (centro conectado a {len(pontas)} pontas):")
grafo_estrela.mostrar_lista_arestas()
print(f"\nDFS a partir de '{centro}':")
resultado = grafo_estrela.busca_em_profundidade(centro)
print(f"Ordem de visita: {resultado}")
print(f"Vértices visitados: {len(resultado)}")
assert len(resultado) == 5, "Deveria visitar centro + 4 pontas"
assert resultado[0] == centro, "Primeiro deve ser o centro"
print("✓ Teste passou!")

# TESTE 15: DFS em vértice isolado (sem arestas)
print("\n===== TESTE 15: DFS em Vértice Isolado =====")
grafo_isolado = ListaArestas()
# Grafo vazio, mas vamos testar busca de um vértice que não existe
print("Grafo vazio")
resultado = grafo_isolado.busca_em_profundidade("ISOLADO")
print(f"DFS a partir de vértice inexistente 'ISOLADO': {resultado}")
print(f"Resultado: {resultado}")
assert resultado == ["ISOLADO"], "Deveria retornar apenas o vértice inicial"
print("✓ Teste passou!")

# TESTE 16: Comparação DFS no grafo original do teste
print("\n===== TESTE 16: DFS no Grafo Original dos Testes =====")
lista_arestas.mostrar_lista_arestas()
print("\nDFS a partir de 'A':")
resultado = lista_arestas.busca_em_profundidade("A")
print(f"Ordem de visita: {resultado}")
print(f"Total de vértices alcançados: {len(resultado)}")

print("\nDFS a partir de 'E':")
resultado_e = lista_arestas.busca_em_profundidade("E")
print(f"Ordem de visita: {resultado_e}")
print(f"Total de vértices alcançados: {len(resultado_e)}")

print("\n" + "="*60)
print("TODOS OS TESTES DE DFS CONCLUÍDOS COM SUCESSO! ✓")
print("="*60)

# === Testes de Detecção de Ciclos ===
print("\n" + "="*60)
print("===== TESTES DE DETECÇÃO DE CICLOS =====")
print("="*60)

# TESTE 17: Grafo SEM ciclo - Árvore simples
print("\n===== TESTE 17: Grafo SEM Ciclo (Árvore) =====")
grafo_arvore = ListaArestas()
arestas_arvore = [
    ("A", "B"), ("B", "A"),
    ("A", "C"), ("C", "A"),
    ("B", "D"), ("D", "B"),
    ("B", "E"), ("E", "B")
]
for start, end in arestas_arvore:
    grafo_arvore.inserir_aresta(Aresta(start, end))

print("Grafo (árvore - sem ciclo):")
print("    A")
print("   / \\")
print("  B   C")
print(" / \\")
print("D   E")
grafo_arvore.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de 'A':")
resultado = grafo_arvore.busca_em_profundidade_detectar_ciclos("A")
print(f"Ordem de visita: {resultado}")
print("Expectativa: NÃO deve detectar ciclo (é uma árvore)")
print("-" * 60)

# TESTE 18: Grafo COM ciclo simples (triângulo)
print("\n===== TESTE 18: Grafo COM Ciclo (Triângulo) =====")
grafo_triangulo = ListaArestas()
arestas_triangulo = [
    ("1", "2"), ("2", "1"),
    ("2", "3"), ("3", "2"),
    ("3", "1"), ("1", "3")  # Fecha o triângulo - cria ciclo
]
for start, end in arestas_triangulo:
    grafo_triangulo.inserir_aresta(Aresta(start, end))

print("Grafo (triângulo 1-2-3):")
print("  1 --- 2")
print("   \\   /")
print("    \\ /")
print("     3")
grafo_triangulo.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de '1':")
resultado = grafo_triangulo.busca_em_profundidade_detectar_ciclos("1")
print(f"Ordem de visita: {resultado}")
print("Expectativa: DEVE detectar ciclo (triângulo)")
print("-" * 60)

# TESTE 19: Grafo COM ciclo (quadrado)
print("\n===== TESTE 19: Grafo COM Ciclo (Quadrado) =====")
grafo_quadrado = ListaArestas()
arestas_quadrado = [
    ("A", "B"), ("B", "A"),
    ("B", "C"), ("C", "B"),
    ("C", "D"), ("D", "C"),
    ("D", "A"), ("A", "D")  # Fecha o quadrado
]
for start, end in arestas_quadrado:
    grafo_quadrado.inserir_aresta(Aresta(start, end))

print("Grafo (quadrado A-B-C-D):")
print("  A --- B")
print("  |     |")
print("  D --- C")
grafo_quadrado.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de 'A':")
resultado = grafo_quadrado.busca_em_profundidade_detectar_ciclos("A")
print(f"Ordem de visita: {resultado}")
print("Expectativa: DEVE detectar ciclo")
print("-" * 60)

# TESTE 20: Grafo SEM ciclo - Caminho linear
print("\n===== TESTE 20: Grafo SEM Ciclo (Caminho Linear) =====")
grafo_caminho = ListaArestas()
arestas_caminho = [
    ("V1", "V2"), ("V2", "V1"),
    ("V2", "V3"), ("V3", "V2"),
    ("V3", "V4"), ("V4", "V3")
]
for start, end in arestas_caminho:
    grafo_caminho.inserir_aresta(Aresta(start, end))

print("Grafo (caminho V1-V2-V3-V4):")
print("V1 --- V2 --- V3 --- V4")
grafo_caminho.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de 'V1':")
resultado = grafo_caminho.busca_em_profundidade_detectar_ciclos("V1")
print(f"Ordem de visita: {resultado}")
print("Expectativa: NÃO deve detectar ciclo (caminho linear)")
print("-" * 60)

# TESTE 21: Grafo COM múltiplos ciclos
print("\n===== TESTE 21: Grafo COM Múltiplos Ciclos =====")
grafo_multiplos = ListaArestas()
arestas_multiplos = [
    # Ciclo 1: A-B-C-A
    ("A", "B"), ("B", "A"),
    ("B", "C"), ("C", "B"),
    ("C", "A"), ("A", "C"),
    # Ciclo 2: C-D-E-C
    ("C", "D"), ("D", "C"),
    ("D", "E"), ("E", "D"),
    ("E", "C"), ("C", "E")
]
for start, end in arestas_multiplos:
    grafo_multiplos.inserir_aresta(Aresta(start, end))

print("Grafo (dois triângulos compartilhando vértice C):")
print("  A --- B       D")
print("   \\   /       / \\")
print("    \\ /       /   \\")
print("     C ------ E")
grafo_multiplos.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de 'A':")
resultado = grafo_multiplos.busca_em_profundidade_detectar_ciclos("A")
print(f"Ordem de visita: {resultado}")
print("Expectativa: DEVE detectar ciclo(s)")
print("-" * 60)

# TESTE 22: Grafo com ciclo + ramo sem ciclo
print("\n===== TESTE 22: Grafo Misto (Ciclo + Árvore) =====")
grafo_misto = ListaArestas()
arestas_misto = [
    # Ciclo: 1-2-3-1
    ("1", "2"), ("2", "1"),
    ("2", "3"), ("3", "2"),
    ("3", "1"), ("1", "3"),
    # Ramo sem ciclo: 1-4-5
    ("1", "4"), ("4", "1"),
    ("4", "5"), ("5", "4")
]
for start, end in arestas_misto:
    grafo_misto.inserir_aresta(Aresta(start, end))

print("Grafo (triângulo 1-2-3 + ramo 4-5):")
print("  1 --- 2       5")
print("  |\\   /        |")
print("  | \\ /         |")
print("  |  3          4")
print("  |")
print("  4 --- 5")
grafo_misto.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de '1':")
resultado = grafo_misto.busca_em_profundidade_detectar_ciclos("1")
print(f"Ordem de visita: {resultado}")
print("Expectativa: DEVE detectar ciclo (no triângulo)")
print("-" * 60)

# TESTE 23: Grafo grande SEM ciclo (árvore binária)
print("\n===== TESTE 23: Grafo SEM Ciclo (Árvore Binária) =====")
grafo_binaria = ListaArestas()
arestas_binaria = [
    ("R", "L"), ("L", "R"),
    ("R", "R2"), ("R2", "R"),
    ("L", "L1"), ("L1", "L"),
    ("L", "L2"), ("L2", "L"),
    ("R2", "R3"), ("R3", "R2"),
    ("R2", "R4"), ("R4", "R2")
]
for start, end in arestas_binaria:
    grafo_binaria.inserir_aresta(Aresta(start, end))

print("Grafo (árvore binária):")
print("       R")
print("      / \\")
print("     L   R2")
print("    / \\  / \\")
print("   L1 L2 R3 R4")
grafo_binaria.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de 'R':")
resultado = grafo_binaria.busca_em_profundidade_detectar_ciclos("R")
print(f"Ordem de visita: {resultado}")
print("Expectativa: NÃO deve detectar ciclo (árvore)")
print("-" * 60)

# TESTE 24: Grafo com auto-loop (caso extremo)
print("\n===== TESTE 24: Grafo COM Auto-Loop =====")
grafo_autoloop = ListaArestas()
arestas_autoloop = [
    ("X", "Y"), ("Y", "X"),
    ("Y", "Y")  # Auto-loop
]
for start, end in arestas_autoloop:
    grafo_autoloop.inserir_aresta(Aresta(start, end))

print("Grafo (X-Y com auto-loop em Y):")
print("  X --- Y ⟲")
grafo_autoloop.mostrar_lista_arestas()
print("\nBusca com detecção de ciclo a partir de 'X':")
resultado = grafo_autoloop.busca_em_profundidade_detectar_ciclos("X")
print(f"Ordem de visita: {resultado}")
print("Expectativa: DEVE detectar ciclo (auto-loop)")
print("-" * 60)

print("\n" + "="*60)
print("TESTES DE DETECÇÃO DE CICLOS CONCLUÍDOS!")
print("="*60)
print("\nRESUMO:")
print("- Grafos SEM ciclo: Testes 17, 20, 23")
print("- Grafos COM ciclo: Testes 18, 19, 21, 22, 24")
print("\nAnalise os resultados acima para validar se o método")
print("está detectando ciclos corretamente!")
print("="*60)
