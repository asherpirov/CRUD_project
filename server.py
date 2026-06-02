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

@app.get("/shapes/{id}")
def get_shape_by_id(id: int):
    try:
        for shape in manager.shapes:
            shape = shape.to_dict()
            if shape["id"] == id:
                return shape
    except:
        raise HTTPException(status_code=404,
            detail="the shape ot exist")

