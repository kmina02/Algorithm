SELECT h.history_id,
    FLOOR(
        CASE
            -- 90일 이상인 경우
            WHEN DATEDIFF(h.end_date, h.start_date) + 1 >= 90 THEN c.daily_fee * (DATEDIFF(h.end_date, h.start_date) + 1) * (1 - dp_90.discount_rate / 100)
            -- 30일 이상 90일 미만인 경우
            WHEN DATEDIFF(h.end_date, h.start_date) + 1 >= 30 THEN c.daily_fee * (DATEDIFF(h.end_date, h.start_date) + 1) * (1 - dp_30.discount_rate / 100)
            -- 7일 이상 30일 미만인 경우
            WHEN DATEDIFF(h.end_date, h.start_date) + 1 >= 7 THEN c.daily_fee * (DATEDIFF(h.end_date, h.start_date) + 1) * (1 - dp_7.discount_rate / 100)
            -- 7일 미만인 경우
            ELSE c.daily_fee * (DATEDIFF(h.end_date, h.start_date) + 1)
        END
    ) AS fee
FROM car_rental_company_rental_history AS h
JOIN car_rental_company_car AS c
    ON c.car_id = h.car_id
-- 각 기간별 할인율을 가져오기 위해 세 번의 JOIN 사용
LEFT JOIN car_rental_company_discount_plan AS dp_90
    ON c.car_type = dp_90.car_type AND dp_90.duration_type = '90일 이상'
LEFT JOIN car_rental_company_discount_plan AS dp_30
    ON c.car_type = dp_30.car_type AND dp_30.duration_type = '30일 이상'
LEFT JOIN car_rental_company_discount_plan AS dp_7
    ON c.car_type = dp_7.car_type AND dp_7.duration_type = '7일 이상'
WHERE c.car_type = '트럭'
ORDER BY fee DESC, h.history_id DESC;
