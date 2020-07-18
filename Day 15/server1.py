from flask import Flask
from logger import trigger_log_save
from scrape import run as scrape_runner

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, world. this is Flask"


# http://localhost:8000/abc_view
@app.route("/abc_view", methods=["GET"])
def abc_view():
    return "Hello, world. this is Awesome"


@app.route("/box-office-mojo-scraper", methods=["POST"])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1, 2, 3]}


# if __name__ == "__main__":
#     app.run(debug=True)

