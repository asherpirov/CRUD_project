from shape import Shape
import math


class Square(Shape):
    """Represents a square shape, inheriting from Shape."""
    def __init__(self, shape_id, shape_type, side):
        """Initialize a Square with an ID and side."""
        super().__init__(shape_id, shape_type)
        self.side = side


    def get_area(self):
        """Calculate and return the area of the square."""
        return self.side ** 2

    def get_perimeter(self):
        """Calculate and return the perimeter of the square."""
        return 4 * self.side

    def to_dict(self):
        """Return a dictionary representation of the square."""
        return {"id": self.id, "type": self.shape_type, "side": self.side}
