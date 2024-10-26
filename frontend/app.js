var map = L.map('map').setView([12.34, 45.67], 5);

// Set up the map layer (OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Function to update the map with new contact information
function updateMap(lat, lon, info) {
    var marker = L.marker([lat, lon]).addTo(map);
    marker.bindPopup(info).openPopup();
}

// Fetch data from the FastAPI backend (for demonstration)
fetch('http://localhost:8000/get-contacts/')
    .then(response => response.json())
    .then(data => {
        data.forEach(contact => {
            updateMap(contact.lat, contact.lon, `Description: ${contact.description}, Speed: ${contact.speed}`);
        });
    });
