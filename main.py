from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello from Flask"

if __name__ == "__main__":
    myapp.run(debug=True)
