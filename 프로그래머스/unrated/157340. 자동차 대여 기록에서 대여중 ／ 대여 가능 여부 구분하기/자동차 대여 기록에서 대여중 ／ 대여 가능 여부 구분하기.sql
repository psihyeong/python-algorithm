SELECT CAR_ID,
    MAX(CASE WHEN '2022-10-16' BETWEEN DATE_FORMAT(START_DATE, '%Y-%m-%d') AND DATE_FORMAT(END_DATE, '%Y-%m-%d')
    THEN '대여중'
    ELSE '대여 가능'
    END) AS 'AVAILABILITY'
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC

/* 
1. BETWEEN을 사용해 START_DATE와 END_DATE사이에 기준날짜 '2022-10-16'가 있는지 체크한다.
2. CASE문으로 기준날짜가 포함되면 대여중 아니면 대여 가능으로 표시한다. (CASE WHEN 조건 THEN 부합한 경우 ELSE 아닌 경우 END)
3. GROUP BY를 사용해 CAR_ID로 묶어준다. MAX를 사용하면 대여중 항목이 있는 경우 대여중, 없으면 대여 가능으로 표시된다.
4. ORDER BY로 CAR_ID 내림차순 정렬.
*/