import sqlite3


DATABASE_NAME = "jobs.db"


def create_table():
    """
    Create the job applications table if it does not already exist.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            job_title TEXT NOT NULL,
            status TEXT NOT NULL,
            match_score REAL,
            notes TEXT
        )
        """
    )

    connection.commit()
    connection.close()


def add_application(company, job_title, status, match_score, notes):
    """
    Save a new job application into the database.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO applications (company, job_title, status, match_score, notes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (company, job_title, status, match_score, notes),
    )

    connection.commit()
    connection.close()


def get_applications():
    """
    Get all saved job applications from the database.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, company, job_title, status, match_score, notes
        FROM applications
        ORDER BY id DESC
        """
    )

    applications = cursor.fetchall()

    connection.close()

    return applications

def delete_application(application_id):
    """
    Delete a job application from the database using its ID.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM applications
        WHERE id = ?
        """,
        (application_id,),
    )

    connection.commit()
    connection.close()