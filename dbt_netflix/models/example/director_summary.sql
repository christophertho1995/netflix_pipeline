select 
    director, 
    count(*) as title_count 
from {{ ref('clean_movies') }}
where director is not null
group by director
order by title_count desc
limit 10
