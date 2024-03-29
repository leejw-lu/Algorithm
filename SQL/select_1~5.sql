-- 프로그래머스 SELECT 문제

-- [평균 일일 대여 요금 구하기]

SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE='SUV'

-- [조건에 맞는 도서 리스트 출력하기]
  
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') PUBLISHED_DATE
FROM BOOK
WHERE PUBLISHED_DATE LIKE '2021-%-%' AND CATEGORY ='인문'
ORDER BY PUBLISHED_DATE

-- [재구매가 일어난 상품과 회원 리스트 구하기]
  
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING count(PRODUCT_ID) > 1
ORDER BY USER_ID, PRODUCT_ID DESC
-- USER_ID ASC 생략

-- [12세 이하인 여자 환자 목록 출력하기]
  
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE<=12 AND GEND_CD='W'
ORDER BY AGE DESC, PT_NAME

-- [3월에 태어난 여성 회원 목록 출력하기]

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH)=3 AND GENDER='W' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID
