import pandas as pd

from fastapi import FastAPI

from database import engine

app = FastAPI()

@app.get("/movies")
def get_all_movies():
    df = pd.read_sql(
        "select * from clean_movies order by show_id desc limit 10",
        engine
    )

    return df.to_dict("records")