-- solution I
SELECT 
    actor_id,
    director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;

-- solution II
SELECT 
    actor_id,
    director_id
FROM (
    actor_id,
    director_id,
    COUNT(*) AS num_of_coo
) AS CooP
WHERE num_of_coo >= 3;