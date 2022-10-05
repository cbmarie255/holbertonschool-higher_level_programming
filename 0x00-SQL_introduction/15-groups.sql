-- listing the number of records with the sam scoew in the second_table
-- using GROUP
SELECT score,COUNT(*) as 'number' FROM second_table GROUP BY score ORDER BY COUNT(*) DESC;
