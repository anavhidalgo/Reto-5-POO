class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self): return self._x
    def get_y(self): return self._y
    def set_x(self, x): self._x = x
    def set_y(self, y): self._y = y

    def compute_distance(self, other) -> float:
        dx = self._x - other.get_x()
        dy = self._y - other.get_y()
        return (dx * dx + dy * dy) ** 0.5


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def compute_length(self) -> float:
        return self._start_point.compute_distance(self._end_point)

    def get_length(self): return self._length


class Shape:
    def __init__(self, vertices: list):
        self._vertices = vertices
        self._edges = self.compute_edges()
        self._inner_angles = []
        self._is_regular = False

    def get_vertices(self): return self._vertices
    def get_edges(self): return self._edges
    def get_inner_angles(self): return self._inner_angles
    def is_regular(self): return self._is_regular

    def set_vertices(self, vertices): self._vertices = vertices
    def set_inner_angles(self, angles): self._inner_angles = angles
    def set_regular(self, value): self._is_regular = value

    def compute_edges(self):
        edges = []
        for i in range(len(self._vertices)):
            p1 = self._vertices[i]
            p2 = self._vertices[(i + 1) % len(self._vertices)]
            edges.append(Line(p1, p2))
        return edges

    def compute_area(self):
        raise NotImplementedError("This method must be overridden")

    def compute_perimeter(self):
        total = 0
        for edge in self._edges:
            total += edge.get_length()
        return total

    def compute_inner_angles(self):
        raise NotImplementedError("This method must be overridden")