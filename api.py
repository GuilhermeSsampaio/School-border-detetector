from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path
from programa import conversao
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = Path("index.html").read_text(encoding='utf-8')
    return HTMLResponse(content=html_content)

@app.post("/post")
async def post(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
        
    converterImagem=conversao(file_location)
    return FileResponse(converterImagem)