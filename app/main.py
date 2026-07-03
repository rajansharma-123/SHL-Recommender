from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api import router

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0"
)

app.include_router(router)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>SHL Assessment Recommender</title>
        </head>
        <body style="font-family: Arial; text-align:center; margin-top:80px;">
            <h1>🚀 SHL Assessment Recommender API</h1>
            <p>The API is running successfully.</p>

            <p>
                <a href="/docs">📄 Swagger API Docs</a>
            </p>

            <p>
                <a href="/health">❤️ Health Check</a>
            </p>
        </body>
    </html>
    """