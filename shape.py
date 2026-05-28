class Shape:
    """Represents a shape, inheriting from Shape."""
    def __init__(self, shape_id: int, shape_type: str) -> None:
        """Initialize a Shape with an ID."""
        self.id = shape_id
        self.shape_type = shape_type

    def get_area(self) -> float:
        """Calculate and return the area of the shape."""
        pass
    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the shape."""
        pass
    def to_dict(self) -> dict:
        """Return a dictionary representation of the shape."""
        pass