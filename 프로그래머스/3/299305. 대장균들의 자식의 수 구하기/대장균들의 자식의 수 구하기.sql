-- 코드를 작성해주세요
SELECT E.ID, COALESCE(C.CHILD_COUNT, 0) AS CHILD_COUNT
FROM ECOLI_DATA AS E
LEFT JOIN (
    select parent_id as id, count(*) as child_count
    from ecoli_data
    where id is not null
    group by parent_id
) AS C
ON E.ID = C.ID