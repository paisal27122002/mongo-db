from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Set up a MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    # Insert the data into MongoDB
    collection.insert_one({'name': name, 'email': email})

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
