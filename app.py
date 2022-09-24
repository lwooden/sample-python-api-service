from flask import Flask, request, jsonify
import os
import requests
from models import Pokemon

app = Flask(__name__)


@app.route("/health", methods=['GET'])
def health_check():
    return "Sample Python API Service is healthy!"


@app.route("/api/echo", methods=["GET"])
def echo():
    args = request.args # captured all query parameters passed in the request
    term = args.get('term') # extract the 'term' query parameter and it's value
    return {
        "message": f"You said: {term}!"
    }

@app.route("/api/env", methods=['GET'])
def env():
    try:
        env = os.environ['ENV']
        return {
            "message": f"It looks like you are running in a {env} environment!"
        }
    except KeyError:
        return {
            "message": f"It looks like the environment variable ENV is not set! Please set it and try again",
            "error": f"{KeyError}"
        }, 400


@app.route("/api/sum", methods=["POST"])
def sum():
    params = request.get_json()
    val1 = params["val1"]
    val2 = params["val2"]

    sum = val1 + val2

    return {
        "sum": sum
    }

@app.route("/api/pokemon/<id>", methods=["GET"])
def fetch_pokemon(id):

    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    data = response.json()
    pokemon_id = data["id"]
    pokemon_name = data["name"]
    pokemon_experience = data["base_experience"]
    # pokemon = Pokemon(pokemon_id, pokemon_name, pokemon_experience)
    # new_pokemon = dict(pokemon)
    # print(pokemon_id, pokemon_name, pokemon_experience)

    return {
        "id": pokemon_id,
        "name": pokemon_name,
        "base_experience": pokemon_experience
    }

    # return jsonify(new_pokemon)


@app.route("/api/kubernetes", methods=["GET"])
def kubernetes():
    try:
        node= os.environ["NODE_NAME"]
        pod = os.environ["POD_NAME"]
        podIp = os.environ["POD_IP"]
        podNamespace = os.environ["POD_NAMESPACE"]
        podService = os.environ["POD_SERVICE"]

        return {
            "node": node,
            "pod": pod,
            "podIp": podIp,
            "podNamespace": podNamespace,
            "podService": podService
        }
    except KeyError:
         return {
            "message": f"It doesn't look like you are running in a Kubernetes Environment!",
            "error": f"{KeyError}"
        }, 400

