-- 코드를 작성해주세요
SELECT
    ID, EMAIL, FIRST_NAME, LAST_NAME
FROM
    DEVELOPERS
WHERE
    (SKILL_CODE & (select code from skillcodes where name = 'Python')) OR
    (SKILL_CODE & (select code from skillcodes where name = 'C#'))
ORDER BY
    ID