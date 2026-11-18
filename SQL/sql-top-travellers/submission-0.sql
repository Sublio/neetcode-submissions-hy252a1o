SELECT  users.name, COALESCE(SUM(rides.distance), 0) AS travelled_distance
FROM users
LEFT JOIN rides ON users.id = rides.user_id
GROUP BY users.id, users.name
ORDER BY travelled_distance DESC, users.name;