from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        print(f"    Calculating Area For A {type(self)}")


class Square(Shape):
    def get_area(self):
        print("Square:")
        super().get_area()

class Circle(Shape):
    def get_area(self):
        print("Circle:")
        super().get_area()

class Rectangle(Shape):
    def get_area(self):
        print("Rectangle:")
        super().get_area()


def main():

    square = Square()
    square.get_area()

    circle = Circle()
    circle.get_area()

    rectangle = Rectangle()
    rectangle.get_area()

if __name__=='__main__': 	
    main()