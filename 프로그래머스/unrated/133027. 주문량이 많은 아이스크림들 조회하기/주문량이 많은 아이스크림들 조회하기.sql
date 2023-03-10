-- 코드를 입력하세요
SELECT FLAVOR
FROM (
    SELECT FIRST_HALF.FLAVOR, SUM(FIRST_HALF.TOTAL_ORDER + JULY.TOTAL_ORDER) AS TOTAL
    FROM FIRST_HALF
    INNER JOIN JULY USING (FLAVOR)
    GROUP BY FLAVOR
) AS SUB
ORDER BY TOTAL DESC
LIMIT 3