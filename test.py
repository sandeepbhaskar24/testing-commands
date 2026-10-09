from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

# Define a route for HTTP GET requests at the root path "/"
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
