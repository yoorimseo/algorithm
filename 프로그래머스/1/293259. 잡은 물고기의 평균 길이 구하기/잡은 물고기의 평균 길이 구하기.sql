-- 코드를 작성해주세요
SELECT ROUND(AVG(LENGTH), 2) AS AVERAGE_LENGTH
FROM (SELECT
        CASE WHEN LENGTH IS NULL THEN 10
            ELSE LENGTH
        END LENGTH
     FROM FISH_INFO) A