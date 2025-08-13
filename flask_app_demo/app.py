from flask import Flask, render_template

app = Flask(__name__)

# Dummy product data
products = [
    {"id": 1, "name": "Laptop", "price": 50000, "image": "images/laptop.jpg"},
    {"id": 2, "name": "Headphones", "price": 10000, "image": "images/headphones.jpg"},
    {"id": 3, "name": "smartphones", "price": 25000, "image": "images/smartphone.jpg"}
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template("product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
