{{ config(materialized='table') }}

select
    show_id,
    trim(title) as title,
    lower(trim(type)) as type,
    coalesce(nullif(trim(director), ''), 'Unknown') as director,
    coalesce(nullif(trim("cast"), ''), 'Unknown') as actors,
    coalesce(nullif(trim(country), ''), 'Unknown') as country,
    rating,
    duration,
    listed_in,
    description,
    release_year,
    cast(date_added as date) as date_added
from raw_movies
where show_id is not null