import sqlite3
import requests

API_URL = "https://openlibrary.org/search.json"
DB_NAME = "books.db"


def fetch_books(query="python", limit=20):
    """Fetch book records from the Open Library API."""
    response = requests.get(
        API_URL,
        params={"q": query, "limit": limit},
        timeout=10
    )
    response.raise_for_status()

    books = []

    for doc in response.json().get("docs", []):
        title = doc.get("title")
        author = ", ".join(doc.get("author_name", ["Unknown"]))
        year = doc.get("first_publish_year")

        if title:
            books.append((title, author, year))

    return books


def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER,
            UNIQUE(title, author)
        )
    """)


def save_books(conn, books):
    conn.executemany(
        """
        INSERT OR IGNORE INTO books
        (title, author, publication_year)
        VALUES (?, ?, ?)
        """,
        books
    )

    conn.commit()


def display_books(conn):
    rows = conn.execute(
        """
        SELECT title, author, publication_year
        FROM books
        ORDER BY publication_year IS NULL, publication_year
        """
    ).fetchall()

    print(f"{'Title':45} {'Author':30} Year")
    print("-" * 85)

    for title, author, year in rows:
        print(
            f"{title[:44]:45} "
            f"{author[:29]:30} "
            f"{year if year else 'N/A'}"
        )


def main():
    try:
        data = fetch_books()
    except requests.RequestException as exc:
        raise SystemExit(f"API request failed: {exc}")

    with sqlite3.connect(DB_NAME) as conn:
        init_db(conn)
        save_books(conn, data)
        display_books(conn)


if __name__ == "__main__":
    main()
