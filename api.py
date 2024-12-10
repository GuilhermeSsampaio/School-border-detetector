from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from programa import conversao
import zipfile
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = Path("index.html").read_text(encoding='utf-8')
    return HTMLResponse(content=html_content)

@app.post("/post")
async def post(files: list[UploadFile] = File(...)):
    output_files = []
    for file in files:
        file_location = f"temp_{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        output_path = f"resultado_{file.filename}"
        conversao(file_location, output_path)
        output_files.append(output_path)
        os.remove(file_location)

    if len(output_files) > 1:
        zip_filename = "resultados.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in output_files:
                zipf.write(file)
                os.remove(file)
        return FileResponse(zip_filename, media_type='application/zip', filename=zip_filename)
    else:
        return FileResponse(output_files[0], media_type='image/jpeg', filename=output_files[0])