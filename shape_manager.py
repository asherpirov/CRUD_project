import logging
import json
from rectangle import Rectangle
from circle import Circle
from square import Square

logger = logging.getLogger(__name__)

class ShapeManager:
    """Manages CRUD operations and JSON persistence for geometric shapes."""
    def __init__(self):
        """Initialize the manager and load existing shapes from JSON."""
        logger.info("Shape_Manager Initializer")
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape_dict: dict):
        """Add a new shape to the list and save changes."""
        fields = ["side", "radius", "width", "height"]
        for field in fields:
            if field in shape_dict and shape_dict[field] is not None:
                if shape_dict[field] <= 0:
                    raise ValueError(f"Error: {field} must be greater than 0")

        if shape_dict["shape_type"] == "rectangle":
            new_shape = Rectangle(shape_dict["id"] ,shape_dict["height"],shape_dict["width"])
        elif shape_dict["shape_type"] == "circle":
            new_shape = Circle(shape_dict["id"] ,shape_dict["radius"])
        elif shape_dict["shape_type"] == "square":
            new_shape = Square(shape_dict["id"] ,shape_dict["side"])
        else:
            logger.error("Shape type not recognized")
            raise ValueError("Shape type not recognized")

        logger.info("Creating new shape: {%s}", new_shape.to_dict())
        self.shapes.append(new_shape)
        print(f"The shape{new_shape.to_dict()} created")
        logger.info("Shape: {%s} append to the shape list", shape_dict["shape_type"])
        self.save_to_json()
        return new_shape


    def get_all_shapes(self):
        """Return a list of all currently managed shapes."""
        if not self.shapes:
            return []
        return self.shapes

    def update_shape(self, shape_id, new_data: dict):
        """Find a shape by ID and update its attributes."""
        fields = ["side", "radius", "width", "height"]
        for field in fields:
            if field in new_data and new_data[field] is not None:
                if new_data[field] <= 0:
                    raise ValueError(f"Cannot update {field} with a value less than or equal to 0")
        for shape in self.shapes:
            if shape.id == shape_id:
                if shape.shape_type == "rectangle":
                    if "side" in new_data or "radius" in new_data:
                        raise ValueError("Rectangle can only have width and height")
                    if "width" in new_data:
                        shape.width = new_data["width"]
                    if "height" in new_data:
                        shape.height = new_data["height"]
                elif shape.shape_type == "square":
                    if "radius" in new_data or "width" in new_data or "height" in new_data:
                        raise ValueError("Square can only have a side attribute")
                    if "side" in new_data:
                        shape.side = new_data["side"]
                elif shape.shape_type == "circle":
                    if "side" in new_data or "width" in new_data or "height" in new_data:
                        raise ValueError("Circle can only have a radius attribute")
                    if "radius" in new_data:
                        shape.radius = new_data["radius"]
                logger.info("Successfully update %s", shape.to_dict())
                self.save_to_json()
                return True

        logger.warning("Shape ID %s not found for update.", shape_id)
        return False

    def delete_shape(self, shape_id):
        """Remove a shape by ID from the list and save changes."""
        for shape in self.shapes:
            if shape.id == shape_id:
                self.shapes.remove(shape)
                logger.info("Shape ID %s successfully deleted.", shape_id)
                self.save_to_json()
                return True

        logger.warning("The ID %s was not found in the file. Delete failed.", shape_id)
        return False


    def save_to_json(self):
        """Serialize and save the current shapes list to a JSON file."""
        data_to_save = []
        for shape in self.shapes:
            data_to_save.append(shape.to_dict())

        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump(data_to_save,file,indent = 4)

        logger.info("Successfully saved %s shapes to shapes.json", len(data_to_save))

    def load_from_json(self):
        """Load and parse shapes from the JSON file into memory."""
        try:
            with open("shapes.json", "r", encoding="utf-8") as file:
                shapes_list = json.load(file)
                logger.info("Shape loaded from JSON")
                for shape in shapes_list:
                    try:
                        self.create_shape(shape)
                    except (ValueError,TypeError,KeyError) as e:
                        logger.warning("Skipping invalid shape in JSON. Error: %s", e)
        except FileNotFoundError:
            logger.info("shapes.json not found. Starting with an empty shape list.")
            self.shapes = []
        except json.JSONDecodeError:
            logger.warning("Failed to decode JSON: The file shapes.json is empty.")
            self.shapes = []


    def get_new_id(self):
        max_id = 0
        for shape in self.shapes:
            if shape.id > max_id:
                max_id = shape.id

        new_id = max_id + 1
        logger.info("New ID find %s", new_id)
        return new_id

    def get_total_area(self):
        """return sum of area for all shapes"""
        sum_of_area = 0
        for shape in self.shapes:
            sum_of_area += shape.get_area()
        return sum_of_area






