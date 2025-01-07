WITH FRONT_END AS (
    SELECT SUM(CODE) AS TOTAL_CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT TOTAL_CODE 
                    FROM FRONT_END) > 0
ORDER BY ID;