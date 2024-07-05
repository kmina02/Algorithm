-- 코드를 입력하세요
SELECT *
FROM PLACES
WHERE HOST_ID IN (
    select host_id
    from places
    group by host_id
    having count(host_id) >= 2
)

ORDER BY ID