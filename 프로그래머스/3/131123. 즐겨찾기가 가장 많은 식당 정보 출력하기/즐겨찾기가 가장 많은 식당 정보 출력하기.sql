-- 코드를 입력하세요
SELECT B.FOOD_TYPE, B.REST_ID, B.REST_NAME, B.FAVORITES
FROM (SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
     FROM REST_INFO
     GROUP BY FOOD_TYPE) A, REST_INFO B
WHERE A.FOOD_TYPE = B.FOOD_TYPE AND A.FAVORITES = B.FAVORITES
ORDER BY FOOD_TYPE DESC