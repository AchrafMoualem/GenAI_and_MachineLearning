import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Spécifiez soit le rayon, soit le diamètre")
    
    # Propriétés pour avoir toujours accès au diamètre
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        # Calculale area 
        return math.pi * self.radius ** 2
    
    def __str__(self):
        # Display the circle with its radius, diameter and area
        return f"Cercle(rayon={self.radius:.2f}, diamètre={self.diameter:.2f}, aire={self.area:.2f})"
    
    def __add__(self, other):
        # Addition of two circles by adding their radii
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        
    
    def __gt__(self, other):
        # Compare if this circle is larger than another (by radius)
        if isinstance(other, Circle):
            return self.radius > other.radius
        
    
    def __lt__(self, other):
        # Compare if this circle is smaller than another (by radius)
        if isinstance(other, Circle):
            return self.radius < other.radius
   
    
    def __eq__(self, other):
        # Verify if two circles are equal (by radius)
        if isinstance(other, Circle):
            return math.isclose(self.radius, other.radius)
        return False

# TESTS 

print("Création des cercles:")
c1 = Circle(radius=5)
c2 = Circle(diameter=10)  #
c3 = Circle(radius=3)
c4 = Circle(diameter=20)  

print(f"c1: {c1}") 
print(f"c2: {c2}")
print(f"c3: {c3}")
print(f"c4: {c4}")

# Test de l'addition
print("\nAddition de cercles:")
c5 = c1 + c3
print(f"c1 + c3 = {c5}")

# Test de comparaison
print("\nComparaisons:")
print(f"c1 > c3 ? {c1 > c3}")  # True
print(f"c1 == c2 ? {c1 == c2}")  # True (même rayon)
print(f"c1 == c3 ? {c1 == c3}")  # False

# Test de tri
print("\n4 Tri d'une liste de cercles:")
circles = [c1, c3, c4, c2]
print("Liste originale:")
for c in circles:
    print(f"  {c}")

circles.sort()  # Utilise __lt__
print("\nListe triée (du plus petit au plus grand):")
for c in circles:
    print(f"  {c}")

# Tri inversé
circles.sort(reverse=True)
print("\nListe triée (du plus grand au plus petit):")
for c in circles:
    print(f"  {c}")