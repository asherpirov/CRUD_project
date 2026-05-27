from shape import Shape
import math

class Rectangle(Shape):
    def __init__(self, shape_id, shape_type, height, width):
        super().__init__(shape_id, shape_type)
        self.height = height
        self.width = width


    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def to_dict(self):
        return {"id": self.id, "type": self.shape_type, "width": self.width,"height": self.height}
