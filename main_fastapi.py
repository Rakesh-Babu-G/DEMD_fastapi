# Importing the required package
from fastapi import FastAPI
import uvicorn ## ASGI server

# Defining the name (will fetch from the actual file name)
app = FastAPI()

# Defining the path or url attahced after the local ip
@app.get('/')
# Function that would be executed when the above URL is hit.
def home():
    return f"Welcome to FASTAPI intro class."
    
# Defining second url
@app.get('/testname')
# Function that should be executed when this URL is hit
def print_name(name:str):
    return f"Welcome to Fastapi intro class, {name}!"

if __name__ == "__main__":
    uvicorn.run()
    
