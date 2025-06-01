from fastapi import APIRouter

router = APIRouter(prefix="/order", tags=["orders"])

@router.post("/create")
def create_order():
    return {"message": "Order created"}
