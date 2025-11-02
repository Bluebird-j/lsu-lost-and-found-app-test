from fastapi.responses import JSONResponse
from uuid import UUID
from fastapi import HTTPException, APIRouter
from Schemas.itemSchema import ItemCreate, ItemUpdate, ItemResponse
from Service.itemService import (
    get_all_items as service_get_all_items,
    create_item as service_create_item,
    get_item_by_id as service_get_item_by_id,
    update_item as service_update_item,
    delete_item as service_delete_item 
    )


router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=list[ItemResponse])
def read_items():
    data = service_get_all_items()
    if not data:
        raise HTTPException(status_code=404, detail="No items found")
    return data

@router.get("/{item_id}")
def get_item_by_id(item_id: UUID):
    data = service_get_item_by_id(str(item_id))
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(content={"item": data[0]})

@router.post("/", response_model=list[ItemResponse])
def create_item(item: ItemCreate):
    data = service_create_item(item.dict())
    if not data:
        raise HTTPException(status_code=400, detail="Failed to create item")
    return data

@router.put("/{item_id}", response_model=list[ItemResponse])
def update_item(item_id: str, item: ItemUpdate):
    data = service_update_item(item_id, item.dict())
    if not data:
        raise HTTPException(status_code=400, detail="Failed to update item")
    return data

@router.delete("/{item_id}")
def delete_item(item_id: str):
    data = service_delete_item(item_id)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found or already deleted")
    return {"message": "Item deleted successfully"}