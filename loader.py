from pathlib import Path

import kagglehub
import pandas as pd

from database import engine

DATASET_HANDLE = "shivamb/netflix-shows"
DATASET_FILE = "netflix_titles.csv"

def pull_netflix_data() -> pd.DataFrame:
    """Pull the latest Netflix titles dataset from Kaggle."""
    dataset_dir = Path(kagglehub.dataset_download(DATASET_HANDLE))
    return pd.read_csv(dataset_dir / DATASET_FILE)

if __name__ == "__main__":
    raw_df = pull_netflix_data()

    raw_df.to_sql(
        "raw_movies",
        engine,
        if_exists="replace",
        index=False
    )
    
    print("Successfully loaded data to postgresql server")
    