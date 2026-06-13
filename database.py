import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

username = os.getenv('user')
password = os.getenv('password')
port = os.getenv('port')
db = os.getenv('db')

engine = create_engine(
f"postgresql+psycopg://{username}:{password}@localhost:{port}/{db}"
)