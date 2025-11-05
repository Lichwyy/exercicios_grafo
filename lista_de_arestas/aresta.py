class Aresta:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_aresta(self):
        return (self.start, self.end)

    def __repr__(self):
        return f"Aresta({self.start}, {self.end})"
