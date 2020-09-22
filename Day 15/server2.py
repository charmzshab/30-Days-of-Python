from fastapi import FastAPI
from logger import trigger_log_save
from scrape import run as scrape_runner


app = FastAPI()


@app.get("/")
def hello_world():
    return {"hello": "world"}


@app.get("/abc")
def abc_view():
    return {"hello": ["Shabix", "Lampard", "Owakabi"]}


@app.post("/box-office-mojo-scraper")
def scrape_runner_view():
    trigger_log_save()
    scrape_runner()
    return {"data": ["Shabix", "Lampard", "Owakabi"]}

