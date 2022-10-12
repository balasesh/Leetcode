select
    neighborhood.name
from
    user
    JOIN neighborhood on neighborhood.id = user.neighborhood_id
GROUP by
    neighborhood.name
HAVING
    COUNT(user.id) = 0