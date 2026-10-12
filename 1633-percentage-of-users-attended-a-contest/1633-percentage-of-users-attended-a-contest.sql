SELECT
    contest_id,
    ROUND(COUNT(DISTINCT r.user_id) * 100.0 /
          (select count(user_id) from users), 2) AS percentage
FROM Register r 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;