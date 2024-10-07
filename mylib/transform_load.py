"""
Transforms and loads data into the local SQLite3 database
"""

import sqlite3
import csv
import os


def load(dataset="biopics.csv"):
    # Open the file with encoding and error handling to avoid UnicodeDecodeError
    with open(dataset, newline="", encoding="utf-8", errors="replace") as f:
        payload = list(csv.reader(f, delimiter=","))  # Read the whole file at once
        print("CSV Contents:", payload)  # Debugging: print to check CSV contents

    # Connect to the SQLite database
    conn = sqlite3.connect("Biopics.db")
    c = conn.cursor()

    # Drop the table if it exists, and recreate it
    c.execute("DROP TABLE IF EXISTS Biopics")
    c.execute(
        """CREATE TABLE Biopics (
            title TEXT, 
            site TEXT, 
            country TEXT, 
            year_release INTEGER, 
            box_office TEXT, 
            director TEXT,
            number_of_subjects INTEGER,
            subject TEXT,
            type_of_subject TEXT,
            race_known TEXT,
            subject_race TEXT,
            person_of_color TEXT,
            subject_sex TEXT,
            lead_actor_actress TEXT
        )"""
    )

    # Skip the header (first row) if necessary
    c.executemany(
        "INSERT INTO Biopics (title, site, country, year_release, box_office, director, number_of_subjects, subject, type_of_subject, race_known, subject_race, person_of_color, subject_sex, lead_actor_actress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        payload[1:],
    )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return "Biopics table created successfully"
