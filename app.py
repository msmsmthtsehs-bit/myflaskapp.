from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات منتجات تجريبية (يمكنك تعديلها أو ربطها بقاعدة بيانات)
products = [
    {
        "id": 1,
        "title": "كريم مرطب",
        "type": "كريمات",
        "price": "80",
        "images": ["images/cream1.jpg", "images/cream2.jpg"]
    },
    {
        "id": 2,
        "title": "سيروم فيتامين C",
        "type": "سيرومات",
        "price": "120",
        "images": ["images/serum1.jpg"]
    }
]

@app.route('/')
def index():
    return render_template("index.html", products=products, page_title="الرئيسية")

@app.route('/product/<int:product_id>')
def product(product_id):
    prod = next((p for p in products if p["id"] == product_id), None)
    if not prod:
        return "المنتج غير موجود", 404
    return render_template("product.html", product=prod, page_title=prod["title"])

@app.route('/cart')
def cart():
    return render_template("cart.html", page_title="سلة التسوق")

@app.route('/checkout')
def checkout():
    return render_template("checkout.html", page_title="إتمام الشراء")

@app.route('/admin')
def admin():
    return render_template("admin.html", page_title="لوحة التحكم")

@app.route('/search')
def search():
    q = request.args.get("q", "")
    filt = [p for p in products if q in p["title"] or q in p["type"]]
    return render_template("index.html", products=filt, page_title=f"نتائج البحث: {q}")

if __name__ == '__main__':
    app.run(debug=True)
