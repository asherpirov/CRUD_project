from fastapi import FastAPI
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
def get_shape_id():
    return manager.get_all_shapes()



