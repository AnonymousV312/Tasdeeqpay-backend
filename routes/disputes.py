from fastapi import APIRouter

router = APIRouter(prefix="/dispute", tags=["disputes"])

@router.post("/raise")
def raise_dispute():
    return {"message": "Dispute raised"}
