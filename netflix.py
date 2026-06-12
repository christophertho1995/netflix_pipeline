from pathlib import Path
import os
from dotenv import load_dotenv

import kagglehub
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

DATASET_HANDLE = "shivamb/netflix-shows"
DATASET_FILE = "netflix_titles.csv"
OUTPUT_FILE = Path(__file__).with_name("netflix_titles_cleaned.csv")


def pull_netflix_data() -> pd.DataFrame:
    """Pull the latest Netflix titles dataset from Kaggle."""
    dataset_dir = Path(kagglehub.dataset_download(DATASET_HANDLE))
    return pd.read_csv(dataset_dir / DATASET_FILE)


def clean_netflix_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return an analysis-ready copy of the Netflix dataset."""
    cleaned = df.copy()

    # Duplicate rows add no information and can distort counts during analysis.
    cleaned = cleaned.drop_duplicates(subset="show_id", keep="first")

    # Remove accidental surrounding whitespace without changing missing values.
    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns
    cleaned[text_columns] = cleaned[text_columns].apply(
        lambda column: column.str.strip()
    )

    # Three movie durations were shifted into the rating column in the source data.
    misplaced_duration = (
        cleaned["duration"].isna()
        & cleaned["rating"].str.fullmatch(r"\d+ min", na=False)
    )
    cleaned.loc[misplaced_duration, "duration"] = cleaned.loc[
        misplaced_duration, "rating"
    ]
    cleaned.loc[misplaced_duration, "rating"] = pd.NA

    # Use a real date type so dates can be sorted, filtered, and grouped reliably.
    cleaned["date_added"] = pd.to_datetime(
        cleaned["date_added"], format="%B %d, %Y", errors="coerce"
    )

    # These missing values mean the source does not provide the information.
    # Keeping the rows and labeling them avoids losing otherwise useful titles.
    unknown_columns = ["director", "cast", "country", "rating", "duration"]
    cleaned[unknown_columns] = cleaned[unknown_columns].fillna("Unknown")

    return cleaned.reset_index(drop=True)


if __name__ == "__main__":
    raw_df = pull_netflix_data()
    # cleaned_df = clean_netflix_data(raw_df)
    # cleaned_df.to_csv(OUTPUT_FILE, index=False)

    # print(f"Cleaned {len(cleaned_df):,} Netflix titles and saved them to {OUTPUT_FILE}")
    # print(cleaned_df.head())

    username = os.getenv('user')
    password = os.getenv('password')
    port = os.getenv('port')
    db = os.getenv('db')

    engine = create_engine(
    f"postgresql+psycopg://{username}:{password}@localhost:{port}/{db}"
    )

    raw_df.to_sql(
        "raw_movies",
        engine,
        if_exists="replace",
        index=False
    )
    
    print("Successfully loaded data to postgresql server")
    