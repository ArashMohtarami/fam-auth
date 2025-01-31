"""
This script runs the FastAPI application using Uvicorn.

It serves as the entry point for the FastAPI application and is typically used 
during development to launch the app with hot reloading enabled.

The script will run the app at `http://0.0.0.0:8000`.

Usage:
    Run this script directly with Python:
        python src/core/routers.py
"""

import uvicorn

if __name__ == "__main__":
    """
    Run the FastAPI app using Uvicorn as the ASGI server.
    
    The application will be hosted on `http://0.0.0.0:8000` and will automatically 
    reload during development if any code changes are detected.
    
    Parameters:
        host (str): The host address to bind the application. Default is "0.0.0.0".
        port (int): The port number to bind the application. Default is 8000.
        log_level (str): The level of logging. Default is "info".
        reload (bool): If True, enables automatic reloading of the app on code changes.
    
    Returns:
        None
    """
    uvicorn.run(
        "src.core.routers:app", host="0.0.0.0", port=8000, log_level="info", reload=True
    )
