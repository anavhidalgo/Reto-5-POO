from paquete.shape import Point
from paquete2.rectangle import Rectangle, Square

p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(4, 3)
p4 = Point(0, 3)

rect = Rectangle([p1, p2, p3, p4])
print("Área del rectángulo:", rect.compute_area())
print("Perímetro del rectángulo:", rect.compute_perimeter())

# --------------

p5 = Point(0, 0)
p6 = Point(2, 0)
p7 = Point(2, 2)
p8 = Point(0, 2)

square = Square([p5, p6, p7, p8])
print("Área del cuadrado:", square.compute_area())
print("Perímetro del cuadrado:", square.compute_perimeter())