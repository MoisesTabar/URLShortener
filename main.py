from dotenv import load_dotenv
from routes import router
from flask import Flask

def main() -> None:

    app = Flask(__name__)

    app.register_blueprint(router)

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

if __name__ == "__main__":

    main()