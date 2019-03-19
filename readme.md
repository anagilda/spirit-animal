# Spirit Animal

Simple app that computes a random adjective + animal for a given name.

This app has a limit of requests per session (10 requests for every 5 minutes per ip address). 

## Using the app

_Note: [base_url] represents either a deployed app url or a localhost url._

_Note: { } = required parameter._

### **GET /spirit-animal/{name}**

Example usage :

[[base_url]/spirit-animal/Ana](https://spirit-animal.herokuapp.com/spirit-animal/ana)

Example output:
```json
{"name":"Ana","spirit_animal":"Fruity Owl"}
```

## Running the app locally
_Note: you must have Python 3 and Redis installed._

#### Initial setup

1. Install requirements.

        pip install -r requirements.txt

2. Insert data to Redis.

        cat server/animals.txt | redis-cli -n 0 --pipe
        cat server/adjectives.txt | redis-cli -n 1 --pipe
    
#### Running the application

* Open the terminal in the `server` folder and run:    
    
        flask run
    