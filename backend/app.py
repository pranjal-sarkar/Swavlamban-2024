from fastapi import FastAPI, UploadFile, File
from ocr import extract_text_from_image
from rag import extract_structured_data
from database import save_contact
import os

app = FastAPI()

@app.post("/process-report/")
async def process_report(file: UploadFile = File(...)):
    # Save the file locally in the temp folder
    file_location = f"./temp/{file.filename}"
    with open(file_location, "wb+") as f:
        f.write(file.file.read())

    # Extract text using OCR
    text = extract_text_from_image(file_location)
    
    # Use RAG to extract structured data
    structured_data = extract_structured_data(text)
    
    # Example of structured_data: [{"lat": 12.34, "lon": 45.67, "speed": 12, "description": "Unidentified Vessel"}]
    for contact in structured_data:
        save_contact(contact['lat'], contact['lon'], contact['speed'], contact['description'])

    return {"extracted_data": structured_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
