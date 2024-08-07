-- 프로그래머스 집계함수 (SUM, MAX, MIN)

-- 가격이 제일 비싼 식품의 정보 출력하기

SELECT * FROM FOOD_PRODUCT 
WHERE PRICE=(SELECT MAX(PRICE) FROM FOOD_PRODUCT)
-- SELECT * FROM FOOD_PRODUCT ORDER BY PRICE DESC LIMIT 1

-- 가장 비싼 상품 구하기

SELECT MAX(PRICE) AS MAX_PRICE FROM PRODUCT

-- 최댓값 구하기

SELECT MAX(DATETIME) AS 시간 FROM ANIMAL_INS

-- 최솟값 구하기

SELECT MIN(DATETIME) AS 시간 FROM ANIMAL_INS

-- 동물 수 구하기

SELECT COUNT(*) AS count FROM ANIMAL_INS

-- 중복 제거하기 (COUNT(DISTINCT 속성))

SELECT COUNT(DISTINCT NAME) AS count FROM ANIMAL_INS WHERE NAME IS NOT NULL

-- 조건에 맞는 아이템들의 가격의 총합 구하기

SELECT SUM(PRICE) AS TOTAL_PRICE FROM ITEM_INFO WHERE RARITY='LEGEND'