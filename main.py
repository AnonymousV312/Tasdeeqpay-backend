from fastapi import FastAPI
from routes import users, orders, disputes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(orders.router)
app.include_router(disputes.router)

@app.get("/")
def read_root():
    return {"message": "Tasdeeq API is running"}
