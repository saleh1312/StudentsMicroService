from flask import Flask
from uploading_routes import uploading_routes
from inference_routes import infer_r

app = Flask(__name__)
app.register_blueprint(uploading_routes)
app.register_blueprint(infer_r)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
