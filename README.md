
# Maritime Contact Tracking System

This project uses OCR (Optical Character Recognition) and Retrieval-Augmented Generation (RAG) to extract information from naval surveillance reports and plot identified contacts (ships, aircraft, submarines, etc.) on a radar/map interface for real-time situational awareness.
## Features

1. OCR-based Text Extraction: Extracts text from scanned or photographed naval reports.
2. RAG Information Retrieval: Uses Hugging Face’s RAG model to intelligently extract structured data such as coordinates, vessel types, speed, and direction.
3. Map-based Visualization: Displays contacts on a dynamic Leaflet.js map with relevant metadata.
4. Automated Alerts: Detects restricted-area breaches and unidentified contacts.
5. Real-time Updates: Automatically refreshes the map with new contacts as they are reported.

## Tech Stack

1. OCR: Tesseract OCR
2. RAG Model: Hugging Face's rag-sequence-nq
3. Map Visualization: Leaflet.js
4. Backend: FastAPI (can use Flask as an alternative)
5. Database: SQLite (for offline data storage)
## Installation Instructions

1. Install Python and Tesseract OCR:

Install Python from here.
Install Tesseract from here.

2. Clone the repository

git clone https://github.com/pranjal-sarkar/Swavlamban-2024.git
cd maritime-contact-tracking

3. Install Dependencies

pip install -r requirements.txt

4. Start the FastAPI Server

uvicorn main:app --reload

5. Open the Frontend Map

Open frontend/index.html in a browser.
## Usage

1. Upload scanned naval reports through the /upload/ endpoint:

curl -F "file=@path/to/report.jpg" http://127.0.0.1:8000/upload/

2. View contacts on the map interface by opening index.html.

3. Example Report:

At 05:30 UTC, an unidentified vessel was sighted at latitude 12.34 N, longitude 45.67 E, moving at 12 knots towards the northeast.

This will extract the following:
Time: 05:30 UTC
Coordinates: (12.34 N, 45.67 E)
Speed: 12 knots
Direction: Northeast
Type: Unidentified vessel
## Alerts

The system automatically scans for:

1. Restricted Area Breaches: Detects if any vessel enters predefined restricted areas.
2. Unidentified Objects: Alerts the operator when a contact is detected without prior knowledge.
## Contributing

1. Fork the repository.
2. Create a feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -m "Added feature").
4. Push the branch (git push origin feature-name).
5. Open a Pull Request.
## Contact

For queries, contact the project maintainer at tataisarkar2001@gmail.com.