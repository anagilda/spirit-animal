import redis

LIMIT = 3 # 10
TIME_LIMIT = 30 # 300  

HOST = "localhost"
PORT = 6379

animals = redis.Redis(host=HOST, port=PORT, db=0, decode_responses=True)
adjectives = redis.Redis(host=HOST, port=PORT, db=1, decode_responses=True)
sessions = redis.Redis(host=HOST, port=PORT, db=2, decode_responses=True)

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

def check_ip_limit(ip):
    '''
    Keeps track of the number of requests for a given ip address and checks if 
    the limit of requests for this ip has been reached.
    
    Requires: ip (str) - an ip address.
    Ensures: 
        - overlimit (bool) - True if the limit of requests was achieved, False
        otherwise;
        - sessions.ttl(ip) (int) - number of seconds until the session for the 
        given ip address is cleared.
    '''
    overlimit = False
    ip_requests = sessions.get(ip)
    if ip_requests:
        if int(ip_requests) < LIMIT:
            sessions.incr(ip)
        else:
            overlimit = True
    else:
        sessions.incr(ip)
        sessions.expire(ip, TIME_LIMIT)
    return overlimit, sessions.ttl(ip)
