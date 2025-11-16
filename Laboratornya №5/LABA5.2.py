class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

circle1 = Circle(5)
print(f"Начальный радиус: {circle1.get_radius()}")
circle1.set_radius(10)
print(f"Новый радиус: {circle1.get_radius()}")