-- 코드를 입력해주세요.
SELECT 
    YEAR(DIFFERENTIATION_DATE) AS YEAR, 
    ABS(SIZE_OF_COLONY - MAX_DATA.MAX_SIZE) AS YEAR_DEV,
    ID
FROM
    ECOLI_DATA
LEFT JOIN
    (
    select year(differentiation_date) as year, max(size_of_colony) as max_size
	from ecoli_data
	group by year(differentiation_date)
    ) AS MAX_DATA
ON
    YEAR(ECOLI_DATA.DIFFERENTIATION_DATE) = MAX_DATA.YEAR
ORDER BY
    YEAR, YEAR_DEV