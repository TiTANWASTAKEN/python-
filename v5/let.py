from flask import Flask, render_template

app = Flask(__name__)

def display_fruit(fruit_function):
    return fruit_function()

def apple_function():
    return "Apple"

def banana_function():
    return "Banana"

def orange_function():
    return "Orange"

def grape_function():
    return "Grape"

def mango_function():
    return "Mango"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display/<fruit>')
def display(fruit):
    result = display_fruit(globals()[f"{fruit.lower()}_function"])
    return result

if __name__ == '__main__':
    app.run(debug=True)
