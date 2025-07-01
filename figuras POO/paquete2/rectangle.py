from  paquete.shape import Shape, Line, Point

class Rectangle(Shape):
    def __init__(self, vertices: list):
        super().__init__(vertices)
        self.set_regular(False)

    def compute_area(self):
        width = self._edges[0].get_length()
        height = self._edges[1].get_length()
        return width * height


class Square(Rectangle):
    def __init__(self, vertices: list):
        super().__init__(vertices)
        self.set_regular(True)

    def compute_area(self):
        side = self._edges[0].get_length()
        return side * side


