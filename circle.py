from shape import Shape
import math

class Circle(Shape):
    """Represents a circle shape, inheriting from Shape."""
    def __init__(self, shape_id, shape_type, radius):
        """Initialize a circle with an ID and radius."""
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.radius

    def to_dict(self):
        """Return a dictionary representation of the circle."""
        return {"id": self.id,
                "type": self.shape_type,
                "radius": self.radius
                }



