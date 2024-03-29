-- 코드를 입력하세요
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE M
JOIN REST_REVIEW R
ON M.MEMBER_ID LIKE R.MEMBER_ID

WHERE M.MEMBER_NAME LIKE (
    SELECT M.MEMBER_NAME
    FROM MEMBER_PROFILE M
    JOIN REST_REVIEW R
    ON M.MEMBER_ID LIKE R.MEMBER_ID
    GROUP BY M.MEMBER_ID
    ORDER BY COUNT(R.REVIEW_ID) DESC
    LIMIT 1
)
ORDER BY R.REVIEW_DATE, REVIEW_TEXT