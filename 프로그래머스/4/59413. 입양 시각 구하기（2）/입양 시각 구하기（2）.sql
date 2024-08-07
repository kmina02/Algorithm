-- 코드를 입력하세요
WITH RECURSIVE cte(n) AS (
    SELECT 0
    UNION ALL
    SELECT N+1 FROM CTE WHERE N < 23
)
SELECT N AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM CTE
LEFT JOIN ANIMAL_OUTS
ON N = HOUR(DATETIME)
GROUP BY 1
ORDER BY 1