from flask import Flask, request, jsonify, render_template
from database import get_db_connection

app = Flask(__name__)

# Strona główna aplikacji
@app.route("/")
def index():
    return render_template("index.html")  # Ładuje plik HTML z folderu "templates"

# Pobierz wszystkie produkty (API)
@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

# Dodaj nowy produkt (API)
@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")  # Teraz jest typu TEXT

    if not name or not quantity:
        return jsonify({"error": "Nieprawidłowe dane"}), 400

    conn = get_db_connection()
    conn.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
    conn.commit()
    conn.close()

    return jsonify({"message": "Produkt został dodany"}), 201


# Oznacz produkt jako zakupiony (API)
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    conn = get_db_connection()
    conn.execute("UPDATE products SET status = 1 WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Produkt został oznaczony jako zakupiony"}), 200

# Usuń produkt (API)
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Produkt został usunięty"}), 200

if __name__ == "__main__":
    app.run(debug=True)
