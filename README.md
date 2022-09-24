## Activate the Environment
Run `source /env/bin/activate`

## Serve frorm the Flask Built-in Development Server
Run `flask run -h 0.0.0.0 -p 3000`

## Serve from  the Production WSGI Server - Gunicorn
Run `gunicorn -w 4 -b 0.0.0.0:3000 app:app`