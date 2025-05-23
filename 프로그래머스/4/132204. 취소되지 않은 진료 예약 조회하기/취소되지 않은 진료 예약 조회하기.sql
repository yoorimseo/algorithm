-- 코드를 입력하세요
SELECT
    APNT_NO,
    PT_NAME,
    A.PT_NO,
    A.MCDP_CD,
    (SELECT DR_NAME FROM DOCTOR WHERE DR_ID = A.MDDR_ID) AS DR_NAME,
    APNT_YMD
FROM APPOINTMENT A JOIN PATIENT P
    ON A.PT_NO = P.PT_NO
WHERE A.MCDP_CD = 'CS'
    AND A.APNT_CNCL_YN = 'N'
    AND A.APNT_YMD LIKE '2022-04-13%'
ORDER BY APNT_YMD