{{ config(materialized='table') }}

select
    show_id,
    trim(title) as title,
    lower(trim(type)) as type,
    nullif(trim(director), '') as director,
    nullif(trim("cast"), '') as actors,
    nullif(trim(country), '') as country,
    rating,
    duration,
    listed_in,
    description,
    release_year,
    cast(date_added as date) as date_added
from raw_movies
where show_id is not null