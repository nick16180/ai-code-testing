from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse


app = FastAPI(title="Hello API", version="1.0.0")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return '''<html><head>
        <title>Hello!</title>
    </head><body>
        <div style="font-size: 24px; color: #ff6b6b;">
            <h1>Hello from FastAPI! 🐍</h1>
            <p>This is a simple hello endpoint.</p>
        </div>
    </body></html>'''


@app.get("/hello", response_class=JSONResponse)
async def hello():
    return {"message": "hello", "status": "success"}


@app.get("/status")
async def status_endpoint():
    """Health check endpoint"""
    return {"status": "healthy", "service": "hello-api"}


# Middleware for timing requests
import time

@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.monotonic()
    response = await call_next(request)
    processing_time = time.monotonic() - start_time
    response.headers["X-Processing-Time"] = str(processing_time)
    return response

