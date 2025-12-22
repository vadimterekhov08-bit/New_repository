class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return f'Радиус: {self.radius}'

    def set_radius(self, new_radius):
        self.radius = new_radius
        return f'Новый радиус: {self.radius}'

circle = Circle(10)

print(circle.get_radius())
print(circle.set_radius(20))
print(circle.get_radius())