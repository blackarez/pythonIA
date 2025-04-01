from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from schemas import Plato

app = FastAPI(
    title="Mi API FastAPI",
    description="Una API creada con FastAPI",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulate a database with a list
platos_db = []

@app.post("/platos/", response_model=Plato, status_code=status.HTTP_201_CREATED)
async def create_plato(plato: Plato):
    """
    Create a new dish in the database.
    
    Args:
        plato (Plato): The dish object to be created
        
    Returns:
        Plato: The created dish
        
    Raises:
        HTTPException: If a dish with the same ID already exists
    """
    # Check if a dish with the same ID already exists
    if any(p.id == plato.id for p in platos_db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un plato con este ID"
        )
    platos_db.append(plato)
    return plato

@app.get("/platos/", response_model=List[Plato])
async def read_platos():
    """
    Get all dishes from the database.
    
    Returns:
        List[Plato]: A list of all dishes
    """
    return platos_db

@app.get("/platos/{plato_id}", response_model=Plato)
async def read_plato(plato_id: int):
    """
    Get a specific dish by its ID.
    
    Args:
        plato_id (int): The ID of the dish to retrieve
        
    Returns:
        Plato: The requested dish
        
    Raises:
        HTTPException: If the dish is not found
    """
    plato = next((p for p in platos_db if p.id == plato_id), None)
    if plato is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plato no encontrado"
        )
    return plato

@app.put("/platos/{plato_id}", response_model=Plato)
async def update_plato(plato_id: int, plato_actualizado: Plato):
    """
    Update an existing dish in the database.
    
    Args:
        plato_id (int): The ID of the dish to update
        plato_actualizado (Plato): The updated dish data
        
    Returns:
        Plato: The updated dish
        
    Raises:
        HTTPException: If the dish is not found
    """
    plato_index = next((i for i, p in enumerate(platos_db) if p.id == plato_id), None)
    if plato_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plato no encontrado"
        )
    platos_db[plato_index] = plato_actualizado
    return plato_actualizado

@app.delete("/platos/{plato_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_plato(plato_id: int):
    """
    Delete a dish from the database.
    
    Args:
        plato_id (int): The ID of the dish to delete
        
    Raises:
        HTTPException: If the dish is not found
    """
    plato_index = next((i for i, p in enumerate(platos_db) if p.id == plato_id), None)
    if plato_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Plato no encontrado"
        )
    platos_db.pop(plato_index)
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888) 