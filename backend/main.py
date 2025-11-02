from fastapi import FastAPI
from Controllers import itemController
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(title="Lost & Found API")

# include routers
app.include_router(itemController.router)

# Scalar Docs
app.mount("/Scalar", get_scalar_api_reference(title="Lost & Found API"))

@app.get("/")
def root():
    return {"message": "Lost & Found backend running 🚀"}
