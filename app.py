from flask import *
import pickle

app = Flask(__name__)

with open(r"C:\Users\j\Desktop\projects\project 1\Real Estate GUI\house_price.pickle", 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sqft = int(request.form['sqft'])
        bedroom = int(request.form['bedroom'])
        bathroom = int(request.form['bathroom'])
        result = round(model.predict([[sqft, bedroom, bathroom]])[0])

        # return f"User Input: Sqaure Feet - {name}, Bedroom - {age}, Bathroom - {location} is {model.predict([[name, age, location]])[0]}"
        return render_template('index.html',sqft=sqft, bedroom=bedroom, bathroom=bathroom, model = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
