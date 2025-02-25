class Shape:
  def __init__(self):
    self.area_value = 0  # Default area for Shape

  def area(self):
    print(f"Area of Shape: {self.area_value}")

class Square(Shape):
  def __init__(self, length):
    super().__init__()  # Initialize the parent class
    self.length = length

  def area(self):
    self.area_value = self.length ** 2  # Calculate square area
    print(f"Area of Square with side {self.length}: {self.area_value}")

shape = Shape()
shape.area()

square = Square(5)
square.area()
