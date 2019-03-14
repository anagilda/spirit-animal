from flask import Flask, request, jsonify
import redis
import logging

app = Flask(__name__)

# Logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s:%(name)s: %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S',
    filename='debug.log',
    level=logging.DEBUG
)

# Redis connection details
HOST = "localhost"
PORT = 6379

# TODO: INSERT DATA FROM FILE
# cat animals.txt | redis-cli --pipe
# unix2dos animals.txt

try:
    redis_db0 = redis.Redis(host=HOST, port=PORT, db=0)
    redis_db1 = redis.Redis(host=HOST, port=PORT, db=1)
    
except Exception as e:
    logging.exception(e)

N_ANIMALS = len(redis_db0.keys())

@app.route("/")
def hello():
    return str(N_ANIMALS)

if __name__ == '__main__':
    app.run()