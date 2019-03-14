from flask import Flask, request, jsonify
from spirit_animals import *

app = Flask(__name__)
    
@app.route("/")
def homepage():
    return str(N_ANIMALS)

@app.route('/spirit-animal/<name>')
def spirit_animal(name):
    animal_index = animal_value(name) % N_ANIMALS
    return jsonify(name=name, spirit_animal=animals.get(animal_index))

if __name__ == '__main__':
    app.run()