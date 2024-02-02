-- 프로그래머스
-- 자동차 대여 기록에서 장기/단기 대여 구분하기

SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE,'%Y-%m-%d') AS START_DATE, DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE, 
    CASE WHEN DATEDIFF(END_DATE, START_DATE)+1>=30 THEN "장기 대여" 
    ELSE "단기 대여" END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%' 
ORDER BY HISTORY_ID DESC

-- 특정 옵션이 포함된 자동차 리스트 구하기

SELECT * FROM CAR_RENTAL_COMPANY_CAR WHERE OPTIONS LIKE '%네비게이션%' ORDER BY CAR_ID DESC

-- 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기

SELECT CONCAT('/home/grep/src/',F.BOARD_ID,'/',F.FILE_ID,F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD B JOIN USED_GOODS_FILE F ON B.BOARD_ID=F.BOARD_ID
WHERE B.VIEWS=(SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY F.FILE_ID DESC

-- 중성화 여부 파악하기

-- 카테고리 별 상품 개수 구하기

-- DATETIME에서 DATE로 형 변환

-- 조건별로 분류하여 주문상태 출력하기