import sqlite3

conn = sqlite3.connect('./data/naval_reports.db')
cursor = conn.cursor()

# Create a table to store contacts
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY, 
    latitude REAL, 
    longitude REAL, 
    speed REAL, 
    description TEXT
)
''')

def save_contact(lat, lon, speed, description):
    cursor.execute("INSERT INTO contacts (latitude, longitude, speed, description) VALUES (?, ?, ?, ?)", 
                   (lat, lon, speed, description))
    conn.commit()
