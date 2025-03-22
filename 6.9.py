import math


def parse_input(file_path):
    figures = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if parts:
                name = parts[0]
                parameters = list(map(float, parts[1:]))
                figures.append((name, parameters))
    return figures


class Shape:
    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        h = math.sqrt(self.c ** 2 - ((self.b - self.a) / 2) ** 2)
        return ((self.a + self.b) / 2) * h


class Parallelogram(Shape):
    def __init__(self, base, side, height):
        self.base, self.side, self.height = base, side, height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def area(self):
        return self.base * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


def create_shape(name, params):
    if name == "Triangle":
        return Triangle(*params)
    elif name == "Rectangle":
        return Rectangle(*params)
    elif name == "Trapeze":
        return Trapeze(*params)
    elif name == "Parallelogram":
        return Parallelogram(*params)
    elif name == "Circle":
        return Circle(*params)
    return None


def find_largest_shapes(file_paths):
    max_area_shape = None
    max_perimeter_shape = None
    max_area = max_perimeter = float('-inf')

    for file_path in file_paths:
        figures = parse_input(file_path)
        for name, params in figures:
            shape = create_shape(name, params)
            if shape:
                area = shape.area()
                perimeter = shape.perimeter()
                if area > max_area:
                    max_area = area
                    max_area_shape = (name, params, area)
                if perimeter > max_perimeter:
                    max_perimeter = perimeter
                    max_perimeter_shape = (name, params, perimeter)

    return max_area_shape, max_perimeter_shape


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    max_area_shape, max_perimeter_shape = find_largest_shapes(input_files)

    with open("output.txt", "w") as file:
        file.write(f"Largest Area: {max_area_shape[0]} {max_area_shape[1]} - Area: {max_area_shape[2]:.2f}\n")
        file.write(
            f"Largest Perimeter: {max_perimeter_shape[0]} {max_perimeter_shape[1]} - Perimeter: {max_perimeter_shape[2]:.2f}\n")
    print("Result saved to output.txt")


if __name__ == "__main__":
    main()
