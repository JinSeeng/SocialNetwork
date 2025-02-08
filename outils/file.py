class File:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def enfiler(self, x):
        self.elements.append(x)

    def defiler(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        return self.elements.pop(0)