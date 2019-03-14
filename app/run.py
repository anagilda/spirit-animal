from flask import Flask, request, jsonify
from flask import render_template
from flask import Markup
import markdown
import os
from spirit_animals import *

app = Flask(__name__)
    
@app.route("/")
def homepage():
    with open(os.path.join(os.pardir, 'readme.md'), 'r') as file:
        content = file.read()
        content = markdown.markdown(content)
    return render_template('index.html', instructions=Markup(content))

@app.route('/spirit-animal/<name>')
def spirit_animal(name):
    animal_index = animal_value(name) % NUM_ANIMALS
    adj_index = adjective_value(name) % NUM_ADJECTIVES
    return jsonify(
        name = name, 
        spirit_animal = ' '.join([
            adjectives.get(adj_index), animals.get(animal_index)
        ])
    )

if __name__ == '__main__':
    app.run()