from shape import Shape
import math
import logging

logger = logging.getLogger(__name__)

class Square(Shape):
    """Represents a square shape, inheriting from Shape."""
    def __init__(self, shape_id: int, side: float) -> None:
        """Initialize a Square with an ID and side."""
        super().__init__(shape_id, "square")
        self.side = side
        logger.info("Created Square object with ID: %s", shape_id)



    def get_area(self) -> float:
        """Calculate and return the area of the square."""
        return self.side ** 2

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the square."""
        return 4 * self.side

    def to_dict(self) -> dict:
        """Return a dictionary representation of the square."""
        return {"id": self.id,
                "type": self.shape_type,
                "side": self.side
                }
