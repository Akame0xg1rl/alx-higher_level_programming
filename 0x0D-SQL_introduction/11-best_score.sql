-- Script to list all records with a score >= 10 in second_table ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
