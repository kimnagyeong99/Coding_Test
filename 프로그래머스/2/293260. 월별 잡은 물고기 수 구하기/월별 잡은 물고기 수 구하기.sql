-- 코드를 작성해주세요
SELECT COUNT(*) FISH_COUNT, MONTH(TIME) MONTH
FROM FISH_INFO
GROUP BY MONTH(TIME)
ORDER BY MONTH ASC;