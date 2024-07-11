SELECT ID, 
    CASE WHEN RANK_SIZE <= (select COUNT(*) from ecoli_data)* 0.25 THEN "CRITICAL"
    WHEN RANK_SIZE <= (select COUNT(*) from ecoli_data)* 0.5 THEN "HIGH"
    WHEN RANK_SIZE <= (select COUNT(*) from ecoli_data)* 0.75 THEN "MEDIUM"
    ELSE "LOW"
    END AS COLONY_NAME
FROM (
    SELECT ID, RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS rank_size
    FROM ECOLI_DATA
) AS A
ORDER BY 1