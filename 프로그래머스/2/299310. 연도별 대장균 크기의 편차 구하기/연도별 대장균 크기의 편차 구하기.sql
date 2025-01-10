-- 코드를 작성해주세요
SELECT
    B.YEAR,
    MAX_SIZE - SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM ECOLI_DATA A JOIN (SELECT
                              YEAR(DIFFERENTIATION_DATE) AS YEAR,
                              MAX(SIZE_OF_COLONY) AS MAX_SIZE
                        FROM ECOLI_DATA
                        GROUP BY YEAR) B
    ON YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY 1, 2