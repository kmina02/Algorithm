-- 코드를 작성해주세요
SELECT
    CASE 
        WHEN SKILL_CODE & (select sum(code) from skillcodes where category = "Front End") > 0 AND SKILL_CODE & (select code from skillcodes where name = "Python") > 0 THEN "A"
        WHEN SKILL_CODE & (select code from skillcodes where name = "C#") > 0 THEN "B"
        WHEN SKILL_CODE & (select sum(code) from skillcodes where category = "Front End") > 0 THEN "C"
    END AS GRADE,
    ID, EMAIL
FROM
    DEVELOPERS
WHERE
    CASE 
        WHEN SKILL_CODE & (select sum(code) from skillcodes where category = "Front End") > 0 AND SKILL_CODE & (select code from skillcodes where name = "Python") > 0 THEN "A"
        WHEN SKILL_CODE & (select code from skillcodes where name = "C#") > 0 THEN "B"
        WHEN SKILL_CODE & (select sum(code) from skillcodes where category = "Front End") > 0 THEN "C"
    END IS NOT NULL

ORDER BY
    GRADE, ID
