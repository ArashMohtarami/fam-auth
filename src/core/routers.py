from fastapi import FastAPI
from src.routers.user import router

# Initialize the FastAPI application
app = FastAPI()
"""
FastAPI application instance.

This is the main entry point of the FastAPI application. It initializes the application
and includes routers for handling various API endpoints.

Attributes:
    app (FastAPI): An instance of the FastAPI application that handles routing and HTTP requests.
"""

# Include the user router for user-related endpoints
app.include_router(router)
"""
Include the user router.

This line includes the `router` from the `user` module, which contains all the user-related 
endpoints. The router is added to the main application to handle requests related to users.

Attributes:
    router (APIRouter): The router from the `user` module that defines user-related API routes.
"""
