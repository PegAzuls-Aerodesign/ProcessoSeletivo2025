import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.length = self._calculate_length()
    
    def _calculate_length(self):
        dx = self.b.x - self.a.x
        dy = self.b.y - self.a.y
        return math.hypot(dx, dy)
    
    def angle_between(self, other):
        # Vetores diretores das linhas
        vec1 = (self.b.x - self.a.x, self.b.y - self.a.y)
        vec2 = (other.b.x - other.a.x, other.b.y - other.a.y)
        
        # Produto escalar
        dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
        # Módulos dos vetores
        mag1 = math.hypot(vec1[0], vec1[1])
        mag2 = math.hypot(vec2[0], vec2[1])
        
        if mag1 == 0 or mag2 == 0:
            return 0.0
        
        # Evita erros de precisão com clamping
        cos_theta = dot_product / (mag1 * mag2)
        cos_theta = max(min(cos_theta, 1.0), -1.0)
        radians = math.acos(cos_theta)
        return math.degrees(radians)

class Truss:
    def __init__(self, name, points, lines):
        self.name = name
        self.points = points
        self.lines = lines

# Pontos da figura
P = Point(0, 0)
E = Point(2, 4)
G = Point(4, 2)
A = Point(6, 4)
Z = Point(8, 0)

# Linhas da treliça
PE = Line(P, E)
EG = Line(E, G)
GA = Line(G, A)
AZ = Line(A, Z)
PG = Line(P, G)
GZ = Line(G, Z)

# Treliça
truss = Truss("Treliça Exemplo", [P, E, G, A, Z], [PE, EG, GA, AZ, PG, GZ])

# Calcular ângulo entre duas linhas
angle = PE.angle_between(EG)
print(f"Ângulo entre PE e EG: {angle:.2f}°")