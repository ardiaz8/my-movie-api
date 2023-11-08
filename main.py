from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

# FastAPI instance
app = FastAPI()
app.title = "My FastApi App"
app.version = "0.0.1"

# Add the error handler
app.add_middleware(ErrorHandler)

# Include the movie router
app.include_router(movie_router)

# Include the user router
app.include_router(user_router)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Function to get the home page
@app.get('/', tags=['Home'])
def home_page():
    message = HTMLResponse("""  
    <html>
        <head>
            <title>Movies API</title>
        </head>
        <body>
            <h1>Welcome to the Movie Description API</h1>
            <p>You can create, read, update or delete any movie</p>
        </body>
    </html>
    """)
    return message