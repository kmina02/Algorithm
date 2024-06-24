-- 코드를 입력하세요
select 
    fp.PRODUCT_ID,
    fp.PRODUCT_NAME,
    sum(fp.price * fo.amount) as TOTAL_SALES
from 
    food_product as fp
join
    food_order as fo
on 
    fp.product_id = fo.product_id
where
    year(fo.produce_date) = 2022 and
    month(fo.produce_date) = 05
group by
    fp.product_id
order by 
    sum(fp.price * fo.amount) desc,
    fp.product_id asc
    