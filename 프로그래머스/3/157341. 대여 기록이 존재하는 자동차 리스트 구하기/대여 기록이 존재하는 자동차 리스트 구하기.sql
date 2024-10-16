-- 코드를 입력하세요
SELECT DISTINCT R.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR R
WHERE CAR_TYPE = '세단' AND
      (SELECT DISTINCT H.CAR_ID
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
      WHERE MONTH(START_DATE) = 10 AND R.CAR_ID = H.CAR_ID)         
ORDER BY 1 DESC;