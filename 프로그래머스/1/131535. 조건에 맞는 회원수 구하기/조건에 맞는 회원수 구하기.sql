-- 코드를 입력하세요
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE JOINED LIKE "2021%" AND 20 <= AGE AND AGE <= 29 