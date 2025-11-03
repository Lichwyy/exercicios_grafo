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

def GrauPorVertice(grafo):
    for x in grafo:
        temp = len(grafo[x])
        grafo[x] = temp

    return grafo

def VerificarSeExisteUmaArestaDeUmVerticeProOutro(grafo, aresta):
    try:
        grafo[aresta[0]].remove(aresta[1])
        return True
    except:
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



