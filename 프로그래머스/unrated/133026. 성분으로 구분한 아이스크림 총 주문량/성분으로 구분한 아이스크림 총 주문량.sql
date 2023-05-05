SELECT B.INGREDIENT_TYPE, sum(A.TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF A ,ICECREAM_INFO B
where A.FLAVOR=B.FLAVOR
group by B.INGREDIENT_TYPE
order by TOTAL_ORDER asc