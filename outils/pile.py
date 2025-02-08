class Pile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, x):
        self.elements.append(x)

    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.elements.pop()