import redis
# Redis connection details
HOST = "localhost"
PORT = 6379

# TODO: INSERT DATA FROM FILE
# unix2dos animals.txt
# cat animals.txt | redis-cli --pipe

animals = redis.Redis(host=HOST, port=PORT, db=0, decode_responses=True)
adjectives = redis.Redis(host=HOST, port=PORT, db=1, decode_responses=True)
sessions = redis.Redis(host=HOST, port=PORT, db=2)

N_ANIMALS = len(animals.keys())

def animal_value(name):
    '''
    Computes the animal value of a given name.

    Requires: name (str) - someone's name.
    Ensures: an integer with the calculation obtained for the given name.
    '''
    res = 0
    for pos, letter in enumerate(name.lower()):
        res += (pos+1) * ord(letter)
    return res

def adjective_value(name):
    '''
    Computes the adjective value of a given name.

    Requires: name (str) - someone's name.
    Ensures: an integer with the calculation obtained for the given name.
    '''
    res = 2 * ord(name[0]) - 1
    for letter in name.lower():
        res += ord(letter)
    return res