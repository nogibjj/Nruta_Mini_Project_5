import sqlite3


def connect_db(db_name):
    return sqlite3.connect(db_name)


def create_biopic(title, site, country, year_release, box_office, director):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Biopics (title, site, country, year_release, box_office, director) VALUES (?, ?, ?, ?, ?, ?)",
        (title, site, country, year_release, box_office, director),
    )
    conn.commit()
    conn.close()


def read_biopics():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Biopics")
    results = cursor.fetchall()
    conn.close()
    return results


def update_biopic(title, site, country, year_release, box_office, director):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Biopics SET title = ?, site = ?, country = ?, year_release = ?, box_office = ?, director = ? WHERE id = ?",
        (title, site, country, year_release, box_office, director, biopic_id),
    )
    conn.commit()
    conn.close()


def delete_biopic(biopic_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Biopics WHERE id = ?", (biopic_id,))
    conn.commit()
    conn.close()
