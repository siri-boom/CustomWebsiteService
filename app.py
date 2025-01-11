from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [{
    'id': 1,
    'title': 'Pink Crossandra',
    'price': '2000'
}, 
{
    'id': 2,
    'title': 'Arabian Jasmine',
    'price': '2500'
}, {
    'id': 3,
    'title': 'Lucky Bamboo',
    'price': '2500'
}, {
    'id': 3,
    'title': 'Peace lily',
    'price': '2500'
}
]

@app.route('/')
def index():
  return render_template('home.html', products=PRODUCTS)

@app.route('/products')
def list_products():
  return jsonify(PRODUCTS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
