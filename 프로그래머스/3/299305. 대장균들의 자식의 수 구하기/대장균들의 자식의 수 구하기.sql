-- 코드를 작성해주세요
SELECT ED1.ID, COUNT(ED2.ID) CHILD_COUNT
FROM ECOLI_DATA ED1 LEFT JOIN ECOLI_DATA ED2 ON ED1.ID = ED2.PARENT_ID
GROUP BY ED1.ID
ORDER BY ID ASC;