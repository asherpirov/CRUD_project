from fastapi import FastAPI, HTTPException
from shape_manager import ShapeManager

app = FastAPI()

manager = ShapeManager()

@app.get("/")
def home():
    return {"Welcome" : "For the CRUD shape project"}

@app.get("/shapes")
def all_shape():
    return manager.get_all_shapes()


@app.get("/shapes/total-area")
def get_total_area():
    if not manager.shapes:
        raise HTTPException(status_code=404, detail= "No shapes found calculate area")
    area = manager.get_total_area()
    return {"sum of total area" : round(area,2)}


@app.get("/shapes/{id}")
def get_shape_by_id(id: int):
    for shape in manager.shapes:
        shape = shape.to_dict()
        if shape["id"] == id:
            return shape
    return []


@app.post("/shapes", status_code=201)
def create_shape(shape_dict: dict):
    id = manager.get_new_id()
    shape_dict["id"] = id
    created_shape = manager.create_shape(shape_dict)
    return created_shape.to_dict()


@app.put("/shapes/{id}")
def update_shape(id: int,new_data: dict):
    update_shpe = manager.update_shape(id, new_data)
    if update_shpe is False:
        raise HTTPException(status_code= 404, detail= "Error in shape update ")

    return update_shpe

@app.delete("/shapes/{id}")
def del_shape(id: int):
    if manager.delete_shape(id) is False:
        raise HTTPException(status_code=404, detail="Error in shape deleted")
    return manager.delete_shape(id)