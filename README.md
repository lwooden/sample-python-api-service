
# Sample Python API
## Activate the Environment
Run `source /env/bin/activate`

## Serve frorm the Flask Built-in Development Server
Run `flask run -h 0.0.0.0 -p 3000`

## Serve from  the Production WSGI Server - Gunicorn
Run `gunicorn -w 4 -b 0.0.0.0:3000 app:app`

## Methods/Endpoints
GET - /api/echo?term=string

GET - /api/env

GET - /api/kubernetes

GET - /api/cats

GET - /api/pokemon/:id

POST - /api/sum => Request Body { val1: int, val2: int }