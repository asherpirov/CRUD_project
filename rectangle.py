from shape import Shape
import math
import logging

logger = logging.getLogger(__name__)

class Rectangle(Shape):
    """Represents a rectangle shape, inheriting from Shape."""
    def __init__(self, shape_id: int, height: float, width: float) -> None:
        """Initialize a Rectangle with an ID, height, and width."""
        super().__init__(shape_id, "rectangle")
        if not isinstance(height, (int, float)) or not isinstance(width, (int, float)):
            logger.error("Failed to create Rectangle ID %s: Height and width must be numbers.", shape_id)
            raise TypeError("Height and width must be numbers.")

        if height <= 0 or width <= 0:
            logger.error("Failed to create Rectangle ID %s: Height and width must be greater than 0.", shape_id)
            raise ValueError("The Height and width must be greater than 0.")
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
                "shape_type": self.shape_type,
                "width": self.width,
                "height": self.height
                }

