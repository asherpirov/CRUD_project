from shape import Shape
import math

class Rectangle(Shape):
    """Represents a rectangle shape, inheriting from Shape."""
    def __init__(self, shape_id, shape_type, height, width):
        """Initialize a Rectangle with an ID, height, and width."""
        super().__init__(shape_id, shape_type)
        self.height = height
        self.width = width


    def get_area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def to_dict(self):
        """Return a dictionary representation of the rectangle."""
        return {"id": self.id,
                "type": self.shape_type,
                "width": self.width,
                "height": self.height
                }
