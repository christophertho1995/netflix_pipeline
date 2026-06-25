# GET /movies/{id}
# GET /summary

import pandas as pd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine

app = FastAPI()

origins = ["http://localhost:5173"] # React dev server
app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]
)

@app.get("/movies")
def get_all_movies():
    df = pd.read_sql(
        "select * from clean_movies order by show_id desc limit 100",
        engine
    )

    return df.to_dict("records")