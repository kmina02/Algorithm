-- 코드를 입력하세요
SELECT CART_ID
FROM CART_PRODUCTS AS P1
WHERE NAME = "Yogurt"
    AND CART_ID IN (
    select cart_id
    from cart_products
    where name = "milk"
)
ORDER BY P1.CART_ID