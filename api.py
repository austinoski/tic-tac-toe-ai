import pickle, json, os
import numpy as np
from flask import (
    Flask,
    request,
    render_template,
    send_from_directory
)
from flask_restful import Resource, Api
from flask_cors import CORS


# Initialize app
app = Flask(__name__)
api = Api(app)
CORS(app)


# Serve staticfiles from frontend directory
@app.route("/js/<path:path>")
@app.route("/css/<path:path>")
def serve_static_file(path):
    resource_path = request.path[1:].split('/')
    resource_path = "/".join(resource_path)
    return send_from_directory(
        directory="templates",
        path=resource_path
    )


# Route to serve frontend application
@app.route("/")
def index():
    return render_template("index.html")


# load saved model
with open("tic-tac-toe_model.pkl", "rb") as f:
    model = pickle.load(f)


# endpoint to make predictions
class PredictMove(Resource):
    def post(self):
        """Takes a board configuration and predicts the next move"""
        board = json.loads(request.data)["board"]
        board = np.array(board).reshape([1, -1])
        move = model.predict(board)
        return {"move": int(move[0])}


api.add_resource(PredictMove, '/predict')
