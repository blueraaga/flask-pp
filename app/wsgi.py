from application import create_app
from dotenv import load_dotenv


load_dotenv(verbose=True)

app = create_app()

if __name__ == "__main__":
    print("[LOC] Running app")
    app.run(host='0.0.0.0')