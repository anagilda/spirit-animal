import redis

HOST = "localhost"
PORT = 6379

animals = redis.Redis(host=HOST, port=PORT, db=0, decode_responses=True)
adjectives = redis.Redis(host=HOST, port=PORT, db=1, decode_responses=True)
sessions = redis.Redis(host=HOST, port=PORT, db=2)

NUM_ANIMALS = len(animals.keys())
NUM_ADJECTIVES = len(adjectives.keys())

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