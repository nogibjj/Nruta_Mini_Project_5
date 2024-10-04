"""
Transforms and loads data into the local SQLite3 database
"""

import sqlite3
import csv
import os


def load(dataset="/workspaces/sqlite-lab/data/Biopics.csv"):
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("Biopics.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Biopics")
    c.execute(
        "CREATE TABLE Biopics (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, site TEXT, country TEXT, year_release INTEGER, box_office TEXT, director TEXT)"
    )
    c.executemany(
        "INSERT INTO Biopics (title, site, country, year_release, box_office, director) VALUES (?, ?, ?, ?, ?, ?)",
        payload,
    )
    conn.commit()
    conn.close()
    return "Biopics"
