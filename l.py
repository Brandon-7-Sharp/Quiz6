from abc import ABC, abstractmethod

class Width(ABC):
    def __init__(self) -> None:
        self.width = 0
    @abstractmethod
    def set_width(self, width):
        self.width = width

class Height(ABC):
    def __init__(self) -> None:
        self.height = 0
    @abstractmethod
    def set_height(self, height):
        self.height = height

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        if (isinstance(self, Height) and isinstance(self, Width)):
            print(f"    Calculating Area WITH Height And Width For A {type(self)}")
        else:
            print(f"    Calculating Area WITHOUT Height And Width For A {type(self)}")

class Triangle(Shape):
    def get_area(self):
        print("Triangle:")
        super().get_area()

class Circle(Shape, Height, Width):
    def get_area(self):
        print("Circle:")
        super().get_area()
    
    def set_height(self, height):
        return super().set_height(height)
    
    def set_width(self, width):
        return super().set_width(width)

class Rectangle(Shape, Height, Width):
    def get_area(self):
        print("Rectangle:")
        super().get_area()
    
    def set_height(self, height):
        return super().set_height(height)
    
    def set_width(self, width):
        return super().set_width(width)


def main():

    triangle = Triangle()
    triangle.get_area()

    circle = Circle()
    circle.get_area()
    circle.set_height(7)
    circle.set_width(5)
    print(f"Circle Height: {circle.height}")
    print(f"Circle Width: {circle.width}")

    rectangle = Rectangle()
    rectangle.get_area()
    rectangle.set_height(7)
    rectangle.set_width(5)
    print(f"Rectangle Height: {rectangle.height}")
    print(f"Rectangle Width: {rectangle.width}")

if __name__=='__main__': 	
    main()