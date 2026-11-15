import psycopg2
from config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(30) UNIQUE NOT NULL
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("PhoneBook table created successfully!")