from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

from openai_client import generate

@app.post("/summarize")
async def summarize_text(request: Request):
    try:
        form_data = await request.json()
        input_text = form_data.get('text','')
        print("INPUT TEXT RECEIVED:", repr(input_text))
        # user_type = form_data.get('user_type', 'default')
        result = generate(TEXT=input_text)
        return {"success": True, "summary": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
