from shape import Shape
import math
import logging

logger = logging.getLogger(__name__)

class Rectangle(Shape):
    """Represents a rectangle shape, inheriting from Shape."""
    def __init__(self, shape_id: int, height: float, width: float) -> None:
        """Initialize a Rectangle with an ID, height, and width."""
        super().__init__(shape_id, "rectangle")
        self.height = height
        self.width = width
        logger.info("Created Rectangle object with ID: %s", shape_id)


    def get_area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def to_dict(self) -> dict:
        """Return a dictionary representation of the rectangle."""
        return {"id": self.id,
                "type": self.shape_type,
                "width": self.width,
                "height": self.height
                }

