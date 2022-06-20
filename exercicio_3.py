import math

class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, outro_ponto):
        dist = (self.x - outro_ponto.x)**2 + (self.y - outro_ponto.y)**2
        dist = math.sqrt(dist)
        return dist


if __name__ == '__main__':
    
    p1 = Ponto(3.5, 6.7)
    p2 = Ponto(1.0, 2.2)

    print("\n")

    print(f'Ponto 1: ({p1.x}, {p1.y})')
    print(f'Ponto 2: ({p2.x}, {p2.y})')

    distancia_1 = p1.calcular_distancia(p2)

    print('\nDistância 1:', distancia_1)

    distancia_2 = p2.calcular_distancia(p1)

    print('\nDistância 2:', distancia_2)

    print("\n")