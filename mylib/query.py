import sqlite3


# Update connection function to accept db_name
def connect_db(db_name):
    return sqlite3.connect(db_name)


def create_table(db_name):
    conn = connect_db(db_name)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS biopics (
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
    conn.commit()
    conn.close()


# Insert a new biopic
def create_biopic(
    db_name,
    title,
    site,
    country,
    year_release,
    box_office,
    director,
    number_of_subjects,
    subject,
    type_of_subject,
    race_known,
    subject_race,
    person_of_color,
    subject_sex,
    lead_actor_actress,
):
    conn = connect_db(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO biopics (title, site, country, year_release, box_office, director, number_of_subjects, subject, type_of_subject, race_known, subject_race, person_of_color, subject_sex, lead_actor_actress) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            title,
            site,
            country,
            year_release,
            box_office,
            director,
            number_of_subjects,
            subject,
            type_of_subject,
            race_known,
            subject_race,
            person_of_color,
            subject_sex,
            lead_actor_actress,
        ),
    )
    conn.commit()
    conn.close()


# Read all biopics
def read_biopics(db_name):
    conn = connect_db(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM biopics")
    results = cursor.fetchall()
    conn.close()
    return results


# Update biopic
def update_biopic(
    db_name,
    title,
    site,
    country,
    year_release,
    box_office,
    director,
    number_of_subjects,
    subject,
    type_of_subject,
    race_known,
    subject_race,
    person_of_color,
    subject_sex,
    lead_actor_actress,
):
    conn = connect_db(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE biopics SET title = ?, site = ?, country = ?, year_release = ?, box_office = ?, director = ?, number_of_subjects = ?, subject = ?, type_of_subject = ?, race_known = ?, subject_race = ?, person_of_color = ?, subject_sex = ?, lead_actor_actress = ?",
        (
            title,
            site,
            country,
            year_release,
            box_office,
            director,
            number_of_subjects,
            subject,
            type_of_subject,
            race_known,
            subject_race,
            person_of_color,
            subject_sex,
            lead_actor_actress,
        ),
    )
    conn.commit()
    conn.close()


# Delete a biopic
def delete_biopic(db_name, title):  # Added db_name
    conn = connect_db(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM biopics WHERE title = ?", (title,))
    conn.commit()
    conn.close()
