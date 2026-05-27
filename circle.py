from shape import Shape
import math
import logging

logger = logging.getLogger(__name__)

class Circle(Shape):
    """Represents a circle shape, inheriting from Shape."""
    def __init__(self, shape_id: int, radius: float) -> None:
        """Initialize a circle with an ID and radius."""
        super().__init__(shape_id, "circle")
        if not isinstance(radius, (int, float)) or radius <= 0:
            logger.error("Failed to create Circle ID %s: Radius must be greater than 0.", shape_id)
            raise ValueError("The Radius must be greater than 0.")

        self.radius = radius
        logger.info("Created Circle object with ID: %s", shape_id)

    def get_area(self) -> float:
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.radius

    def to_dict(self) -> dict:
        """Return a dictionary representation of the circle."""
        return {"id": self.id,
                "type": self.shape_type,
                "radius": self.radius
                }



