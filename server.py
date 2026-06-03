from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager
from pydantic import BaseModel, PositiveFloat
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class ShapeCreate(BaseModel):
    shape_type: str
    side: Optional[float] = None
    radius: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

class ShapeUpdate(BaseModel):
    side: Optional[float] = None
    radius: Optional[float] = None
    width: Optional[float] = None
    height: Optional[float] = None

app = FastAPI()

manager = ShapeManager()
logger.info("FastAPI Server initialized and ShapeManager loaded successfully.")

@app.get("/")
def home():
    """Return a welcome message for the shapes CRUD project."""
    return {"Welcome" : "For the CRUD shape project"}

@app.get("/shapes")
def all_shape():
    """Retrieve all shapes currently stored in the system."""
    return manager.get_all_shapes()


@app.get("/shapes/total-area")
def get_total_area():
    """
        Calculate the total area of all shapes combined.

        Raises:
            HTTPException (404): If no shapes exist to calculate area.
    """
    if not manager.shapes:
        raise HTTPException(status_code=404, detail= "No shapes found calculate area")
    area = manager.get_total_area()
    return {"sum of total area" : round(area,2)}

@app.get("/shapes/count")
def count_of_shapes():
    """Return the total number of shapes in the system."""
    shapes_list = manager.get_all_shapes()
    return {"total shapes": len(shapes_list)}

@app.get("/shapes/type/{type}")
def get_shape_type(type:str):
    """
    Filter and retrieve shapes by their specific type.

    Raises:
        HTTPException (404): If no shapes match the requested type.
    """
    new_lst_type = []
    for shape in manager.shapes:
        if shape.shape_type == type:
            new_lst_type.append(shape.to_dict())
    if not new_lst_type:
        logger.warning("Fetch failed: No shapes found for type '%s'", type)
        raise HTTPException(status_code=404, detail="Error: the shape not exist")
    return new_lst_type

@app.get("/shapes/{id}")
def get_shape_by_id(id: int):
    """
    Retrieve a specific shape by its unique ID.

    Raises:
        HTTPException (404): If the shape ID does not exist.
    """
    for shape in manager.shapes:
        if shape.id == id:
            return shape.to_dict()
    logger.warning("Fetch failed: Shape ID %s not found", id)
    raise HTTPException(status_code= 404, detail= "Error: the shape not exist")


@app.post("/shapes", status_code=201)
def create_shape(shape_dict: ShapeCreate):
    """
    Create and store a new shape with a generated ID.

    Raises:
        HTTPException (400): If validation fails (negative values or invalid fields).
    """
    try:
        id = manager.get_new_id()
        shape_dict = shape_dict.model_dump(exclude_unset= True)
        shape_dict["id"] = id
        created_shape = manager.create_shape(shape_dict)
        logger.info("Shape created successfully with ID %s", id)
        return created_shape.to_dict()
    except (KeyError, TypeError, ValueError) as e:
        logger.error("Validation error during shape creation: %s", str(e))
        raise HTTPException(status_code= 400, detail= f"Error:{str(e)}")



@app.put("/shapes/{id}")
def update_shape(id: int,new_data: ShapeUpdate):
    """
    Update an existing shape's attributes by ID.

    Raises:
        HTTPException (404): If the shape is not found.
        HTTPException (400): If the update values or fields are invalid.
    """
    try:
        new_data = new_data.model_dump(exclude_unset= True)
        update_shpe = manager.update_shape(id, new_data)
        if update_shpe is False:
            logger.warning("Update failed: Shape ID %s not found", id)
            raise HTTPException(status_code= 404, detail= "Error in shape update ")

        return update_shpe
    except (KeyError, TypeError, ValueError) as e:
            logger.error("Validation error during update for shape ID %s: %s", id, str(e))
            raise HTTPException(status_code= 400, detail= f"Error:{str(e)}")

@app.delete("/shapes/{id}")
def del_shape(id: int):
    """
    Delete a shape from the system by its ID.

    Raises:
        HTTPException (404): If the shape is not found.
    """
    success =  manager.delete_shape(id)
    if not success:
        logger.warning("Deleted failed: Shape ID %s not found", id)
        raise HTTPException(status_code=404, detail="Error in shape deleted")
    logger.info("Shape ID %s deleted successfully", id)
    return {"message": "Shape deleted successfully"}

