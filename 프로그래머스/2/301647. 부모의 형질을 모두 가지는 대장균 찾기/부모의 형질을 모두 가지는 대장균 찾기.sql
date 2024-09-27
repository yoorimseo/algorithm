-- 코드를 작성해주세요
SELECT B.ID, B.GENOTYPE, A.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA A
     JOIN ECOLI_DATA B
     ON A.ID = B.PARENT_ID
        AND A.GENOTYPE & B.GENOTYPE = A.GENOTYPE
ORDER BY 1;