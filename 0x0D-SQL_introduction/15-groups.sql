-- computes the score average in a table in database on MySQL server
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
