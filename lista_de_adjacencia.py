grafo = {
    "V1" : ["V2", "V3", "V4"],
    "V2" : ["V3"],
    "V3" : ["V4"],
    "V4" : []
}

def AddVertice(grafo, vertice):
    grafo[vertice] = []
    return grafo

def RemoveVertice(grafo, vertice):
    grafo.pop(vertice)
    for x in grafo:
        try:
            grafo[x].remove(vertice)
        except:
            continue
    return grafo

def AddEdge(grafo, aresta):
    grafo[aresta[0]].append(aresta[1])
    return grafo

def RemoveEdge(grafo, aresta):
    try:
        grafo[aresta[0]].remove(aresta[1])
    except:
        return "Não existe essa aresta no grafo"
    return grafo

def GrauPorVertice(grafo, dirigido=True):
    if dirigido:
        graus = {v: {"entrada": 0, "saida": len(grafo.get(v, []))} for v in grafo}
        for origem, destinos in grafo.items():
            for d in destinos:
                if d in graus:
                    graus[d]["entrada"] += 1
                else:
                    graus[d] = {"entrada": 1, "saida": len(grafo.get(d, []))}
        return graus
    else:
        graus = {}
        for v in grafo:
            graus[v] = len(grafo.get(v, []))
        for origem, destinos in grafo.items():
            for d in destinos:
                if d not in graus:
                    graus[d] = 1
                else:
                    pass
        return graus

def VerificarSeExisteUmaArestaDeUmVerticeProOutro(grafo, aresta, dirigido=True):
    origem, destino = aresta
    lista_origem = grafo.get(origem, [])
    if destino in lista_origem:
        return True
    if not dirigido:
        lista_destino = grafo.get(destino, [])
        if origem in lista_destino:
            return True
    return False

def ListarTodosOsVizinhosDoVertice(grafo,vertice):
    return grafo[vertice]

def VerificarPercurso(grafo,percurso):
    for x in range(len(percurso) - 1):
        if percurso[x + 1] in grafo[percurso[x]]:
            continue
        else:
            return False

    return True

def busca_em_profundidade(grafo, inicio):
    visitados = []  
    pilha = [inicio]   

    while pilha:
     
        vertice = pilha.pop()
        
        if vertice not in visitados:
            visitados.append(vertice)
            
            for vizinho in reversed(grafo[vertice]):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return visitados

grafo_teste = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
            
result = busca_em_profundidade(grafo_teste, "A")
print(result)
    
def verificar_ciclo(grafo, inicio):
    visitados = []
    pilha = [inicio]
    aux = {inicio: None}

    while pilha:
        vertice = pilha.pop()
        
        if vertice not in visitados:
            visitados.append(vertice)
            
            for vizinho in reversed(grafo[vertice]):

                
                if vizinho in visitados and aux[vertice] != vizinho:
                    return True

                
                if vizinho not in visitados and vizinho not in pilha:
                    aux[vizinho] = vertice
                    pilha.append(vizinho)
    return False

grafo1 = {
    1: [2],
    2: [1, 3],
    3: [2]
}

grafo2 = {
    1: [2],
    2: [1, 3],
    3: [2, 1]
}

print(verificar_ciclo(grafo1, 1))  # False
print(verificar_ciclo(grafo2, 1))  # True