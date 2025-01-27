from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "read": False},
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "read": False,
    },
    {
        "id": 3,
        "title": "Design Patterns",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "read": False,
    },
]


# Consultar todos os livros
@app.route("/books", methods=["GET"])
def get_book():
    return jsonify(books)


# Consultar um livro por ID
@app.route("/books/<int:id>", methods=["GET"])
def get_book_by_id(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return None

# editar um livro por ID
@app.route("/books/<int:id>", methods=["PUT"])
def update_book_by_id(id):
    updated_book = request.get_json()
    for index, book in enumerate(books):
        if book["id"] == id:
            books[index].update(updated_book)
            return jsonify(book[index])
    return None

# Adicionar um livro
@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

app.run(port=5000, host="localhost", debug=True)
