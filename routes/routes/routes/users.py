from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup():
    return {"message": "User signup logic here"}

@router.post("/login")
def login():
    return {"message": "User login logic here"}
