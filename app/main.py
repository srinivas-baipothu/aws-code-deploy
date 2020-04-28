from flask import Flask
from flask_cors import CORS
from app.pprod_compilation.routes import pprod_compilation

app = Flask(__name__)

app.register_blueprint(pprod_compilation, url_prefix='/pprod_compilation')
cors = CORS(app)


@app.route('/')
def home():
    return 'App Home', 200


if __name__ == '__main__':
    app.run(debug=True)

