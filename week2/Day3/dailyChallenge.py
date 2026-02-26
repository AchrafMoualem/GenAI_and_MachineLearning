class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.diameter = diameter
        else:
            raise ValueError("Vous devez spécifier soit le rayon, soit le diamètre")
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = value * 2
    
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Cercle: Rayon={self.radius}, Diamètre={self.diameter}"

# Test
c1 = Circle(radius=5)
print(c1)  # Cercle: Rayon=5, Diamètre=10
print(f"Aire: {c1.area():.2f}")

c2 = Circle(diameter=10)
print(c2)  # Cercle: Rayon=5, Diamètre=10