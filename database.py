import sqlite3

# Inicjalizacja bazy danych
def init_db():
    conn = sqlite3.connect("shopping_list.db")
    cursor = conn.cursor()

    # Tworzenie tabeli products
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity TEXT NOT NULL,
            status BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# Funkcja do połączenia z bazą danych
def get_db_connection():
    conn = sqlite3.connect("shopping_list.db")
    conn.row_factory = sqlite3.Row  # Umożliwia zwracanie wyników jako słowniki
    return conn

# Wywołanie inicjalizacji przy uruchomieniu
if __name__ == "__main__":
    init_db()
    print("Baza danych została zainicjalizowana.")
