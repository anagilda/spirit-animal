# Spirit Animal

### Using the app

* Coming soon...


### Running locally
_Note: you must have Python 3 and Redis installed._

_Note: steps 1 & 2 only needed once._

1. Install requirements.

    `pip install -r requirements.txt`

2. Insert data to Redis.

        cat animals.txt | redis-cli -n 0 --pipe
        cat adjectives.txt | redis-cli -n 1 --pipe
    
3. Run the application.
    
        cd app
        python run.py
    