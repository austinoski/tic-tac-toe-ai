import pickle, json
from urllib import response
import numpy as np
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


# Initialize app
app = Flask(__name__)
api = Api(app)
CORS(app)

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
