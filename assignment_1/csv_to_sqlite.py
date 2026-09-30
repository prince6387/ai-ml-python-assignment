import csv
import sqlite3

CSV_FILE = "users.csv"
DB_NAME = "users.db"


def read_users(path):
    with open(
        path,
        newline="",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(f)

        return [
            (
                r["name"].strip(),
                r["email"].strip().lower()
            )
            for r in reader
            if r.get("name") and r.get("email")
        ]


def main():
    rows = read_users(CSV_FILE)

    with sqlite3.connect(DB_NAME) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)

        conn.executemany(
            """
            INSERT OR IGNORE INTO users
            (name, email)
            VALUES (?, ?)
            """,
            rows
        )

        conn.commit()

        for row in conn.execute(
            "SELECT id, name, email FROM users"
        ):
            print(row)


if __name__ == "__main__":
    main()
