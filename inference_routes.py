from flask import Blueprint, request
from model import predict_sentiment


infer_r = Blueprint("inference", __name__)

@infer_r.route("/ask")
def ask():
    print("=====>  ", request.args)
    text = request.args.get("text")
    predictoion = predict_sentiment(text)
    response = text + " is " + predictoion
    return response
