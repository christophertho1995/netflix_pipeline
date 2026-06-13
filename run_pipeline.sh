#!/bin/bash

set -e

cd /home/christophertho1/projects/netflix_pipeline

source .venv/bin/activate

echo "Starting to load raw data..."
python loader.py

cd dbt_netflix
echo "Running dbt models..."
dbt run

echo "Running dbt tests..."
dbt test