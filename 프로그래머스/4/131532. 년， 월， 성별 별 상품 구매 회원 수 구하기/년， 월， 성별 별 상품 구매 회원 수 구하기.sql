-- 코드를 입력하세요
SELECT
    YEAR(O.SALES_DATE) AS YEAR, 
    MONTH(O.SALES_DATE) AS MONTH, 
    U.GENDER AS GENDER,
    COUNT(DISTINCT U.USER_ID) AS USERS
FROM ONLINE_SALE AS O
JOIN USER_INFO AS U
ON O.USER_ID = U.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3