from flask import Flask, request, jsonify
from flask import render_template
from flask import Markup
import markdown
import os
from spirit_animals import *

app = Flask(__name__)
app.debug = False
    
@app.route("/")
def homepage():
    with open(os.path.join(os.pardir, 'readme.md'), 'r') as file:
        content = file.read()
        content = markdown.markdown(content)
    return render_template('index.html', instructions=Markup(content))

@app.route('/spirit-animal/<name>')
def spirit_animal(name):
    overlimit, ttl = check_ip_limit(request.remote_addr)
    if not overlimit:
        animal_index = animal_value(name) % NUM_ANIMALS
        adj_index = adjective_value(name) % NUM_ADJECTIVES
        return jsonify(
            name = name, 
            spirit_animal = ' '.join([
                adjectives.get(adj_index), animals.get(animal_index)
            ])
        ), 200
    else:
        ttl_mins = ttl//60
        ttl_sec = (ttl-ttl_mins) % 60
        return jsonify(
            error = (
                'Your limit of requests for this session has been reached. '
                + 'Try again in {} mins and {} secs.'.format(ttl_mins, ttl_sec)
            )
        ), 401

if __name__ == '__main__':
    app.run()