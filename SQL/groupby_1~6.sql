-- 프로그래머스 GROUP BY 파트
-- GROUP BY로 묶으면 가장 상단에 있는 데이터들을 임의로 가져온다.
-- > SELECT에 MAX를 해도 최대값을 가져오는것이 아닌 그룹화된 테이블 가장 상단을 가져오게 된다.

-- 즐겨찾기가 가장 많은 식당 정보 출력하기 (WHERE+ 서브쿼리)

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN 
    (SELECT FOOD_TYPE, MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC

-- 조건에 맞는 사용자와 총 거래금액 조회하기 (그냥 JOIN은 INNER JOIN)

SELECT A.USER_ID, A.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER A
JOIN USED_GOODS_BOARD B ON A.USER_ID=B.WRITER_ID
WHERE B.STATUS='DONE'
GROUP BY B.WRITER_ID
HAVING TOTAL_SALES>=700000
ORDER BY TOTAL_SALES

-- 저자 별 카테고리 별 매출액 집계하기

SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(B.PRICE*BS.SALES) AS TOTAL_SALES
FROM BOOK B JOIN BOOK_SALES BS ON B.BOOK_ID=BS.BOOK_ID
JOIN AUTHOR A ON B.AUTHOR_ID=A.AUTHOR_ID
-- WHERE YEAR(BS.SALES_DATE) = 2022 AND MONTH(BS.SALES_DATE) =1
WHERE BS.SALES_DATE LIKE '2022-01%'
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY B.AUTHOR_ID, B.CATEGORY DESC

-- 카테고리 별 도서 판매량 집계하기

SELECT B.CATEGORY, SUM(BS.SALES) AS TOTAL_SALES
FROM BOOK B JOIN BOOK_SALES BS ON B.BOOK_ID=BS.BOOK_ID
WHERE BS.SALES_DATE LIKE '2022-01%'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY

-- 자동차 대여 기록에서 대여중/대여 가능 여부 구분하기 (가상필드: CASE WHEN /THEN /ELSE /END)

SELECT CAR_ID, MAX(CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE 
                    THEN '대여중' ELSE '대여 가능' END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC
-- SELECT에 MAX()를 사용한 이유 : 가장 최신 날짜 데이터를 가져오게 한다.

-- 진료과별 총 예약 횟수 출력하기

SELECT MCDP_CD AS '진료과코드', COUNT(MCDP_CD) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
-- ORDER BY COUNT(MCDP_CD), MCDP_CD
ORDER BY 5월예약건수, 진료과코드